# Free-ATS-Resume-Scanner

## Overview
The **Free ATS Resume Scanner** is a web application developed using Python Flask that provides two main functionalities:
1. **Keyword Extraction**: Extracts and displays key skills and keywords from a job description.
2. **Resume Matching**: Compares a resume against a job description to calculate a match percentage and highlights the keywords present in the resume. Users can download the results as a PDF.

## Features

- **Extract Keywords**: Upload a job description and receive a list of key skills and keywords.
- **Resume Matching**: Upload a resume and job description to calculate the match percentage. The result is displayed with a donut chart and the matched keywords are shown in columns.
- **Download Results**: Option to download the resume match results as a PDF file.

## Technology Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript
- **PDF Generation**: ReportLab
- **Libraries**:
  - Flask
  - ReportLab
  - PyPDF2 (or PdfReader for newer versions)

## Project Structure
    Free_ATS-Resume_Scan/
    │
    ├── static/
    │ └── styles.css
    │
    ├── templates/
    │ ├── index.html
    │ ├── keywords_result.html
    │ └── match_result.html
    │
    ├── app.py
    ├── requirements.txt
    └── README.md

  ## To Clone the Repository
  ## Stepup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/kishorekumar0814/free-ats-resume-scanner.git
    cd free-ats-resume-scanner
    ```

2. **Install Dependencies**:

    Make sure you have Python 3.6 or higher installed. Then, create a virtual environment and install the required packages:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the Application**:

    Start the Flask application:

    ```bash
    python app.py
    ```

    Open your browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

1. **Homepage**: Choose between "Extract Keywords" or "Resume Matching" options.
2. **Extract Keywords**:
    - Upload a job description file (PDF, DOC, DOCX).
    - View the extracted keywords displayed in a grid layout.
3. **Resume Matching**:
    - Upload both a job description and a resume file.
    - View the match percentage displayed as a donut chart.
    - Download the results as a PDF file.

## Dependencies

The required Python packages are listed in `requirements.txt`. They include:

- Flask
- ReportLab
- PyPDF2 (or PdfReader for newer versions)
- Any other packages used in your project

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Flask**: Micro web framework for Python.
- **ReportLab**: Library for generating PDFs.
- **PyPDF2**: Library for handling PDF files.

## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [ReportLab Documentation](https://www.reportlab.com/docs/)
- [PyPDF2 Documentation](https://pypi.org/project/PyPDF2/)

  ## Contact

For additional information or to contribute to the project, please reach out via email:

- **Email**: [Gmail](mailto:kishorekumar1409@gmail.com)

For any issues or contributions, please open an issue or submit a pull request on the [GitHub repository](https://github.com/kishorekumar0814/free-ats-resume-scanner).

*Project Report:*  [Project_Report.docx](https://github.com/user-attachments/files/16409991/Project_Report.docx)
