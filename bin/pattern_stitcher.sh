#!/bin/bash
# convert single pages to montage
filename=”BM1234_123Schnitt.pdf”

# save single pages
pdftk A=$filename cat A2 output 1a.pdf
pdftk A=$filename cat A3 output 1b.pdf
pdftk A=$filename cat A4 output 1c.pdf
pdftk A=$filename cat A5 output 1d.pdf
pdftk A=$filename cat A6 output 1e.pdf
pdftk A=$filename cat A7 output 1f.pdf
pdftk A=$filename cat A8 output 1g.pdf

pdftk A=$filename cat A9 output 3a.pdf
pdftk A=$filename cat A10 output 3b.pdf
pdftk A=$filename cat A11 output 3c.pdf
pdftk A=$filename cat A12 output 3d.pdf
pdftk A=$filename cat A13 output 3e.pdf
pdftk A=$filename cat A14 output 3f.pdf
pdftk A=$filename cat A15 output 3g.pdf

pdftk A=$filename cat A16 output 5a.pdf
pdftk A=$filename cat A17 output 5b.pdf
pdftk A=$filename cat A18 output 5c.pdf
pdftk A=$filename cat A19 output 5d.pdf
pdftk A=$filename cat A20 output 5e.pdf
pdftk A=$filename cat A21 output 5f.pdf
pdftk A=$filename cat A22 output 5g.pdf

# make a “montage” of single pages
montage 5a.pdf 5b.pdf 5c.pdf 5d.pdf 5e.pdf 5f.pdf 5g.pdf \
3a.pdf 3b.pdf 3c.pdf 3d.pdf 3e.pdf 3f.pdf 3g.pdf \
1a.pdf 1b.pdf 1c.pdf 1d.pdf 1e.pdf 1f.pdf 1g.pdf -geometry +0+0 -tile 7×3 output.pdf
