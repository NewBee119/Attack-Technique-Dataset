#coding:utf-8
'''
Description:
1. preprocesses the file in "references" folder and
2. detectes the file type using PyPDF2 library and convert pdf into html，
    and resave the new file into "reference_processed" folder
3. extract the main context related html tag from the html file，
    and resave the new file into "reference_processed" folder
'''
import PyPDF2
from htmlcontent import HTML_Extractor
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO


def is_ascii(s):
    return all(ord(c) < 128 for c in s)
def clean_string(s):
    s = [e for e in s if is_ascii(e)]
    s = ''.join(s)
    return s
def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    # device = TextConverter(manager, retstr, laparams=layout)
    layoutmode = 'normal'
    imagewriter = None
    device = HTMLConverter(manager, retstr,
                           layoutmode=layoutmode, laparams=layout,
                           imagewriter=imagewriter)

    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    filepath.close()
    device.close()
    retstr.close()
    # print text
    from BeautifulSoup import BeautifulSoup
    parsed_html = BeautifulSoup(text)
    return clean_string(parsed_html.text)


if __name__ == "__main__":
    # filelist = ['a','b']
    filelist = os.listdir('./references')
    for filename in filelist:
        file = open('./references/'+filename, 'rb')
        try:
            #detect if html file
            PyPDF2.PdfFileReader(file)
            try:
                file.close()
                # pdf2html(filename, './reference_processed/pdf/'+filename)
                text = pdf_to_text('./references/'+filename)
                open('./reference_processed/pdf/'+filename,'wb').write(text)
            except:
                open('error_processed.txt','a').write(filename+'\n')
                continue
        except:
            #main context related tag extracted
            file.close()
            html = open('./references/'+filename).read()
            ext = HTML_Extractor()
            try:
                content = ext.get_content(html, just_content=True, with_tag=True)
            except:
                open('error_processed.txt', 'a').write(filename+'\n')
            open('./reference_processed/html/'+filename, 'w').write(content)
            # print "html"
