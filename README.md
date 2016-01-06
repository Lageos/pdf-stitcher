# Pattern Stitcher

Different means to stitch sewing patterns delivered in single sheets to a whole plan.

## Prerequisites
* python
* PyPDF2 with 
        `pip install pypdf2`
        ( https://pypi.python.org/pypi/PyPDF2/1.25.1 )


## Usage
`python pattern_stitcher.py input_file.pdf positions.csv output.pdf [tx]`

With positions.csv decribing the placement of the pages on the final output:
```2, 3, 4, 5
6, 7, 8, 9
10, 11, 12, 13```

Each line should have the same amount of pages (specified with the page
number).




