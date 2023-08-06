import re
import csv
from io import StringIO
import xlrd
from os import path

from PyQt5 import QtWidgets
import chardet

from openstereo.ui.import_dialog_ui import Ui_Dialog as import_dialog_Ui_Dialog

keep_chars = re.compile("\W+")


def get_dialect_data(dialect):
    return {
        "delimiter": dialect.delimiter,
        "doublequote": dialect.doublequote,
        "escapechar": dialect.escapechar,
        "lineterminator": dialect.lineterminator,
        "quotechar": dialect.quotechar,
        "quoting": dialect.quoting,
        "skipinitialspace": True,
    }


# is this a good name?
class Importer:
    direction_names = ["direction", "dipdirection", "dd", "clar", "dipdir"]
    dip_names = ["dip", "d"]
    trend_names = ["trend", "azimuth," "direction", "dipdirection"]
    plunge_names = ["plunge", "dip"]
    obliquity_names = ["rake", "obliquity"]
    alpha_names = ["alpha", "angle", "semiapicalangle", "opening"]
    sample_size = 1024
    default_comment = "#"
    header = None
    # geoeas = None

    def __init__(
        self,
        data_type=None,
        direction=False,
        rake=False,
        fname=None,
        dialect=None,
        comment=None,
    ):
        self.fname = fname
        self.ext = path.splitext(fname)[1]

        self.csv_sniffer = csv.Sniffer()

        self.sample = None
        self.worksheet = None

        self.header = []

        self.dialect = (
            dialect
            if dialect is not None
            else get_dialect_data(csv.get_dialect("excel"))
        )  # TODO: set to none if non csv

        self.encoding = None

        # self.geoeas = False

        self.data_type = data_type if data_type is not None else "plane"

        self.direction = direction
        self.rake = rake

        self.header_row = 0
        self.has_header = False

        if comment is None:
            self.comment_marker = self.default_comment
        else:
            self.comment_marker = comment

        self.skip_lines = 0
        self.do_skip = False

    def get_header(self):
        return getattr(
            self,
            "get_header_{}".format(self.ext.strip(".")),
            self.get_header_csv,
        )()

    def get_header_csv(self):
        reader = csv.reader(  # should it really get it from sample?
            skip_comments(StringIO(self.sample), self.comment_marker),
            **self.dialect,  # should it skip comments?
        )
        header_row = self.header_row
        if self.do_skip:
            header_row += self.skip_rows
        for lineno in range(header_row + 1):
            header = next(reader)
        return header

    def get_header_xlsx(self):
        book = xlrd.open_workbook(self.fname)
        sheet = book.sheet_by_name(self.worksheet)
        header_row = self.header_row
        if self.do_skip:
            header_row += self.skip_rows
        return sheet.row_values(header_row)

    def get_header_xls(self):  # abstract these to a "plugin module, maybe"
        return self.get_header_xlsx()

    def sniff_columns(self):
        getattr(
            self,
            "sniff_columns_{}".format(self.data_type),
            self.sniff_columns_plane,
        )()

    def normalize_column_name(self, column):
        if isinstance(column, str):
            return keep_chars.sub("", column).lower()
        else:
            return ""

    def sniff_columns_plane(self):
        n_header = len(self.header) - 1
        self.longitude = min(n_header, 0)
        self.colatitude = min(n_header, 1)
        self.alpha = None
        self.obliquity = None

        for i, column in enumerate(self.header):
            if self.normalize_column_name(column) in self.direction_names:
                self.longitude = i
                break
        for i, column in enumerate(self.header):
            if self.normalize_column_name(column) in self.dip_names:
                self.colatitude = i
                break

    def sniff_columns_line(self):
        n_header = len(self.header) - 1
        self.longitude = min(n_header, 0)
        self.colatitude = min(n_header, 1)
        self.alpha = None
        self.obliquity = None

        for i, column in enumerate(self.header):
            if self.normalize_column_name(column) in self.trend_names:
                self.longitude = i
                break
        for i, column in enumerate(self.header):
            if self.normalize_column_name(column) in self.plunge_names:
                self.colatitude = i
                break

    def sniff_columns_rake(self):
        self.sniff_columns_plane()
        n_header = len(self.header) - 1
        self.obliquity = min(n_header, 2)
        for i, column in enumerate(self.header):
            if self.normalize_column_name(column) in self.obliquity_names:
                self.obliquity = i
                break

    def sniff_columns_smallcircle(self):
        self.sniff_columns_line()
        n_header = len(self.header) - 1
        self.alpha = min(n_header, 2)
        for i, column in enumerate(self.header):
            if self.normalize_column_name(column) in self.alpha_names:
                self.alpha = i
                break

    def sniff_columns_circular(self):
        n_header = len(self.header) - 1
        self.longitude = min(n_header, 0)
        self.colatitude = None
        self.alpha = None
        self.obliquity = None
        for i, column in enumerate(self.header):
            if self.normalize_column_name(column) in self.trend_names:
                self.longitude = i
                break

    def sniff_dialect(self):
        self.sample = self.read_sample()
        try:
            self.dialect = get_dialect_data(
                self.csv_sniffer.sniff(self.sample)
            )
        except csv.Error:
            self.dialect = get_dialect_data(csv.get_dialect("excel"))
        return self.dialect

    def sniff_header(self):  # is this OK?
        for field in self.header:
            try:
                float(str(field))
                return False
            except ValueError:
                pass
        return True

    def sniff_encoding(self):  # TODO: where to call this?
        detector = chardet.UniversalDetector()
        with open(self.fname, "rb") as f:
            for line in f:
                detector.feed(line)
                if detector.done:
                    break
        detector.close()
        self.encoding = detector.result["encoding"]

    def read_sample(self):
        if self.encoding is None:
            self.sniff_encoding()
        read_length = 0
        sample = []
        with open(self.fname, "r", encoding=self.encoding) as f:
            for line in skip_comments(f, self.comment_marker):
                sample.append(line)
                read_length += len(sample)
                if read_length > self.sample_size:
                    break
        return "".join(sample)

    def get_data(self):
        return getattr(
            self, "get_data_{}".format(self.ext.strip(".")), self.get_data_csv
        )()

    def get_data_csv(self):
        f = open(self.fname, "r", encoding=self.encoding)
        # f.seek(self.offset)
        if self.do_skip:
            skip_rows = self.skip_rows
        else:
            skip_rows = 0
        if self.has_header:
            skip_rows += self.header_row + 1
        reader = csv.reader(
            skip_comments(f, self.comment_marker), **self.dialect
        )
        for i in range(skip_rows):
            next(reader)
        return reader

    def get_data_xlsx(self):
        book = xlrd.open_workbook(self.fname)
        sheet = book.sheet_by_name(self.worksheet)
        header_row = 0
        if self.has_header:
            header_row += self.header_row + 1
        if self.do_skip:
            header_row += self.skip_rows
        return skip_comments_xlsx(
            [sheet.row_values(i) for i in range(header_row, sheet.nrows)],
            self.comment_marker,
        )

    def get_data_xls(self):
        return self.get_data_xlsx()

    def process_file(self):
        if self.fname:
            getattr(
                self,
                "process_file_{}".format(self.ext.strip(".")),
                self.process_file_csv,
            )()
        else:
            pass

    def process_file_csv(self):
        if self.encoding is None:
            self.sniff_encoding()
        self.sample = self.read_sample()
        self.sniff_dialect()
        self.header = self.get_header()
        self.has_header = self.sniff_header()
        self.sniff_columns()

    def process_file_xlsx(self):
        book = xlrd.open_workbook(self.fname)
        self.worksheets = book.sheet_names()  # TODO: check if necessary
        self.worksheet = self.worksheets[0]
        self.header = self.get_header()  # how to set the worksheet to first?
        self.sniff_columns()

    def process_file_shp(self):
        pass

    def import_data(self):  # TODO: rework all this, rly
        data = {  # TODO:  add direction, rake?
            "worksheet": self.worksheet,
            "keep_input": True,  # TODO: remove this
            "line": True
            if self.data_type in ["line", "smallcircle", "rake", "circular"]
            else False,
            "attitude_type": self.data_type,
            "dip_direction": not self.direction,  # normalize
            "dipdir_column": self.longitude,
            "dip_column": self.colatitude,
            "alpha_column": self.alpha,
            "obliquity_column": self.obliquity,
            "circular": self.data_type == "circular",
            "rake": self.data_type == "rake",
            "data_headers": self.header if self.has_header else None,
            "has_header": self.has_header,
            "header_row": self.header_row if self.has_header else None,
            "skip_rows": self.skip_rows if self.do_skip else None,
            "comment_marker": self.comment_marker,
        }
        if self.dialect is not None:
            data["dialect_data"] = self.dialect
        return data


class ImportDialog(QtWidgets.QDialog, import_dialog_Ui_Dialog):
    def __init__(
        self,
        parent=None,
        fname=None,
        data_type=None,
        direction=False,
        rake=False,
    ):
        super(ImportDialog, self).__init__(parent)
        self.setupUi(self)

        self.importer = Importer(
            fname=fname, data_type=data_type, direction=direction, rake=rake
        )

        if data_type:
            self.data_type = data_type
        if direction:
            self.planetype.setCurrentIndex(1)
        if rake:
            self.linetype.setCurrentIndex(1)

        self.importer.process_file()

        # if fname:
        self.fname.setText(fname)

        self.comment_marker.setText(self.importer.comment_marker)
        self.ext = self.importer.ext
        self.fname.editingFinished.connect(self.on_file_selected)  # remove?
        self.browse.clicked.connect(self.on_browse)  # remove?
        for widget in (
            self.lines,
            self.planes,
            self.small_circle,
            self.circular,
        ):
            widget.toggled.connect(self.on_type_changed)
        self.planetype.currentIndexChanged.connect(self.on_type_changed)
        self.linetype.currentIndexChanged.connect(self.on_type_changed)
        self.delimiter.editingFinished.connect(self.on_delimiter_changed)
        self.has_header.stateChanged.connect(self.on_header_changed)
        self.header_row.valueChanged.connect(self.on_header_changed)
        self.do_skip.stateChanged.connect(self.on_skip_rows)
        self.skip_rows.valueChanged.connect(self.on_skip_rows)

        self.longitude.currentIndexChanged.connect(self.on_column_change)
        self.colatitude.currentIndexChanged.connect(self.on_column_change)
        self.rake.currentIndexChanged.connect(self.on_column_change)
        self.alpha.currentIndexChanged.connect(self.on_column_change)

        self.on_type_changed()

        self.on_file_selected()

    # TODO: colapse these
    # region file settings
    def set_headers_on_dialog(self, headers):  # ui
        for widget in (self.longitude, self.colatitude, self.alpha, self.rake):
            widget.clear()
            for header in headers:
                widget.addItem(str(header))
            # add sniffer behaviour here

    def on_worksheet_changed(self):
        self.on_header_changed()

    def on_delimiter_changed(self):
        # self.dialect.delimiter = (
        #     str(self.delimiter.text()).strip("'").strip('"')
        # )
        self.importer.dialect["delimiter"] = (
            str(self.delimiter.text()).strip("'").strip('"')
        )
        self.on_header_changed()

    def on_skip_rows(self):
        self.importer.do_skip = self.do_skip.isChecked()
        self.importer.skip_rows = self.skip_rows.value()
        if self.importer.ext in [".xls", ".xlsx"]:
            pass
        else:
            self.importer.sample = self.importer.read_sample()
        self.on_header_changed()

    def on_header_changed(self):
        self.importer.has_header = self.has_header.isChecked()
        self.importer.header_row = self.header_row.value()
        self.importer.header = self.importer.get_header()
        if self.has_header.isChecked():
            self.set_headers_on_dialog(self.importer.header)
        else:
            self.set_headers_on_dialog(list(range(len(self.importer.header))))
        self.on_type_changed()
        # endregion

    # region type changed
    def on_type_changed(self):
        if (
            self.lines.isChecked()
            or self.small_circle.isChecked()
            or self.circular.isChecked()
        ):
            self.longitude_label.setText("Trend")
            self.longitude.setEnabled(True)
            self.colatitude_label.setText("Plunge")
            self.colatitude.setEnabled(not self.circular.isChecked())
            self.alpha.setEnabled(self.small_circle.isChecked())
            if self.lines.isChecked() and self.linetype.currentIndex() == 1:
                self.rake.setEnabled(True)
                if self.planetype.currentIndex() == 0:
                    self.longitude_label.setText("Dip Direction")
                else:
                    self.longitude_label.setText("Direction")
                self.colatitude_label.setText("Dip")
            else:
                self.rake.setEnabled(False)
        elif self.planes.isChecked():
            if self.planetype.currentIndex() == 0:
                self.longitude_label.setText("Dip Direction")
            else:
                self.longitude_label.setText("Direction")
            self.longitude.setEnabled(True)
            self.colatitude_label.setText("Dip")
            self.colatitude.setEnabled(True)
            self.rake.setEnabled(False)
            self.alpha.setEnabled(False)

        self.importer.direction = False
        if self.lines.isChecked():
            if self.linetype.currentIndex() == 0:
                self.importer.data_type = "line"
            else:
                self.importer.data_type = "rake"
                if self.planetype.currentIndex() == 1:
                    self.importer.direction = True
        elif self.planes.isChecked():
            self.importer.data_type = "plane"
            if self.planetype.currentIndex() == 1:
                self.importer.direction = True
        elif self.small_circle.isChecked():
            self.importer.data_type = "smallcircle"
        elif self.circular.isEnabled():
            self.importer.data_type = "circular"

        self.importer.sniff_columns()

        if self.importer.longitude is not None:
            self.longitude.setCurrentIndex(self.importer.longitude)
        if self.importer.colatitude is not None:
            self.colatitude.setCurrentIndex(self.importer.colatitude)
        if self.importer.obliquity is not None:
            self.rake.setCurrentIndex(self.importer.obliquity)
        if self.importer.alpha is not None:
            self.alpha.setCurrentIndex(self.importer.alpha)

    # end region

    # region file change
    def on_browse(self):
        fname, extension = QtWidgets.QFileDialog.getOpenFileName(
            self, "Import Data"
        )
        if not fname:
            return
        self.fname.setText(fname)
        self.on_file_selected()

    def on_file_selected(self):
        fname = self.fname.text()
        if not path.exists(fname):
            return
        name, self.ext = path.splitext(fname)
        self.importer.fname = fname
        self.importer.ext = self.ext
        if self.ext in [".xls", ".xlsx"]:
            self.worksheet.clear()
            self.worksheet.setEnabled(True)
            self.importer.offset = 0
            self.do_skip.setChecked(False)
            self.skip_rows.setValue(0)
            self.header_row.setValue(0)
            self.delimiter.setEnabled(False)
            self.delimiter.setText("")

            book = xlrd.open_workbook(self.fname.text())
            worksheets = book.sheet_names()
            for worksheet in worksheets:
                self.worksheet.addItem(worksheet)

            # TODO: fix this madness!
            self.header = self.importer.header = self.importer.get_header()
            if self.importer.sniff_header():
                self.has_header.setChecked(True)
                self.importer.has_header = True
            else:
                self.has_header.setChecked(False)
                self.importer.has_header = False

            # self.on_worksheet_changed()
        elif self.ext in [".ply", ".shp"]:
            pass
        else:
            self.worksheet.clear()
            self.worksheet.setEnabled(False)
            self.offset = 0
            self.do_skip.setChecked(False)
            self.skip_rows.setValue(0)
            self.header_row.setValue(0)
            self.importer.skip_rows = 0
            self.importer.header_row = 0
            self.delimiter.setEnabled(True)

            self.has_header.setEnabled(True)
            self.header_row.setEnabled(True)

            self.delimiter.setText(repr(self.importer.dialect["delimiter"]))
            self.importer.sniff_encoding()
            self.importer.sample = self.importer.read_sample()
            self.header = self.importer.get_header()
            try:  # TODO: check if should use this or unified
                if self.importer.csv_sniffer.has_header(self.importer.sample):
                    self.has_header.setChecked(True)
                    self.importer.has_header = True
                else:
                    self.has_header.setChecked(False)
                    self.importer.has_header = False
            except csv.Error:
                self.has_header.setChecked(False)
                self.importer.has_header = False
            self.header_row.setValue(0)
        self.on_type_changed()
        self.importer.process_file()
        self.on_header_changed()

    # endregion

    # region data settings
    def on_column_change(self):
        self.importer.longitude = self.longitude.currentIndex()
        self.importer.colatitude = self.colatitude.currentIndex()
        self.importer.obliquity = self.rake.currentIndex()
        self.importer.alpha = self.alpha.currentIndex()

    # endregion

    # def update_importer(self):
    #     pass

    def import_kwargs(self):
        kwargs = {
            "worksheet": self.worksheet.currentText(),
            "keep_input": True,
            "line": self.lines.isChecked() or self.small_circle.isChecked(),
            "dip_direction": self.planetype.currentIndex() == 0,
            "dipdir_column": self.longitude.currentIndex(),
            "dip_column": self.colatitude.currentIndex(),
            "alpha_column": self.alpha.currentIndex(),
            "circular": self.circular.isChecked(),
            "data_headers": self.header
            if self.has_header.isChecked()
            else None,
            "has_header": self.has_header.isChecked(),
            "header_row": self.header_row.value()
            if self.has_header.isChecked()
            else None,
            "skip_rows": self.skip_rows.value()
            if self.do_skip.isChecked()
            else None,
            # "is_geoeas": self.geoeas,
            # "geoeas_offset": self.offset if self.geoeas else None,
            "comment_marker": self.comment_marker.text(),
            "encoding": self.encoding,
        }
        if self.importer.dialect is not None:
            kwargs["dialect_data"] = self.importer.dialect
        return kwargs

    # @import_kwargs.setter
    # def import_kwargs(self, kwargs):
    #     pass

    @property  # TODO: change this whole behaviour
    def data_type(self):
        if self.lines.isChecked():
            return "line_data", "L"
        elif self.small_circle.isChecked():
            return "smallcircle_data", "SC"
        elif self.circular.isChecked():
            return "circular_data", "AZ"
        elif self.planes.isChecked():
            return "plane_data", "P"

    @data_type.setter  # This is madness...
    def data_type(self, data_type):
        if data_type == "line_data":
            self.lines.setChecked(True)
            self.importer.data_type = "line"
        elif data_type == "smallcircle_data":
            self.small_circle.setChecked(True)
            self.importer.data_type = "smallcircle"
        elif data_type == "circular_data":
            self.circular.setChecked(True)
            self.importer.data_type = "circular"
        elif data_type == "plane_data":
            self.planes.setChecked(True)
            self.importer.data_type = "plane"
        self.importer.data_type = data_type

    def get_data(self):
        fname = self.fname.text()
        name, self.ext = path.splitext(fname)
        if self.ext in [".xls", ".xlsx"]:
            book = xlrd.open_workbook(fname)
            sheet = book.sheet_by_name(self.worksheet.currentText())
            header_row = 0
            if self.has_header.isChecked():
                header_row += self.header_row.value() + 1
            if self.do_skip.isChecked():
                header_row += self.skip_rows.value()
            return [
                sheet.row_values(i) for i in range(header_row, sheet.nrows)
            ]
        else:
            f = open(fname, "r", encoding=self.importer.encoding)
            f.seek(self.offset)
            if self.do_skip.isChecked():
                skip_rows = self.skip_rows.value()
            else:
                skip_rows = 0
            if self.has_header.isChecked():
                skip_rows += self.header_row.value() + 1
            reader = csv.reader(
                skip_comments(f, self.comment_marker.text()),
                **self.importer.dialect,
            )
            for i in range(skip_rows):
                next(reader)
            return reader


# region old importer
# TODO: Abstract away the specifics to allow easier integration of new types
# class ImportDialog(QtWidgets.QDialog, import_dialog_Ui_Dialog):
#     direction_names = ["direction", "dipdirection", "dd", "clar"]
#     dip_names = ["dip"]
#     trend_names = ["trend", "azimuth," "direction", "dipdirection"]
#     plunge_names = ["plunge", "dip"]
#     rake_names = ["rake"]
#     alpha_names = ["alpha", "angle", "semiapicalangle", "opening"]
#     sample_size = 1024
#     default_comment = "#"
#     header = None
#     geoeas = None

#     def __init__(
#         self, parent=None, data_type=None, direction=False, fname=None
#     ):
#         super(ImportDialog, self).__init__(parent)
#         self.setupUi(self)

#         self.csv_sniffer = csv.Sniffer()
#         self.comment_marker.setText(self.default_comment)
#         self.sample = None
#         self.ext = None
#         self.fname.editingFinished.connect(self.on_file_changed)
#         self.browse.clicked.connect(self.on_browse)
#         for widget in (
#             self.lines,
#             self.planes,
#             self.small_circle,
#             self.circular,
#         ):
#             widget.toggled.connect(self.on_type_changed)
#         self.planetype.currentIndexChanged.connect(self.on_type_changed)
#         self.linetype.currentIndexChanged.connect(self.on_type_changed)
#         self.delimiter.editingFinished.connect(self.on_delimiter_changed)
#         self.has_header.stateChanged.connect(self.on_header_changed)
#         self.header_row.valueChanged.connect(self.on_header_changed)
#         self.do_skip.stateChanged.connect(self.on_skip_rows)
#         self.skip_rows.valueChanged.connect(self.on_skip_rows)
#         # self.worksheet.valueChanged.connect(self.on_worksheet_changed)
#         self.header = []
#         self.dialect = None
#         self.geoeas = False
#         self.on_type_changed()
#         if data_type:
#             self.data_type = data_type
#         if direction:
#             self.planetype.setCurrentIndex(1)
#         if fname:
#             self.fname.setText(fname)
#             self.on_file_changed()

#     def get_header(self):  # basedata
#         if self.ext not in [".xlsx", ".xls"]:
#             if self.geoeas:
#                 return self.header
#             else:
#                 reader = csv.reader(
#                     skip_comments(
#                         StringIO(self.sample), self.comment_marker.text()
#                     ),
#                     self.dialect,
#                 )
#                 header_row = self.header_row.value()
#                 if self.do_skip.isChecked():
#                     header_row += self.skip_rows.value()
#                 for lineno in range(header_row + 1):
#                     header = next(reader)
#                 return header
#         else:
#             book = xlrd.open_workbook(self.fname.text())
#             sheet = book.sheet_by_name(self.worksheet.currentText())
#             header_row = self.header_row.value()
#             if self.do_skip.isChecked():
#                 header_row += self.skip_rows.value()
#             return sheet.row_values(header_row)

#     def set_headers_on_dialog(self, headers):  # ui
#         for widget in (self.longitude, self.colatitude, self.alpha):
#             widget.clear()
#             for header in headers:
#                 widget.addItem(str(header))

#     def sniff_columns(self):  # basedata
#         n_headers = self.longitude.count()
#         self.longitude.setCurrentIndex(min(n_headers, 0))
#         self.colatitude.setCurrentIndex(min(n_headers, 1))
#         self.alpha.setCurrentIndex(min(n_headers, 2))
#         if (
#             self.lines.isChecked()
#             or self.small_circle.isChecked()
#             or self.circular.isChecked()
#         ):
#             for i, column in enumerate(self.header):
#                 if keep_chars.sub("", column).lower() in self.trend_names:
#                     self.longitude.setCurrentIndex(i)
#                     break
#             for i, column in enumerate(self.header):
#                 if keep_chars.sub("", column).lower() in self.plunge_names:
#                     self.colatitude.setCurrentIndex(i)
#                     break
#             if self.small_circle.isChecked():
#                 for i, column in enumerate(self.header):
#                     if keep_chars.sub("", column).lower() in self.alpha_names:
#                         self.alpha.setCurrentIndex(i)
#                         break
#         elif self.planes.isChecked():
#             for i, column in enumerate(self.header):
#                 if keep_chars.sub("", column).lower() in self.direction_names:
#                     self.longitude.setCurrentIndex(i)
#                     break
#             for i, column in enumerate(self.header):
#                 if keep_chars.sub("", column).lower() in self.dip_names:
#                     self.colatitude.setCurrentIndex(i)
#                     break

#     def sniff_geoEAS(self, f):
#         return False
#         # self.title = f.readline().strip()
#         # try:
#         #     nvars = int(f.readline())
#         # except ValueError:
#         #     self.geoeas = False
#         #     f.seek(0)
#         #     return False
#         # self.header = [f.readline().strip() for i in range(nvars)]
#         # self.offset = f.tell()
#         # self.geoeas = True
#         # return True

#     def sniff_dialect(self):  # basedata
#         try:
#             self.dialect = self.csv_sniffer.sniff(self.sample)
#         except csv.Error:
#             self.dialect = csv.get_dialect("excel")
#         return self.dialect

#     def sniff_header(self, header):  # basedata
#         for field in header:
#             try:
#                 float(str(field))
#                 return False
#             except ValueError:
#                 pass
#         return True

#     def read_sample(self, f):  # basedata
#         read_length = 0
#         sample = []
#         for line in skip_comments(f, self.comment_marker.text()):
#             sample.append(line)
#             read_length += len(sample)
#             if read_length > self.sample_size:
#                 break
#         return "\n".join(sample)

#     def on_file_changed(self):
#         fname = self.fname.text()
#         if not path.exists(fname):
#             return
#         name, self.ext = path.splitext(fname)
#         if self.ext in [".xls", ".xlsx"]:
#             self.worksheet.clear()
#             self.worksheet.setEnabled(True)
#             self.offset = 0
#             self.do_skip.setChecked(False)
#             self.skip_rows.setValue(0)
#             self.header_row.setValue(0)
#             self.delimiter.setEnabled(False)
#             self.delimiter.setText("")

#             book = xlrd.open_workbook(self.fname.text())
#             worksheets = book.sheet_names()
#             for worksheet in worksheets:
#                 self.worksheet.addItem(worksheet)

#             self.header = self.get_header()
#             if self.sniff_header(self.header):
#                 self.has_header.setChecked(True)
#             else:
#                 self.has_header.setChecked(False)

#             self.on_worksheet_changed()
#             self.dialect = None
#         elif self.ext in [".ply", ".shp"]:
#             pass
#         else:
#             self.worksheet.clear()
#             self.worksheet.setEnabled(False)
#             self.offset = 0
#             self.do_skip.setChecked(False)
#             self.skip_rows.setValue(0)
#             self.header_row.setValue(0)
#             self.delimiter.setEnabled(True)

#             # try:
#             with open(fname, "r", encoding="utf-8-sig") as f:
#                 geoeas = self.sniff_geoEAS(f)
#                 if geoeas:
#                     self.has_header.setEnabled(False)
#                     self.header_row.setEnabled(False)
#                 else:
#                     self.has_header.setEnabled(True)
#                     self.header_row.setEnabled(True)
#                 current_pos = f.tell()
#                 self.sample = self.read_sample(f)
#                 f.seek(current_pos)
#                 self.dialect = self.sniff_dialect()
#                 self.delimiter.setText(repr(self.dialect.delimiter))
#                 self.header = self.get_header()
#                 try:
#                     if self.csv_sniffer.has_header(self.sample) or geoeas:
#                         self.has_header.setChecked(True)
#                     else:
#                         self.has_header.setChecked(False)
#                 except csv.Error:
#                     self.has_header.setChecked(False)
#                 self.header_row.setValue(0)
#                 self.on_header_changed()
#                 self.sniff_columns()

#     def on_worksheet_changed(self):
#         self.on_header_changed()

#     def on_delimiter_changed(self):
#         self.dialect.delimiter = (
#             str(self.delimiter.text()).strip("'").strip('"')
#         )
#         self.on_header_changed()

#     def on_skip_rows(self):
#         fname = self.fname.text()
#         name, self.ext = path.splitext(fname)
#         if self.ext in [".xls", ".xlsx"]:
#             pass
#         else:
#             if self.do_skip.isChecked():
#                 skip_rows = self.skip_rows.value()
#             else:
#                 skip_rows = 0
#             with open(fname, "r", encoding="utf-8-sig") as f:
#                 f.seek(self.offset)
#                 for i in range(skip_rows):
#                     f.readline()
#                 self.sample = self.read_sample(f)
#         self.on_header_changed()

#     def on_header_changed(self):
#         self.header = self.get_header()
#         if self.has_header.isChecked():
#             self.set_headers_on_dialog(self.header)
#         else:
#             self.set_headers_on_dialog(list(range(len(self.header))))
#         self.sniff_columns()

#     def on_type_changed(self):
#         if (
#             self.lines.isChecked()
#             or self.small_circle.isChecked()
#             or self.circular.isChecked()
#         ):
#             self.longitude_label.setText("Trend")
#             self.longitude.setEnabled(True)
#             self.colatitude_label.setText("Plunge")
#             self.colatitude.setEnabled(not self.circular.isChecked())
#             self.alpha.setEnabled(self.small_circle.isChecked())
#             self.rake.setEnabled(self.linetype.currentIndex() == 1)
#         elif self.planes.isChecked():
#             if self.planetype.currentIndex() == 0:
#                 self.longitude_label.setText("Dip Direction")
#             else:
#                 self.longitude_label.setText("Direction")
#             self.longitude.setEnabled(True)
#             self.colatitude_label.setText("Dip")
#             self.colatitude.setEnabled(True)
#             self.alpha.setEnabled(False)
#         self.sniff_columns()

#     def on_browse(self):
#         fname, extension = QtWidgets.QFileDialog.getOpenFileName(
#             self, "Import Data"
#         )
#         if not fname:
#             return
#         self.fname.setText(fname)
#         self.on_file_changed()

#     @property
#     def import_kwargs(self):
#         kwargs = {
#             "worksheet": self.worksheet.currentText(),
#             "keep_input": True,
#             "line": self.lines.isChecked() or self.small_circle.isChecked(),
#             "dip_direction": self.planetype.currentIndex() == 0,
#             "dipdir_column": self.longitude.currentIndex(),
#             "dip_column": self.colatitude.currentIndex(),
#             "alpha_column": self.alpha.currentIndex(),
#             "circular": self.circular.isChecked(),
#             "data_headers": self.header
#             if self.has_header.isChecked()
#             else None,
#             "has_header": self.has_header.isChecked(),
#             "header_row": self.header_row.value()
#             if self.has_header.isChecked()
#             else None,
#             "skip_rows": self.skip_rows.value()
#             if self.do_skip.isChecked()
#             else None,
#             "is_geoeas": self.geoeas,
#             "geoeas_offset": self.offset if self.geoeas else None,
#             "comment_marker": self.comment_marker.text(),
#         }
#         if self.dialect is not None:
#             kwargs["dialect_data"] = {
#                 "delimiter": self.dialect.delimiter,
#                 "doublequote": self.dialect.doublequote,
#                 "escapechar": self.dialect.escapechar,
#                 "lineterminator": self.dialect.lineterminator,
#                 "quotechar": self.dialect.quotechar,
#                 "quoting": self.dialect.quoting,
#                 "skipinitialspace": self.dialect.skipinitialspace,
#             }
#         return kwargs

#     @import_kwargs.setter
#     def import_kwargs(self, kwargs):
#         pass

#     @property
#     def data_type(self):
#         if self.lines.isChecked():
#             return "line_data", "L"
#         elif self.small_circle.isChecked():
#             return "smallcircle_data", "SC"
#         elif self.circular.isChecked():
#             return "circular_data", "AZ"
#         elif self.planes.isChecked():
#             return "plane_data", "P"

#     @data_type.setter
#     def data_type(self, data_type):
#         if data_type == "line_data":
#             self.lines.setChecked(True)
#         elif data_type == "smallcircle_data":
#             self.small_circle.setChecked(True)
#         elif data_type == "circular_data":
#             self.circular.setChecked(True)
#         elif data_type == "plane_data":
#             self.planes.setChecked(True)

#     def get_data(self):
#         fname = self.fname.text()
#         name, self.ext = path.splitext(fname)
#         if self.ext in [".xls", ".xlsx"]:
#             book = xlrd.open_workbook(fname)
#             sheet = book.sheet_by_name(self.worksheet.currentText())
#             header_row = 0
#             if self.has_header.isChecked():
#                 header_row += self.header_row.value() + 1
#             if self.do_skip.isChecked():
#                 header_row += self.skip_rows.value()
#             return [
#                 sheet.row_values(i) for i in range(header_row, sheet.nrows)
#             ]
#         else:
#             f = open(fname, "r", encoding="utf-8-sig")
#             f.seek(self.offset)
#             if self.do_skip.isChecked():
#                 skip_rows = self.skip_rows.value()
#             else:
#                 skip_rows = 0
#             if self.has_header.isChecked():
#                 skip_rows += self.header_row.value() + 1
#             reader = csv.reader(
#                 skip_comments(f, self.comment_marker.text()), self.dialect
#             )
#             for i in range(skip_rows):
#                 next(reader)
#             return reader
# endregion


def get_data(fname, kwargs):
    name, ext = path.splitext(fname)
    if ext in [".xls", ".xlsx"]:
        book = xlrd.open_workbook(fname)
        sheet = book.sheet_by_name(kwargs["worksheet"])
        header_row = (
            0 if kwargs["header_row"] is None else kwargs["header_row"] + 1
        )
        header_row += 0 if kwargs["skip_rows"] is None else kwargs["skip_rows"]
        return skip_comments_xlsx(
            [sheet.row_values(i) for i in range(header_row, sheet.nrows)],
            kwargs.get("comment_marker", "#"),
        )
    else:
        encoding = kwargs.get("encoding", "utf-8-sig")
        f = open(fname, "r", encoding=encoding)
        if kwargs.get("is_geoeas", False):
            f.seek(kwargs["geoeas_offset"])
        skip_rows = (
            0 if kwargs["header_row"] is None else kwargs["header_row"] + 1
        )
        skip_rows += 0 if kwargs["skip_rows"] is None else kwargs["skip_rows"]
        dialect_data = {}
        for key, item in list(kwargs["dialect_data"].items()):
            dialect_data[key] = str(item) if isinstance(item, str) else item
        reader = csv.reader(
            skip_comments(f, kwargs.get("comment_marker", "#")), **dialect_data
        )
        for i in range(skip_rows):  # TODO: check if this should be before
            next(reader)
        return reader


def skip_comments(iterable, comment="#"):  # TODO: skip comments in xlsx
    for line in iterable:
        if line.startswith(comment):
            continue
        yield line


def skip_comments_xlsx(iterable, comment="#"):
    for line in iterable:
        if len(line) > 0 and str(line[0]).startswith(comment):
            continue
        yield line


split_attitude_re = re.compile("[^NESW\.\+\-0-9]+", flags=re.IGNORECASE)


def split_attitude(data):
    return split_attitude_re.split(data)
