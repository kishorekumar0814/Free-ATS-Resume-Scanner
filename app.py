from flask import Flask, render_template, request, send_file
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from PyPDF2 import PdfReader
from docx import Document
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Ensure nltk resources are available
nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([' '.join(filtered_tokens)])
    keywords = vectorizer.get_feature_names_out()
    return keywords

def extract_text_from_resume(file):
    if file.filename.endswith('.pdf'):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
    elif file.filename.endswith('.docx'):
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        text = ""
    return text

def calculate_match_percentage(keywords, resume_text):
    resume_words = word_tokenize(resume_text.lower())
    matched_words = set(keywords).intersection(set(resume_words))
    if len(keywords) == 0:
        return 0
    return (len(matched_words) / len(keywords)) * 100

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/extract_keywords', methods=['POST'])
def extract_keywords_route():
    job_description = request.form['job_description']
    keywords = extract_keywords(job_description)
    return render_template('keywords_result.html', keywords=keywords)

@app.route('/download_result')
def download_result():
    # Extract parameters from the request
    percentage = request.args.get('percentage')
    keywords = request.args.get('keywords')

    # Create a BytesIO buffer to hold the PDF
    buffer = BytesIO()
    
    # Create a PDF canvas
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Draw text on the PDF
    c.drawString(100, height - 100, "Resume Matching Result")
    c.drawString(100, height - 120, f"Match Percentage: {percentage}")
    c.drawString(100, height - 140, "Matched Keywords:")
    
    # Split keywords into lines if too long
    y = height - 160
    keyword_lines = keywords.split(', ')
    for keyword in keyword_lines:
        c.drawString(100, y, keyword)
        y -= 20
        if y < 50:  # Check if we need to create a new page
            c.showPage()
            y = height - 100

    # Save the PDF
    c.save()
    buffer.seek(0)

    # Return the PDF file to the user
    return send_file(
        buffer,
        as_attachment=True,
        download_name='match_result.pdf',
        mimetype='application/pdf'
    )

@app.route('/match_resume', methods=['POST'])
def match_resume_route():
    job_description = request.form['job_description']
    resume_file = request.files['resume']

    keywords = extract_keywords(job_description)
    resume_text = extract_text_from_resume(resume_file)
    match_percentage = calculate_match_percentage(keywords, resume_text)
    
    # Determine color based on match percentage
    if match_percentage <= 30:
        color = 'red'
    elif match_percentage <= 75:
        color = 'yellow'
    else:
        color = 'green'
    
    # Find matched keywords
    resume_words = set(word_tokenize(resume_text.lower()))
    matched_keywords = [keyword for keyword in keywords if keyword.lower() in resume_words]

    # Prepare keywords for download
    matched_keywords_str = ', '.join(matched_keywords)
    
    return render_template(
        'match_result.html',
        match_percentage=match_percentage,
        color=color,
        matched_keywords=matched_keywords,
        download_url=f'/download_result?percentage={match_percentage}&keywords={matched_keywords_str}'
    )

if __name__ == '__main__':
    app.run(debug=True)