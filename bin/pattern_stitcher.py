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
    tx = 0
    ty = 0
    with open(sys.argv[1], 'rb') as input:
        pdf = PyPDF2.PdfFileReader(input)
        print("Number of Pages: %1.2i" % pdf.getNumPages())

        first_page = True
        with open(sys.argv[2], 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                for page in row:
                    print("Reading page %1.2i" % int(page))
                    if first_page is True:
                        output = pdf.getPage(int(page) - 1)
                        first_page = False
                    else:
                        output = addright(output, pdf.getPage(int(page) - 1), tx)
                rows.append(output)
                first_page = True

            print("Stitching lines of pages ...")
            first_line = True
            for row in reversed(rows):
                print('Row: ', row.mediaBox)
                if first_line is True:
                    output = rows[-1]
                    print('Output: ', output.mediaBox)
                    first_line = False
                else:
                    print('Output: ', output.mediaBox)
                    output.mergeTranslatedPage(row, 0, output.mediaBox[3] + ty, expand=True)

        print("Saving new file...")
        with open(sys.argv[3], 'wb') as out_file:
            pdf_out = PyPDF2.PdfFileWriter()
            pdf_out.addPage(output)
            pdf_out.write(out_file)
    print("Finished.")
    return

if __name__ == "__main__":
    main()
