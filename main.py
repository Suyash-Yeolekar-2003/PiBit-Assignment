import fitz  # PyMuPDF for handling PDF files
import re    # For regular expressions
import json  # For JSON handling

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file using PyMuPDF.
    
    Args:
        pdf_path (str): The file path to the PDF document.
        
    Returns:
        str: The extracted text from the PDF.
    """
    text = ""
    pdf_document = fitz.open(pdf_path)  # Open the PDF file
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  # Load each page
        text += page.get_text()  # Extract text from the page
    return text

def clean_text(text):
    """
    Clean up the extracted text by removing excessive whitespace.
    
    Args:
        text (str): The raw text extracted from the PDF.
        
    Returns:
        str: Cleaned text with excessive whitespace removed.
    """
    # Replace multiple newlines and tabs with a single space
    text = re.sub(r'[\n\t]+', ' ', text)
    return text.strip()

def extract_contact_info(text):
    """
    Extract contact information (email and phone number) from the text.
    
    Args:
        text (str): The cleaned text extracted from the PDF.
        
    Returns:
        dict: A dictionary containing email and phone number.
    """
    contact_info = {}
    # Define regex patterns for email and phone number
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+?\d[\d -]{8,}\d'

    # Search for email and phone number in the text
    email = re.search(email_pattern, text)
    phone_number = re.search(phone_pattern, text)

    # Add found email and phone number to the contact_info dictionary
    if email:
        contact_info['Email'] = email.group(0)
    if phone_number:
        contact_info['Phone Number'] = phone_number.group(0)
    
    return contact_info

def parse_resume(text):
    """
    Parse various sections of the resume from the cleaned text.
    
    Args:
        text (str): The cleaned text extracted from the PDF.
        
    Returns:
        dict: A dictionary with parsed sections of the resume.
    """
    # Define patterns to extract different sections of the resume
    patterns = {
        "Education": r"Education[\s\S]+?Experience",
        "Experience": r"Experience[\s\S]+?Projects",
        "Projects": r"Projects[\s\S]+?Skills",
        "Skills": r"Skills[\s\S]+?Course Work",
        "Course Work": r"Course Work[\s\S]+?Achievements",
        "Achievements": r"Achievements[\s\S]+?Certificates",
        "Certificates": r"Certificates[\s\S]+"
    }

    parsed_data = {}
    # Extract contact information
    contact_info = extract_contact_info(text)
    
    # Extract each section based on the defined patterns
    for section, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            # Clean up the extracted section text
            parsed_data[section] = match.group(0).replace(section, '').strip()
        else:
            # If no match is found, initialize the section with an empty string
            parsed_data[section] = ""

    # Rearrange the JSON structure to include contact information first
    final_output = {
        "Contact": contact_info,
        **parsed_data
    }

    return final_output

def main():
    """
    Main function to execute the resume parsing and output the JSON.
    """
    pdf_path = 'path/to/your/resume.pdf'  # Replace with the path to your PDF file
    text = extract_text_from_pdf(pdf_path)  # Extract text from the PDF
    clean_text_data = clean_text(text)  # Clean the extracted text
    parsed_resume = parse_resume(clean_text_data)  # Parse the cleaned text
    
    # Convert the parsed resume to JSON format with indentation
    json_output = json.dumps(parsed_resume, indent=4)
    
    # Print the JSON output
    print(json_output)

if __name__ == "__main__":
    main()
