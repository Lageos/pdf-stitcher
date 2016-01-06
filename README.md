# PDF Stitcher

Different means to stitch sewing patterns (or any pdf file) delivered in single sheets to a whole plan (file).

## Prerequisites
* Python (tested with python 2.7.10 Anaconda 64-bit)
* PyPDF2 (tested version 1.25.1, https://pypi.python.org/pypi/PyPDF2/1.25.1 )
        install with `pip install pypdf2`

## Usage
`python pdf_stitcher.py input_file.pdf positions.csv output.pdf`

With positions.csv decribing the placement of the pages (specified with the page
number):
![pdf_stitcher flow](https://smidgeonpigeon.files.wordpress.com/2016/01/pdf_stitcher_flow1.png "pdf_stitcher flow")

The easiest way to create this file is with a simple text editor.

Stitching is done with no spacing between pages.
