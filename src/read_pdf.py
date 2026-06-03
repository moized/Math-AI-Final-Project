import PyPDF2

def read_pdf(pdf_path):
    """
    Read and extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
    
    Returns:
        str: Extracted text from the PDF
    """
    text = ""
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            print(f"Total pages: {num_pages}\n")
            
            for page_num, page in enumerate(pdf_reader.pages):
                print(f"--- Page {page_num + 1} ---")
                page_text = page.extract_text()
                text += page_text + "\n"
                print(page_text[:200] + "...\n")  # Print first 200 characters of each page
        
        return text
    
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None


if __name__ == "__main__":
    # Read both PDFs
    pdf_files = [
        "Tutorial on Variational Autoencoders (VAE) (2021 revision).pdf",
        "VAE Raporu - Mohammed Izedin Mohammed.pdf"
    ]
    
    all_text = {}
    
    for pdf_file in pdf_files:
        print(f"\n{'='*60}")
        print(f"Reading: {pdf_file}")
        print(f"{'='*60}\n")
        
        full_text = read_pdf(pdf_file)
        
        if full_text:
            all_text[pdf_file] = full_text
            # Save each PDF's text to a separate file
            output_filename = pdf_file.replace(".pdf", "_extracted.txt")
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(full_text)
            print(f"\nText extracted and saved to '{output_filename}'\n")
    
    print(f"\n{'='*60}")
    print("Summary:")
    print(f"{'='*60}")
    for pdf_file in all_text:
        print(f"✓ {pdf_file} - {len(all_text[pdf_file])} characters extracted")
