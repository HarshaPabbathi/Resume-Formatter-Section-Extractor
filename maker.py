import os
import json
from pathlib import Path
from datetime import datetime
from compile_latex import tex_to_pdf
import jinja2  # Added for rendering LaTeX template

UPLOAD_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def escape_latex(text):
    if not text:
        return ""
    return text.translate(str.maketrans({
        '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_',
        '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}', '\\': r'\textbackslash{}'
    }))

def generate_autocv(data, preview=False):
    # Build the context for template rendering
    context = {
        'name': escape_latex(data['personal_info']['name']),
        'email': escape_latex(data['personal_info'].get('email', '')),
        'phone': escape_latex(data['personal_info'].get('phone', '')),
        'github': escape_latex(data['personal_info'].get('github', '')),
        'linkedin': escape_latex(data['personal_info'].get('linkedin', '')),
        'summary': escape_latex(data.get('summary', '')),
        'work_experience': data.get('experience', []),
        'projects': data.get('projects', []),
        'education': data.get('education', []),
        'skills': [{'title': key, 'list': data.get('skills', {}).get(key, [])} for key in data.get('skills', {})]
    }
    
    # Load and render the LaTeX template from autoCV_template.tex
    template_path = os.path.join(os.path.dirname(__file__), "autoCV_template.tex")
    with open(template_path, 'r') as f:
        template_str = f.read()
    template = jinja2.Template(template_str)
    tex_content = template.render(**context)
    
    if preview:
        return tex_content

    filename = f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    filepath = Path(UPLOAD_FOLDER) / f"{filename}.tex"
    
    with open(filepath, 'w') as f:
        f.write(tex_content)
    
    tex_to_pdf(str(filepath))
    return str(filepath.with_suffix('.pdf'))


if __name__ == '__main__':
    sample_data_path = os.path.join(os.path.dirname(__file__), "sample_resume_data.json")
    if os.path.exists(sample_data_path):
        with open(sample_data_path) as f:
            resume_data = json.load(f)

        # Preview LaTeX to console
        latex_code = generate_autocv(resume_data, preview=True)
        print("\n===== LATEX OUTPUT =====\n")
        print(latex_code)

        # Generate PDF
        path = generate_autocv(resume_data, preview=False)
        print(f"\nPDF generated at: {path}")
    else:
        print("sample_resume_data.json not found. Please provide sample data to generate PDF.")
