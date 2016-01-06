#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, with_statement
import PyPDF2
import csv
import sys

# --- Pattern Stitcher ---

def addright(page, right_page, tx=0):
    """Adds page (PageObject) on the right side, tx is an addtional offset"""
    page.mergeTranslatedPage(right_page, page.mediaBox[2] + tx, 0, expand=True)
    return page


def main():
    print('## Pattern Stitcher ##')
    with open(sys.argv[1], 'r') as input:
        pdf = PyPDF2.PdfFileReader(input)
        print("Number of Pages: %1.2i" % pdf.getNumPages())

        output = PyPDF2.pdf.PageObject()
        with open(sys.argv[2], 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                for page in row:
                    output = addright(output, pdf.getPage(int(page)))

        with open(sys.argv[3], 'wb') as out_file:
            pdf_out = PyPDF2.PdfFileWriter()
            pdf_out.addPage(output)
            pdf_out.write(out_file)
    return

if __name__ == "__main__":
    main()
