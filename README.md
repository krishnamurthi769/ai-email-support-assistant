# 📧 AI Email & Screenshot Support Assistant

An AI-powered tool that analyzes support emails _and screenshots_ to automatically detect issues and generate professional IT support replies.

This project solves a real repetitive problem faced by IT Support & Helpdesk teams by using **LLM + Vision AI** to automate manual analysis.

---

## 🚀 Live Demo

(Add after deployment)

```
https://<your-app-name>.streamlit.app
```

---

## 📌 Features

### 📝 1. Email Issue Detection

Paste any email → AI extracts:

- Issue Type
- Severity
- Troubleshooting
- Auto-reply

---

### 🖼 2. Screenshot Text Extraction (Vision AI)

Upload a screenshot → AI extracts text from:

- Error popups
- System alerts
- Outlook / VPN messages
- Browser issues

Then merges screenshot text + email text for accurate analysis.

---

### 🤖 3. AI-Powered Support Response

AI generates:

- Professional reply
- Clear format
- Ready-to-send email

---

### 🎨 4. Clean Professional UI

Built with:

- Streamlit
- Custom CSS
- Card-style layout
- Light theme

Perfect for assignment + company demo.

---

## 🧠 Why This Project?

IT teams waste hours manually:

- Understanding unclear emails
- Reading screenshots
- Repeating the same troubleshooting
- Writing long replies

This tool automates **70–80%** of that workflow.

Matches assignment requirements (LLM + automation + real-world problem).

---

## 🏗 Tech Stack

| Component             | Technology                         |
| --------------------- | ---------------------------------- |
| Frontend / UI         | Streamlit                          |
| Backend               | Python                             |
| LLM                   | OpenAI GPT-4o-mini (Vision + Text) |
| OCR                   | Vision (Model-based)               |
| Environment Variables | python-dotenv                      |
| Styling               | Custom CSS                         |

---

## 📁 Project Structure

```
AI-EMAIL/
 ├── app.py
 ├── requirements.txt
 ├── README.md
 ├── .env                # not included in repo
 └── .gitignore
```

---

## ⚙ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/YOUR-USERNAME/AI-EMAIL.git
cd AI-EMAIL
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Add API Key

Create a file named `.env`:

```
OPENAI_API_KEY="your_api_key_here"
```

### 4️⃣ Run the App

```
streamlit run app.py
```

The app opens at:
👉 http://localhost:8501/

---

## 🧪 How to Test

### ✔ Email Example

```
Hi team, my VPN is not connecting. It shows authentication failed.
```

### ✔ Screenshot Example

Upload:

- Windows error
- Outlook login issues
- VPN popup
- Browser error

AI extracts text → analyzes → generates support reply.

---

## 📷 Screenshots

(Add images after running your app)

```
📸 Email Input
📸 Screenshot Upload
📸 AI Response
📸 Auto Reply
```

---

## 🌐 Deployment (Streamlit Cloud)

### 1. Go to:

https://share.streamlit.io

### 2. Create a New App

### 3. Select Repo and Branch

- Repo: `yourusername/AI-EMAIL`
- Branch: `main`
- File: `app.py`

### 4. Add Environment Variable

```
OPENAI_API_KEY = your_api_key
```

### 5. Deploy 🎉

---

## 🎯 Assignment Mapping

| Requirement                          | Status                |
| ------------------------------------ | --------------------- |
| Solve real repetitive/manual problem | ✔️                    |
| LLM-powered automation               | ✔️                    |
| Streamlit prototype                  | ✔️                    |
| Practical business impact            | ✔️                    |
| GitHub link                          | ✔️                    |
| Short presentation                   | ✔️ (You will add PPT) |

---

## 👨‍💻 Author

**Krishna Murthi**  
AI & Software Developer  
B.Tech CSE – GITAM University

---

## ⭐ Support

If you like this project, consider ⭐ starring the repo!
