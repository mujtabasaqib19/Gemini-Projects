### AI Projects Using Gemini Pro

## Projects

### 1. **Image Model**
   - **Description**: Analyzes images and generates textual insights using Google Gemini Pro's large language and vision models.
   - **Features**:
     - Upload an image and provide textual input for context.
     - Receive insights about the image based on the input text.
   - **Technologies**: Streamlit, PIL, Google Gemini Pro.
   - **Run**:
     ```bash
     streamlit run image.py
     ```

---

### 2. **Invoice Extractor**
   - **Description**: Extracts and interprets information from invoice images, enabling users to understand and query invoice content effectively.
   - **Features**:
     - Upload an invoice image.
     - Answer specific queries related to the uploaded invoice using AI.
     - Designed to work with invoices in multiple languages.
   - **Technologies**: Streamlit, PIL, Google Gemini Pro.
   - **Run**:
     ```bash
     streamlit run invoice.py
     ```

---

### 3. **Resume Tracking System**
   - **Description**: Assesses resumes against job descriptions for percentage matching and professional evaluations using ATS (Applicant Tracking System) logic.
   - **Features**:
     - Upload a resume in PDF format.
     - Analyze and match the resume against a job description.
     - Provide a percentage match, missing keywords, and strengths/weaknesses evaluation.
   - **Technologies**: Streamlit, PyMuPDF, Google Gemini Pro.
   - **Run**:
     ```bash
     streamlit run resume.py
     ```

---

### 4. **SQL Querying App**
   - **Description**: Converts natural language questions into SQL queries and executes them on an SQLite database.
   - **Features**:
     - Input a natural language question.
     - Generate an SQL query from the question using AI.
     - Execute the query on a sample database and display results.
   - **Technologies**: Streamlit, SQLite, Google Gemini Pro.
   - **Run**:
     ```bash
     streamlit run querying.py
     ```

---

## Installation
### Prerequisites:
- Python 3.7+
- Google Cloud API Key for Gemini Pro
- Required Python libraries: `streamlit`, `google-generativeai`, `pillow`, `dotenv`, `sqlite3`, `fitz (PyMuPDF)`, `io`, `base64`

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/GeminiProjects/AI-Project-Suite.git
   cd AI-Project-Suite
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add your **Google Gemini Pro API key**:
     ```env
     GOOGLE_API_KEY=your_google_api_key
     ```

---

## Usage
1. Navigate to the desired project folder.
2. Run the Streamlit app for the selected project:
   ```bash
   streamlit run <project_script>.py
   ```
3. Follow the on-screen instructions to upload files, input queries, and view outputs.

---

## File Descriptions
- **image_model.py**: Code for the Image Model project.
- **invoice_extractor.py**: Code for the Invoice Extractor project.
- **resume_tracking_system.py**: Code for the Resume Tracking System project.
- **sql_querying.py**: Code for the SQL Querying App.
- **requirements.txt**: List of Python libraries required to run the projects.
- **.env**: Environment file to store API keys (to be created by the user).

---

## Features
- **AI-Powered**: Leverages Google Gemini Pro for advanced image, text, and query processing.
- **Streamlit Interface**: Provides an intuitive, web-based interface for interacting with AI models.
- **Modular Design**: Each project can run independently.
---

## Contact
For questions or suggestions, contact mujtabasaqib654@gmail.com.
