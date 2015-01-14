#!/usr/bin/python
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

from PyPDF2 import PdfFileReader

# FILENAME = '/home/markmuetz/Dropbox/PhDs/Oxford/SkillVsStatistics/ctr148.pdf'
# FILENAME = '/home/markmuetz/Dropbox/PhDs/Oxford/SkillVsStatistics/PNAS-2011-Majda-12599-604.pdf'
FILENAME = '/home/markmuetz/Dropbox/PhDs/Oxford/SkillVsStatistics/Model_Fidelity.pdf'

def get_doc():
    fp = open(FILENAME, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    #parser.set_document(doc)
    #doc.set_parser(parser)
    # doc.initialize()
    return doc

def get_doc_pypdf2():
    fp = open(FILENAME, 'rb')
    pdf_toread = PdfFileReader(fp)
    return pdf_toread

if __name__ == "__main__":
    doc = get_doc()
    print doc.info  # The "Info" metadata
    doc2 = get_doc_pypdf2()
    print(str(doc2.getDocumentInfo()))
