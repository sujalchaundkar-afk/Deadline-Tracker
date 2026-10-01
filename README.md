# ⏰ Deadline Tracker

An AI-powered web application built with Streamlit and Gemini Vision that extracts structured academic and project deadlines from messy, real-world images such as syllabus, exam timetables, and assignment sheets, and dispatches automated notification digests via email.

---

## 🛠️ Tech Stack

* **Frontend / UI:** [Streamlit](https://streamlit.io/)
* **AI Core:** [Google Gemini API](https://ai.google.dev/) (`gemini-3.6-flash`)
* **Image Processing:** [Pillow (PIL)](https://python-pillow.org/)
* **Notification Engine:** Python `smtplib` (Gmail SMTP)
* **Language:** Python 3.10+

---

## ✨ Key Features

* **📷 Visual Deadline Extraction:** Parses complex timetable grids, assignment notices, and syllabus sheets using Gemini Vision models.
* **🛡️ Graceful Failure Handling:** Identifies non-schedule images and guides the user without raising unhandled exceptions.
* **⚡ Image Compression Pipeline:** Resizes and optimizes uploaded image payloads to improve API throughput and response speed.
* **🔄 Model Fallback Strategy:** Automatically rotates across standard Flash models to improve availability and handle quota limits (`429 Rate Limit`).
* **📧 Multi-Channel Alerts:** Dispatches structured Markdown summary digests to recipient email inboxes via Gmail SMTP.

---

## 📁 Repository Structure

```text
Deadline-Tracker/
├── .streamlit/
│   └── secrets.toml          # Local secrets (API keys & passwords) - Git-ignored
├── action_tool.py             # Email (SMTP)
├── app.py                     # Main Streamlit application entry point
├── prompts.py                 # Structured system prompt for Gemini Vision
├── requirements.txt           # Python dependencies
├── .gitignore                 # Excludes sensitive keys and cache files
└── README.md                  # Project documentation
```

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sujalchaundkar-afk/Deadline-Tracker.git
cd Deadline-Tracker
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure Local Credentials

Create a `.streamlit/secrets.toml` file inside your project root folder:

```toml
# Google Gemini API Key
GEMINI_API_KEY = "your_gemini_api_key"

# Gmail SMTP Configuration
GMAIL_ADDRESS = "your_email@gmail.com"
GMAIL_APP_PASSWORD = "your_16_digit_app_password"


```



### 4. Run the Application

```bash
python -m streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🎯 How to Use

1. **Configure Recipient:** Select **Gmail (SMTP)** in the sidebar and enter your recipient email address.
2. **Upload Document:** Upload a picture of a timetable, exam sheet, or syllabus (`PNG`, `JPG`, `JPEG`).
3. **Extract:** Click **Extract Deadlines** to run Gemini Vision analysis.
4. **Send Alert:** Click **Send Alert via Gmail (SMTP)** to dispatch the digest directly to your inbox.
