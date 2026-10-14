"""Radials of a uniform current (u, v) = (10, 5) cm/s seen from 12 look angles; OI recovers it."""
import numpy as np
from oimap4rs import lonlat2km, tuvOIg

rng = np.random.default_rng(0)
lon0, lat0 = -117.25, 32.55
n = 12
ang = np.deg2rad(np.linspace(0, 150, n))
lon = lon0 + rng.normal(0, 0.01, n)
lat = lat0 + rng.normal(0, 0.01, n)
dx, dy = lonlat2km(lon0, lat0, lon, lat)
rs = 10.0 * np.cos(ang) + 5.0 * np.sin(ang)

u, v, cuu, cvv, cuv = tuvOIg(lon, lat, dx, dy, rs, ang, 2.0, 2.0, 400.0, 40.0)
print(f"u = {u:.2f}, v = {v:.2f} cm/s (true 10, 5);  normalized uncertainty uu, vv, uv = {cuu:.2f}, {cvv:.2f}, {cuv:.3f}")
