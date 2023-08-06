import math
from math import pi, sin, cos, acos, atan2, degrees, radians, sqrt

import numpy as np

import auttitude as au


# https://en.wikipedia.org/wiki/Earth_radius#Mean_radius
earth_radius = 6371008.8


# http://www.movable-type.co.uk/scripts/latlong.html
def haversine(long1, long2, lat1, lat2, R=earth_radius):
    phi1, phi2 = radians(lat1), radians(lat2)
    lambda1, lambda2 = radians(long1), radians(long2)
    delta_phi = phi1 - phi2
    delta_lambda = lambda1 - lambda2
    a = (
        sin(delta_phi / 2.0) ** 2
        + cos(phi1) * cos(phi2) * sin(delta_lambda / 2.0) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


# http://www.movable-type.co.uk/scripts/latlong.html
def bearing(long1, long2, lat1, lat2):
    phi1, phi2 = radians(lat1), radians(lat2)
    lambda1, lambda2 = radians(long1), radians(long2)
    y = sin(lambda2 - lambda1) * cos(phi2)
    x = cos(phi1) * sin(phi2) - sin(phi1) * cos(phi2) * cos(lambda2 - lambda1)
    return degrees(atan2(y, x)) % 360.0


# http://stackoverflow.com/a/22659261/1457481
def in_interval(from_, to_, theta):
    from_, to_ = from_ % 360.0, to_ % 360.0
    return (from_ > to_ and (theta > from_ or theta < to_)) or (
        from_ < to_ and (theta <= to_ and theta >= from_)
    )


def dcos(atti):
    dd, d = np.transpose(atti)
    return np.array((sin(d) * sin(dd), sin(d) * cos(dd), cos(d)))


def dcos_lines(atti):
    tr, pl = np.transpose(atti)
    return np.array((cos(pl) * sin(tr), cos(pl) * cos(tr), -sin(pl)))


def sphere(x, y, z):
    """Calculates the attitude of poles direction cossines."""
    sign_z = np.copysign(1, z)
    return np.array(
        (
            np.degrees(np.arctan2(sign_z * x, sign_z * y)) % 360,
            np.degrees(np.arccos(np.abs(z))),
        )
    ).T


def normal_versor(a, b):
    c = np.cross(a, b)
    return c / np.linalg.norm(c)


def direction_versor(a):
    if a[2] == 1.0:
        return np.array((0.0, 1.0, 0.0))
    else:
        d = np.cross((0.0, 0.0, 1.0), a)
        return d / np.linalg.norm(d)


def angle(A, B):
    a, b = A / np.linalg.norm(A), B / np.linalg.norm(B)
    return math.atan2(np.linalg.norm(np.cross(a, b)), np.inner(a, b))


def angle_acos(A, B):
    a, b = A / np.linalg.norm(A), B / np.linalg.norm(B)
    return math.acos(np.clip(np.dot(a, b), -1.0, 1.0))


def normalized_cross(a, b):
    c = np.cross(a, b)
    return c / np.linalg.norm(c)[:, None]


def dip_versor(a):
    d = np.cross(direction_versor(a), a)
    return d / np.linalg.norm(d)


def great_circle_arc(a, b, r=radians(1.0)):
    dot = np.dot(a, b)
    theta = acos(dot)
    b_ = b - dot * a
    b_ = b_ / np.linalg.norm(b_)
    # c = np.cross(a, b_)
    theta_range = np.arange(0, theta, radians(r))
    sin_range = np.sin(theta_range)
    cos_range = np.cos(theta_range)
    return (a * cos_range[:, None] + b_ * sin_range[:, None]).T


def great_circle_simple(dcos, range=2 * pi, r=radians(1.0)):
    theta_range = np.arange(0, range, r)
    sin_range = np.sin(theta_range)
    cos_range = np.cos(theta_range)
    dir_v = direction_versor(dcos)
    dip_v = dip_versor(dcos)
    return (np.outer(dir_v, cos_range) + np.outer(dip_v, sin_range)).T


def great_circle(dcos, n=360):
    theta_range = np.linspace(0, 2 * pi, n)
    sin_range = np.sin(theta_range)
    cos_range = np.cos(theta_range)
    dir_v = direction_versor(dcos)
    dip_v = dip_versor(dcos)
    return (np.outer(dir_v, cos_range) + np.outer(dip_v, sin_range)).T


def small_circle(axis, alpha, n=360):
    k = np.linspace(0.0, 2 * pi, n)
    dir = direction_versor(axis)
    dip = dip_versor(axis)
    gc = dip[:, None] * np.sin(k) + dir[:, None] * np.cos(k)
    sc = gc * sin(alpha) + axis[:, None] * cos(alpha)
    return sc.T, -sc.T


def net_grid(gcspacing=10.0, scspacing=10.0, n=360, clean_caps=True):
    theta = np.linspace(0.0, 2 * pi, n)
    gcspacing, scspacing = radians(gcspacing), radians(scspacing)
    theta_gc = (
        np.linspace(0.0 + scspacing, pi - scspacing, n)
        if clean_caps
        else np.linspace(0.0, pi, n)
    )
    gc_range = np.arange(0.0, pi + gcspacing, gcspacing)
    sc_range = np.arange(0.0, pi + scspacing, scspacing)
    i, j, k = np.eye(3)
    ik_circle = i[:, None] * np.sin(theta) + k[:, None] * np.cos(theta)
    great_circles = [
        (
            np.array((cos(alpha), 0.0, -sin(alpha)))[:, None]
            * np.sin(theta_gc)
            + j[:, None] * np.cos(theta_gc)
        ).T
        for alpha in gc_range
    ] + [
        (
            np.array((cos(alpha), 0.0, -sin(alpha)))[:, None]
            * np.sin(theta_gc)
            + j[:, None] * np.cos(theta_gc)
        ).T
        for alpha in -gc_range
    ]
    small_circles = [
        (ik_circle * sin(alpha) + j[:, None] * cos(alpha)).T
        for alpha in sc_range
    ]
    if clean_caps:
        theta_gc = np.linspace(-scspacing, scspacing, n)
        great_circles += [
            (
                np.array((cos(alpha), 0.0, -sin(alpha)))[:, None]
                * np.sin(theta_gc)
                + j[:, None] * np.cos(theta_gc)
            ).T
            for alpha in (0, pi / 2.0)
        ]
        theta_gc = np.linspace(pi - scspacing, pi + scspacing, n)
        great_circles += [
            (
                np.array((cos(alpha), 0.0, -sin(alpha)))[:, None]
                * np.sin(theta_gc)
                + j[:, None] * np.cos(theta_gc)
            ).T
            for alpha in (0, pi / 2.0)
        ]
    return great_circles, small_circles


# probably not needed
def clip_lines(data, clip_radius=1.1):
    radii = np.linalg.norm(data, axis=1)
    radii[np.isinf(radii)] = 100.0
    radii[np.isnan(radii)] = 100.0
    inside = radii < clip_radius
    results = []
    current = []
    for i, is_inside in enumerate(inside):
        if is_inside:
            current.append(data[i])
        elif current:
            results.append(current)
            current = []
    if current:
        results.append(current)
    return results


def au_clip_lines(data, z_tol=0.1):
    """segment point pairs between inside and outside of primitive, for
    avoiding spurious lines when plotting circles."""
    z = np.transpose(data)[2]
    inside = z < z_tol
    results = []
    current = []
    for i, is_inside in enumerate(inside):
        if is_inside:
            current.append(data[i])
        elif current:
            results.append(current)
            current = []
    if current:
        results.append(current)
    return results


def au_join_segments(segments, c_tol=radians(1.0)):
    """segment point pairs between inside and outside of primitive, for
    avoiding spurious lines when plotting circles."""
    all_joined = False
    while not all_joined and len(segments) > 1:
        all_joined = True
        segment = segments.pop(0)
        if abs(angle_acos(segment[-1], segments[0][0])) < c_tol:
            segment.extend(segments.pop(0))
            all_joined = False
        elif abs(angle_acos(segment[0], segments[0][-1])) < c_tol:
            segment_b = segments.pop(0)
            segment_b.extend(segment)
            segment = segment_b
            all_joined = False
        elif abs(angle_acos(segment[-1], segments[0][-1])) < c_tol:
            segment.extend(reversed(segments.pop(0)))
            all_joined = False
        elif abs(angle_acos(segment[0], segments[0][0])) < c_tol:
            segment_b = segments.pop(0)
            segment_b.extend(reversed(segment))
            segment = segment_b
            all_joined = False
        segments.append(segment)
    return segments


def au_close_polygon(projected_polygon):
    first = projected_polygon[0]
    last = projected_polygon[-1]
    mid = (first + last) / 2
    mid = mid / np.linalg.norm(mid)
    if np.dot(first, last) == 0.0:
        mid = np.array([first[1], -first[0]])
    if np.linalg.norm(first) > 1.0 and np.linalg.norm(last) > 1.0:
        return np.vstack([projected_polygon, [2 * last, 3 * mid, 2 * first]])
    return projected_polygon


def extents_from_center(cx, cy, ex, ey, nx, ny, w, h):
    dx = cx - ex
    dy = cy - ny
    left = -1.0 - ex / dx
    right = (w - cx) / dx
    top = 1.0 + ny / dy
    bottom = -(h - cy) / dy
    return (left, right, bottom, top)


# TODO: send this upstream to autti
def resolve_sense(plane, line, sense):
    if plane[-1] > 0:
        plane = -plane
    sense = str(sense).lower()[0]
    if sense in ("u", "f", "0", "5", "?"):
        return line, False
    elif sense in ("n", "2", "-"):
        return line, True
    elif sense in ("i", "1", "+"):
        return -line, True

    line_sense = plane.direction_vector.dot(line)
    if sense in ("d", "3"):
        if line_sense > 0:
            return line, True
        else:
            return -line, True
    elif sense in ("s", "4"):
        if line_sense < 0:
            return line, True
        else:
            return -line, True
    else:  # is this right?
        return line, True
