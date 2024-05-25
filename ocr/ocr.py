import easyocr

from ocr.documents.doc_01207 import doc_01207
from ocr.documents.doc_01707 import doc_01707
from ocr.documents.doc_02016 import doc_02016
from ocr.documents.doc_04021 import doc_04021
from ocr.documents.doc_09015 import doc_09015
from ocr.documents.doc_09029 import doc_09029

reader = easyocr.Reader(['en'], gpu=True)
reader_english_russian = easyocr.Reader(['en', 'ru'], gpu=True)
reader_chinese = easyocr.Reader(['en', 'ch_sim'], gpu=True)


def read_document(box_images, pdf_file):
    documents = []

    for box in box_images:
        if box == '09029':
            documents.append(doc_09029(box_images[box], pdf_file.file, reader_english_russian))

        elif box == '04021':
            documents.append(doc_04021(box_images[box], pdf_file.file, reader_english_russian))

        elif box == '02016':
            documents.append(doc_02016(box_images[box], pdf_file.file, reader))

        elif box == '01207':
            documents.append(doc_01207(box_images[box], pdf_file.file, reader))

        elif box == '01707':
            documents.append(doc_01707(box_images[box], pdf_file.file, reader))

        elif box == '09015':
            documents.append(doc_09015(box_images[box], pdf_file.file, reader_chinese))

    return documents
