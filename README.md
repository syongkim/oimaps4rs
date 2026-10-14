# oimaps4rs

Optimal interpolation (OI) of HF-radar radial velocities onto a vector current at one grid point.
Python version of the OI of Kim, Terrill, and Cornuelle (2008), which replaces the constant-vector
(UWLS) assumption within a search radius by an exponential spatial correlation.

## Install

    pip install .          # requires Python >= 3.9 and NumPy

## Use

```python
from oimaps4rs import lonlat2km, tuvOIg

# km (east, north) from the grid point to each radial cell
dx, dy = lonlat2km(lon0, lat0, lon, lat)

u, v, cuu, cvv, cuv = tuvOIg(lon, lat, dx, dy, rs, ang,
                             sx=2, sy=2, P=400, R=40)
```

| Argument | Meaning |
|---|---|
| `lon, lat` | longitude, latitude (deg) of each radial cell inside the search radius |
| `dx, dy` | east, north distance (km) from the grid point to each radial cell |
| `rs` | radial velocity (cm/s); positive away from the radar |
| `ang` | look angle (rad), u ~ cos, v ~ sin |
| `sx, sy` | decorrelation lengths (km); isotropic if `sx == sy` |
| `P` | signal variance (cm^2/s^2) |
| `R` | observational error variance (cm^2/s^2), applied as `R I` |

Returns `u, v` and the normalized uncertainty `cuu, cvv, cuv` (a posteriori error covariance
normalized by the signal variance). Returns `NaN` if fewer than two radials are given or the
covariance matrix is singular.

Typical values (Kim et al., 2008): search radius 5 km, `sx = sy = 2` km, `P = 400`, `R = 40`.

## Example

    python examples/uniform_vector.py

## Cite

Kim, S. Y., E. J. Terrill, and B. D. Cornuelle (2008), Mapping surface currents from HF radar radial
velocity measurements using optimal interpolation, *J. Geophys. Res.*, 113, C10023,
doi:10.1029/2007JC004244. See also `CITATION.cff`.

## License

MIT (see `LICENSE`, `NOTICE`).
