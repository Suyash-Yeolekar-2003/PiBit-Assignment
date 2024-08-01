```markdown
# Resume Parsing Script

This Python script extracts and parses information from a resume PDF, converting it into a structured JSON format. It uses the `PyMuPDF` library to extract text from PDF files, cleans the text, and then parses sections like Contact Information, Education, Experience, Projects, Skills, Course Work, Achievements, and Certificates.

## Requirements

- Python 3.x
- PyMuPDF (`fitz`)
- Regular Expressions (`re`)
- JSON

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/resume-parsing.git
   cd resume-parsing
   ```

2. **Install the required libraries:**

   You can install the necessary libraries using `pip`:

   ```sh
   pip install PyMuPDF
   ```

## Usage

1. **Place your resume PDF in the project directory** or provide the path to the PDF file.

2. **Modify the `pdf_path` variable** in the `main` function of `main.py` to point to your PDF file:

   ```python
   pdf_path = 'path/to/your/resume.pdf'  # Replace with the path to your PDF file
   ```

3. **Run the script:**

   Execute the script using Python:

   ```sh
   python main.py
   ```

4. **View the output:**

   The script will print the JSON output to the console. You can redirect this output to a file if needed:

   ```sh
   python main.py > parsed_resume.json
   ```

## Script Overview

- **`extract_text_from_pdf(pdf_path)`**: Extracts text from the PDF file.
- **`clean_text(text)`**: Cleans up the extracted text by removing excessive whitespace.
- **`extract_contact_info(text)`**: Extracts contact information such as email and phone number from the text.
- **`parse_resume(text)`**: Parses various sections of the resume and organizes them into a dictionary.
- **`main()`**: Main function to execute the text extraction, cleaning, parsing, and JSON output.

Feel free to modify and extend this README to better suit your project's needs.
