import os
import glob
from docx import Document
from docx.opc.exceptions import PackageNotFoundError

def read_docx(file_path):
    """Load the *.docx file and extract text"""
    try:
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except PackageNotFoundError:
        print(f"Skipping file (not a valid .docx or temporary file): {file_path}")
        return ""
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def count_concurrentword(text, word):
    """Count occurrences of a specific word"""
    return text.lower().split().count(word.lower())

def count_word_in_all_docx(folder_path, word):
    """Count occurrences of the specific word in all *.docx files in the folder"""
    total_count = 0
    docx_files = glob.glob(os.path.join(folder_path, '*.docx'))
    
    for file_path in docx_files:
        text = read_docx(file_path)
        word_count = count_concurrentword(text, word)
        total_count += word_count
        if text:
            print(f'{word} appears {word_count} times in {os.path.basename(file_path)}')
    
    print(f'Total occurrences of "{word}" in all .docx files: {total_count}')

# Folder path containing the .docx files (use raw string literal to avoid invalid escape sequences)
folder_path = r"D:\Personal Documents\CV and All\IT Specialist"

# Specific word to count
given_word = "Rajib"

# Count the given word in all .docx files in the specified folder
count_word_in_all_docx(folder_path, given_word)
