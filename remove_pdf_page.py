"""
PDF page removal utility.

This module removes the first page from a PDF file and saves the result
to a new PDF file.
"""

import PyPDF2


def remove_first_page(input_pdf_path: str, output_pdf_path: str) -> None:
    """
    Remove the first page from a PDF file.

    Args:
        input_pdf_path: Path to input PDF file
        output_pdf_path: Path to save output PDF file

    Returns:
        None

    Example:
        >>> remove_first_page('input.pdf', 'output.pdf')
    """
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


def main() -> None:
    """
    Execute PDF first page removal with user input.

    Returns:
        None
    """
    input_pdf = input('input file location : ')
    output_pdf = r'C:\Users\manch\OneDrive\Desktop\CS4270\L09_fixed.pdf'
    remove_first_page(input_pdf, output_pdf)


if __name__ == '__main__':
    main()
