#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
import PyPDF2

# --- Pattern Stitcher ---

def addright(page, right_page, tx=0):
    """Adds page (PageObject) on the right side, tx is an addtional offset"""
    page.mergeTranslatedPage(right_page, page.mediaBox[2] + tx, 0, expand=True)
    return page


def main():
    filename = 'bin/test/BM1004_102Schnitt.pdf'
    print('## Pattern Stitcher ##')
    pdf = PyPDF2.PdfFileReader(filename)
    print(pdf.documentInfo)
    print("Number of Pages: %1.2i" % pdf.getNumPages())

    a = pdf.getPage(5)
    b = pdf.getPage(6)
    print(a.mediaBox)
    a.mergeTranslatedPage(b, a.mediaBox[2] - 50, 0, expand=True)
    print(a.mediaBox)

    output = PyPDF2.PdfFileWriter()
    output.addPage(a)
    out_file = open('bin/test/output.pdf', 'wb')
    output.write(out_file)
    out_file.close()
    return

if __name__ == "__main__":
    main()
