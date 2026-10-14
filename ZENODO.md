# GitHub + Zenodo (DOI) — oimaps4rs

GitHub root: `/pao1/library/repository/oimaps4rs` (master copy; the `meetings` folder holds only a share copy).
Same procedure as `papers/ksstats/deposit/ZENODO.md`.

## 0. GitHub repo `syongkim/oimaps4rs`

```bash
cd /pao1/library/repository/oimaps4rs
git remote add origin git@github.com:syongkim/oimaps4rs.git
git push -u origin main
```

(Create the empty repository `oimaps4rs` on GitHub first, public, without README or license.)

## 1. Zenodo

GitHub → Settings → Applications → Zenodo → Repository access → add `oimaps4rs`; Zenodo → GitHub → sync.
Make a release with tag `v0.1.0` on GitHub; Zenodo issues the version DOI and the concept DOI.
Manual zip if the GitHub page times out:

```bash
git archive --format=zip --prefix=oimaps4rs-0.1.0/ -o /tmp/oimaps4rs-0.1.0.zip HEAD
```

zenodo.org → Upload → New upload → attach the zip, MIT, related identifier
`https://github.com/syongkim/oimaps4rs`, publish.

## 2. After the DOI exists

Put `doi:` and `repository-code:` in `CITATION.cff`, commit, and use the DOI link for the QR code on the
last slide of `ORCA2026_SYK.pptx`.

## 3. What not to upload

`__pycache__/`, `*.egg-info/`, any data files.
