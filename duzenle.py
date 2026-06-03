import os
import shutil

# 1. Klasörleri oluştur (Minimalist Plan + Düzen için Notebooks)
folders = ['data', 'src', 'reports', 'presentation', 'notebooks']
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# 2. Nokta atışı taşıma ve snake_case isim temizliği haritası
move_map = {
    # Kodlar -> src/
    'read_pdf.py': 'src/read_pdf.py',
    'generate_presentation.py': 'src/generate_presentation.py',
    
    # Veri -> data/
    'veri.csv': 'data/veri.csv',
    
    # Sunumlar -> presentation/
    'Sunum.txt': 'presentation/sunum_notlari.txt',
    'Sunum.pptx': 'presentation/final_presentation.pptx',
    'Sunum.html': 'presentation/sunum.html',
    'Sunum.jpg': 'presentation/sunum_kapak.jpg',
    'VAE_Final_Project_Presentation_STUDENT_ID_REMOVED.pptx': 'presentation/vae_presentation_255b7003.pptx',
    'VAE_Presentation.html': 'presentation/vae_presentation.html',
    
    # Raporlar ve Akademik Metinler -> reports/
    'submission_notes.txt': 'reports/submission_notes.txt',
    'whatwecoveredınclass.txt': 'reports/class_notes.txt',
    'Tutorial on Variational Autoencoders (VAE) (2021 revision).pdf': 'reports/tutorial_vae.pdf',
    'Tutorial on Variational Autoencoders (VAE) (2021 revision)_extracted.txt': 'reports/tutorial_vae_extracted.txt',
    'VAE Raporu - Mohammed Izedin Mohammed.pdf': 'reports/vae_report.pdf',
    'VAE Raporu - Mohammed Izedin Mohammed_extracted.txt': 'reports/vae_report_extracted.txt',
    'VAE_Final_Project_Report.html': 'reports/vae_final_project_report.html',
    'VAE_Final_Project.html': 'reports/vae_final_project.html',
    'VAE_Final_Project.pdf': 'reports/vae_final_project.pdf',
    'VAE_Final_Project_Submission.zip': 'reports/vae_final_project_submission.zip',
    'extracted_text.txt': 'reports/extracted_text.txt',
    
    # Notebooks -> notebooks/
    'VAE_Final_Project.ipynb': 'notebooks/vae_final_project.ipynb',
    
    # Görseller / Grafikler -> reports/ altına (README'de göstermek için ideal yer)
    'loss_convergence.png': 'reports/loss_convergence.png',
    'latent_grid.png': 'reports/latent_grid.png',
    'VAE_results.png': 'reports/vae_results.png',
    'beta_ablation.png': 'reports/beta_ablation.png',
    'generated_samples.png': 'reports/generated_samples.png',
    'latent_manifold.png': 'reports/latent_manifold.png',
    'recon_error_hist.png': 'reports/recon_error_hist.png',
    'reconstruction_comparison.png': 'reports/reconstruction_comparison.png',
    'ytu_logo.png': 'reports/ytu_logo.png'
}

# 3. Dosyaları güvenli bir şekilde taşı
for src, dst in move_map.items():
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"✅ Taşındı ve Yeniden Adlandırıldı: {src} -> {dst}")

print("\n🎉 Klasör yapısı başarıyla modernize edildi!")