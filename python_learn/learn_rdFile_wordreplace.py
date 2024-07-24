import os
import glob
import fitz         # PyMuPDF for PDFs
from PIL import Image   # For image file processing
from docx import Document   # For .docx file processing
import pytesseract  # For OCR

def count_linepage_docxfile(file_path):
    """Count the number of lines and pages in a .docx file"""
    try:
        doc = Document(file_path)
        num_lines = len(doc.paragraphs)
        # Approximate pages, as python-docx does not support page count directly
        page_lines = 20     # This can be adjusted as needed
        num_pages = (num_lines + page_lines - 1) // page_lines
        return num_lines, num_pages
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
        return 0, 0

def count_linepage_txtfile(file_path):
    """Count the number of lines in a .txt file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
        return 0

def count_linepage_pdffile(file_path):
    """Count the number of pages in a .pdf file"""
    try:
        doc = fitz.open(file_path)
        return len(doc)
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
        return 0

def extract_text_imagefile(file_path):
    """Extract text from an image file (placeholder)"""
    try:
        image = Image.open(file_path)
        # Using OCR to extract text from image
        text = pytesseract.image_to_string(image)
        num_lines = len(text.split('\n'))
        return num_lines
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
        return 0

def process_files(folder_path):
    """Process all supported files in the folder and count lines/pages"""
    
    # Process .txt files
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    for file_path in txt_files:
        num_lines = count_linepage_txtfile(file_path)
        print(f'{os.path.basename(file_path)}: {num_lines} lines')
    
    # Process .docx files
    doc_files = glob.glob(os.path.join(folder_path, "*.docx"))
    for file_path in doc_files:
        num_lines, num_pages = count_linepage_docxfile(file_path)
        print(f'{os.path.basename(file_path)}: {num_lines} lines, {num_pages} pages')

    # Process .pdf files
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    for file_path in pdf_files:
        num_pages = count_linepage_pdffile(file_path)
        print(f'{os.path.basename(file_path)}: {num_pages} pages')
    
    # Process image files (.jpg, .gif, .png)
    image_files = glob.glob(os.path.join(folder_path, "*.jpg")) + glob.glob(os.path.join(folder_path, "*.gif")) + glob.glob(os.path.join(folder_path, "*.png"))
    
    for file_path in image_files:
        num_lines = extract_text_imagefile(file_path)
        print(f'{os.path.basename(file_path)}: {num_lines} lines (extracted from image)')

# Folder path
folder_path = r"D:\Personal Documents\CV and All\IT Specialist"

# Process all files in the specified folder
process_files(folder_path)
