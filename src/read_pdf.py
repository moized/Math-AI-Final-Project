import os
import pdfplumber

def read_pdf_high_fidelity(pdf_path):
    """
    Extracts text from an academic PDF while preserving layout 
    and handling multi-column scientific text structure cleanly.
    """
    extracted_text = ""
    
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File '{pdf_path}' not found.")
        return None

    try:
        with pdfplumber.open(pdf_path) as pdf:
            num_pages = len(pdf.pages)
            print(f"Processing: {os.path.basename(pdf_path)} ({num_pages} pages)")
            
            for page_num, page in enumerate(pdf.pages):
                # .extract_text(layout=True) attempts to layout text close to original positioning
                page_text = page.extract_text(layout=False)
                if page_text:
                    extracted_text += f"\n--- Page {page_num + 1} ---\n" + page_text + "\n"
                    
        return extracted_text
    except Exception as e:
        print(f"❌ Error reading PDF {pdf_path}: {e}")
        return None

if __name__ == "__main__":
    # Base directory targets your newly organized reports folder
    reports_dir = os.path.join(os.getcwd(), "reports")
    
    # Corrected, snake_case academic filenames located in reports/
    pdf_targets = [
        "tutorial_vae.pdf",
        "vae_report.pdf"
    ]
    
    print("🔄 Starting High-Fidelity Text Extraction Pipeline...\n")
    
    for pdf_name in pdf_targets:
        full_pdf_path = os.path.join(reports_dir, pdf_name)
        
        extracted_content = read_pdf_high_fidelity(full_pdf_path)
        
        if extracted_content:
            # Generate target name inside the same reports folder
            output_txt_name = pdf_name.replace(".pdf", "_extracted.txt")
            full_output_path = os.path.join(reports_dir, output_txt_name)
            
            with open(full_output_path, "w", encoding="utf-8") as f:
                f.write(extracted_content)
            print(f"✅ Saved clean extraction to: reports/{output_txt_name}\n")
            
    print("🎉 Ingestion processing complete.")