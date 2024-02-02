import os
import time
from pathlib import Path
from PyPDF2 import PdfMerger
import pdfkit as pdf

### assisting functions 
def string_number(number):
    temp = '000000' + str(number)
    return temp[-4:]


### def main functions

def make_temp_pdf_files(url_ref, pages_count):
    url_ref = url_ref[:-10]
    suffix = '.xhtml'
    
    pdf_output_dir = Path(__file__).parent / 'Temp files'
    pdf_output_dir.mkdir(parents=True, exist_ok=True)


    for i in range(1, pages_count+1):
        mybook_number = string_number(i)
        temp_url = url_ref + mybook_number + suffix
        pdf.from_url(temp_url, str(pdf_output_dir) + '/' + 'mybook' + str(i) + '.pdf')


def merge_pdf_files(pages_count, doc_title):
    pdfs = ['Temp files/mybook' + str(i) + '.pdf' for i in range(1, pages_count+1)]

    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(doc_title + '.pdf')
    merger.close()


def remove_temp_pdf_files(pages_count):
    for i in range(1, pages_count+1):
        os.remove('Temp files/mybook' + str(i) + '.pdf')
    os.rmdir('Temp files')  

doc_title = input('Введите название готового файла: ')
url_ref = input('Вставьте ссылку на первую страницу: ')
pages_count = int(input('Введите количество страниц: '))

start_time = time.time()

make_temp_pdf_files(url_ref, pages_count)
merge_pdf_files(pages_count, doc_title)
remove_temp_pdf_files(pages_count)

print("--- %s seconds ---" % (time.time() - start_time))

print('Документ готов!')
input("Enter any key to exit ")
