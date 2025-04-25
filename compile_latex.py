import subprocess
import shutil

def tex_to_pdf(tex_file):
    # Check if pdflatex is available in PATH
    pdflatex_path = shutil.which("pdflatex")
    if pdflatex_path is None:
        raise FileNotFoundError("pdflatex executable not found. Please install MiKTeX or TeX Live and ensure pdflatex is in your PATH")
    try:
        # Run pdflatex twice to resolve references (e.g., TOC, citations)
        subprocess.run(
            [pdflatex_path, '-interaction=nonstopmode', tex_file],
            check=True,
            stdout=subprocess.PIPE,  # Suppress output (optional)
            stderr=subprocess.PIPE
        )
        print(f"✅ PDF generated: {tex_file.replace('.tex', '.pdf')}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e.stderr.decode()}")

# Example usage
tex_to_pdf("test.tex")  # Replace with your .tex filename