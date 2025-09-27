import os
import json
import sys
from main import extract_text_from_pdf

pdf_dir = '/app/Public Policies'
content_dir = '/app/policy_content'

print('--- Starting PDF content extraction script ---')

if not os.path.exists(pdf_dir):
    print(f'Error: PDF directory "{pdf_dir}" not found. Skipping content extraction.')
    sys.exit(1)

os.makedirs(content_dir, exist_ok=True)
count = 0
pdf_files = [os.path.join(root, file) for root, _, files in os.walk(pdf_dir) for file in files if file.endswith('.pdf')]

print(f'Found {len(pdf_files)} PDF files to process...')

for pdf_path in pdf_files:
    file = os.path.basename(pdf_path)
    print(f'Processing {file}...')
    content = extract_text_from_pdf(pdf_path)
    if content:
        content_file = os.path.join(content_dir, file.replace('.pdf', '.json'))
        with open(content_file, 'w') as f:
            json.dump({'filename': file, 'content': content}, f)
        count += 1

print(f'--- Successfully extracted content from {count} PDF files ---')
