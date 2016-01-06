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
    with open(sys.argv[1], 'rb') as input:
        pdf = PyPDF2.PdfFileReader(input)
        print("Number of Pages: %1.2i" % pdf.getNumPages())

        first_page = True
        with open(sys.argv[2], 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                for page in row:
                    if first_page is True:
                        output = pdf.getPage(int(page))
                        first_page = False
                    else:
                        output = addright(output, pdf.getPage(int(page)))
                rows.append(output)
            output = rows[0]
            for row in rows:
                output.mergeTranslatedPage(row, 0, output.mediaBox[3], expand=True)

        with open(sys.argv[3], 'wb') as out_file:
            pdf_out = PyPDF2.PdfFileWriter()
            pdf_out.addPage(output)
            pdf_out.write(out_file)
    return

if __name__ == "__main__":
    main()
