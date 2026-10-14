# GitHub + Zenodo (DOI) — oimap4rs

GitHub root: `/pao1/library/repository/oimap4rs` (master copy; the `meetings` folder holds only a share copy).
Same procedure as `papers/ksstats/deposit/ZENODO.md`.

## 0. GitHub repo `syongkim/oimap4rs`

```bash
cd /pao1/library/repository/oimap4rs
git remote add origin git@github.com:syongkim/oimap4rs.git
git push -u origin main
```

(Create the empty repository `oimap4rs` on GitHub first, public, without README or license.)

## 1. Zenodo

GitHub → Settings → Applications → Zenodo → Repository access → add `oimap4rs`; Zenodo → GitHub → sync.
Make a release with tag `v0.1.0` on GitHub; Zenodo issues the version DOI and the concept DOI.
Manual zip if the GitHub page times out:

```bash
git archive --format=zip --prefix=oimap4rs-0.1.0/ -o /tmp/oimap4rs-0.1.0.zip HEAD
```

zenodo.org → Upload → New upload → attach the zip, MIT, related identifier
`https://github.com/syongkim/oimap4rs`, publish.

## 2. After the DOI exists

Put `doi:` and `repository-code:` in `CITATION.cff`, commit, and use the DOI link for the QR code on the
last slide of `ORCA2026_SYK.pptx`.

## 3. What not to upload

`__pycache__/`, `*.egg-info/`, any data files.
