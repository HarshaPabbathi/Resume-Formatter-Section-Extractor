# 📄 Resume Formatter & Section Extractor

Automate the process of creating well-structured, professional resumes using LaTeX. This Python-based tool extracts key sections from your resume data and formats them into a polished PDF using a customizable LaTeX template.

## ✨ Features

- 📑 Extracts and organizes resume sections: Personal Info, Education, Experience, Projects, Skills, etc.
- 🧾 Automatically populates a LaTeX resume template
- 📄 Generates clean, professional PDF resumes
- ⚙️ Customizable via configuration files
- 🖥️ Command-line interface for automation

---

## 📁 Project Structure

Resume-Formatter-Section-Extractor/ │ ├── app.py # Main entry point to generate the resume ├── maker.py # Extracts sections and injects them into LaTeX ├── compile_latex.py # Compiles LaTeX into PDF ├── autoCV_template.tex # LaTeX template used for resume formatting ├── config.yaml # Configuration for formatting and content ├── requirements.txt # Python dependencies ├── output/ # Directory where generated PDFs are saved └── sample_data/ # Example inputs or sample resumes (if provided)


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/HarshaPabbathi/Resume-Formatter-Section-Extractor.git
cd Resume-Formatter-Section-Extractor

2. Install Dependencies
Make sure you have Python installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
You'll also need a LaTeX distribution installed (e.g., TeX Live or MiKTeX) to compile the PDF.

3. Run the Application
bash
Copy
Edit
python app.py
The script will process your input data and generate a professional resume in PDF format using the autoCV_template.tex.

🛠 Customization
Modify config.yaml to change input fields or format preferences.

Edit autoCV_template.tex if you want to tweak the LaTeX styling (e.g., fonts, layout, colors).

Update logic in maker.py if you need to extract custom sections.

📦 Dependencies
Python 3.x

PyYAML

LaTeX (pdflatex or xelatex)

Install Python packages:

bash
Copy
Edit
pip install -r requirements.txt
📄 Sample Output
A sample generated PDF is available in the output/ directory. You can modify the input or template to suit your design preferences.

