import PyPDF2

def remove_first_page(input_pdf_path, output_pdf_path):
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(input_pdf_path)
    
    # Create a PDF writer object for the output PDF
    writer = PyPDF2.PdfWriter()
    
    # Loop through all the pages except the first one and add them to the writer
    for i in range(1, len(reader.pages)):
        writer.add_page(reader.pages[i])
    
    # Write out the modified PDF to a new file
    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)

# Usage example
input_pdf = input('input file location : ')  # Replace with your PDF file path
output_pdf = r'C:\Users\manch\OneDrive\Desktop\CS4270\L09_fixed.pdf'  # Replace with your desired output PDF file path
remove_first_page(input_pdf, output_pdf)
