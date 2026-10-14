"""Kim 2008 / rad2uvoiunif: OI of radials onto a vector at one grid point.

Exponential covariance, isotropic if sx == sy. Matches
/pao1/scripts/myfunctions/rad2uvoiunif.m (June 2006).
"""
from __future__ import annotations

import numpy as np


def lonlat2km(lon1, lat1, lon2, lat2):
    """East/north km from (lon1, lat1) to (lon2, lat2). Degrees."""
    lon1 = np.asarray(lon1, dtype=float)
    lat1 = np.asarray(lat1, dtype=float)
    lon2 = np.asarray(lon2, dtype=float)
    lat2 = np.asarray(lat2, dtype=float)
    latm = 0.5 * (lat1 + lat2)
    de = (lon2 - lon1) * 111.32 * np.cos(np.deg2rad(latm))
    dn = (lat2 - lat1) * 111.32
    return de, dn


def tuvOIg(x, y, dx, dy, rs, ang, sx, sy, P, R):
    """Combine radials at one grid point.

    x, y : observation lon, lat (deg)
    dx, dy : east/north km from grid to each observation
    rs : radial velocity
    ang : look angle (rad), same convention as Kim: u~cos, v~sin
    sx, sy : decorrelation lengths (km)
    P : signal variance
    R : observation noise variance (scalar, applied as R I)
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    dx = np.asarray(dx, dtype=float)
    dy = np.asarray(dy, dtype=float)
    rs = np.asarray(rs, dtype=float)
    ang = np.asarray(ang, dtype=float)
    n = rs.size
    if n < 2:
        return np.nan, np.nan, np.nan, np.nan, np.nan
    f = np.sqrt(dx * dx / sx**2 + dy * dy / sy**2)
    cmd = np.exp(-f)
    cmd = np.column_stack((cmd * np.cos(ang), cmd * np.sin(ang)))
    lon1, lon2 = np.meshgrid(x, x)
    lat1, lat2 = np.meshgrid(y, y)
    ang1, ang2 = np.meshgrid(ang, ang)
    drx, dry = lonlat2km(lon1, lat1, lon2, lat2)
    g = np.sqrt(drx * drx / sx**2 + dry * dry / sy**2)
    w = np.exp(-g) * P
    cdd = w * (np.cos(ang1) * np.cos(ang2) + np.sin(ang1) * np.sin(ang2))
    P_ = P * np.eye(2)
    try:
        icdd = np.linalg.solve(cdd + R * np.eye(n), cmd)
    except np.linalg.LinAlgError:
        return np.nan, np.nan, np.nan, np.nan, np.nan
    gain = P_ @ icdd.T
    uv = gain @ rs
    e = np.linalg.inv(P_) @ (P_ - gain @ cmd @ P_)
    return float(uv[0]), float(uv[1]), float(e[0, 0]), float(e[1, 1]), float(e[0, 1])
