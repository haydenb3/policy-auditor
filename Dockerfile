# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY backend/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application code to the working directory
COPY backend/ .

# Copy the policy documents for content extraction
COPY Public\ Policies /app/Public\ Policies/

# Extract PDF content during build
RUN python3 -c "\
import os, json, sys; \
sys.path.append('/app'); \
from main import extract_text_from_pdf; \
pdf_dir = '/app/Public Policies'; \
content_dir = '/app/policy_content'; \
print('Starting PDF content extraction...'); \
if os.path.exists(pdf_dir): \
    os.makedirs(content_dir, exist_ok=True); \
    count = 0; \
    for root, dirs, files in os.walk(pdf_dir): \
        for file in files: \
            if file.endswith('.pdf'): \
                pdf_path = os.path.join(root, file); \
                content = extract_text_from_pdf(pdf_path); \
                if content: \
                    content_file = os.path.join(content_dir, file.replace('.pdf', '.json')); \
                    with open(content_file, 'w') as f: \
                        json.dump({'filename': file, 'content': content}, f); \
                    count += 1; \
                    print(f'Extracted content from {file}'); \
    print(f'Successfully extracted content from {count} PDF files'); \
else: \
    print('PDF directory not found, skipping content extraction')"

# Expose the port the app runs on
EXPOSE 8000

# Run the application
# We use 0.0.0.0 to ensure it's accessible from outside the container.
# The port is set by Railway via the $PORT environment variable.
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
