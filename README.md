# ScamLens

## Explainable AI-Based Social Engineering Scam Risk Assessment Platform

ScamLens is a web-based platform designed to analyze suspicious messages and identify **social-engineering scam indicators** such as urgency, threats, financial requests, credential requests, authority impersonation, rewards, suspicious links, and scam-specific patterns.

The platform provides a **risk score, risk level, explainable indicators, and safety recommendations** to help users understand why a message may be suspicious.

> **Project Status:** Working prototype developed for academic evaluation and research.

---

## 🎯 Objectives

ScamLens aims to:

- Detect potential social-engineering scam messages.
- Identify manipulation techniques such as urgency, fear, authority, rewards, and financial pressure.
- Calculate a numerical scam-risk score.
- Classify messages into LOW, MEDIUM, or HIGH risk.
- Explain the factors contributing to the detected risk.
- Provide actionable safety recommendations.
- Evaluate the prototype using labelled scam and safe messages.
- Compare the proposed risk engine with a simple keyword-count baseline.

---

## ✨ Key Features

- 🔍 **Suspicious Message Analysis**
- 🚨 **Social-Engineering Signal Detection**
- 📊 **Contextual Risk Scoring**
- 🟢 **LOW / MEDIUM / HIGH Risk Classification**
- 💡 **Explainable Risk Indicators**
- 🛡️ **Safety Recommendations**
- 🔗 **URL Detection**
- ✅ **Input Validation**
- 🧪 **Automated Testing**
- 📈 **Prototype Evaluation and Baseline Comparison**

---

## 🧠 How ScamLens Works

The system follows a modular analysis pipeline:

```text
User
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
Text Preprocessing
  ↓
Signal Detection
  ↓
Contextual Risk Scoring
  ↓
Risk Classification
  ↓
Explanation Generation
  ↓
Safety Recommendations
  ↓
Result Display
```

### Analysis Pipeline

**1. Message Input**

The user enters a suspicious message into the ScamLens interface.

**2. Preprocessing**

The backend cleans and normalizes the message before analysis.

**3. Signal Detection**

The system identifies risk-related signals such as:

- Urgency
- Threats
- Financial requests
- Credential requests
- Rewards
- Authority impersonation
- Suspicious links
- Investment scams
- Job scams
- Delivery scams
- Loan/refund scams

**4. Contextual Risk Scoring**

Detected signals are assigned risk weights. Relevant combinations of signals can receive additional contextual risk scores.

**5. Risk Classification**

The final score is converted into a risk level:

| Score | Risk Level |
|---|---|
| 0–39 | 🟢 LOW |
| 40–69 | 🟡 MEDIUM |
| 70–100 | 🔴 HIGH |

**6. Explainability**

ScamLens identifies the factors that contributed to the risk assessment and explains why the message may be suspicious.

**7. Safety Recommendations**

The system provides recommendations based on the detected risk indicators.

---

## 🏗️ Project Architecture

```text
ScamLens/
│
├── backend/
│   ├── analyzer/
│   │   ├── preprocessing.py
│   │   ├── signals.py
│   │   ├── risk_engine.py
│   │   ├── explanation.py
│   │   └── recommendations.py
│   │
│   ├── evaluation/
│   │   ├── dataset.py
│   │   ├── evaluate.py
│   │   └── baseline.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── tests/
│   │   └── test_scam_lens.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── package-lock.json
│
├── .gitignore
└── README.md
```

---

## 🛠️ Technology Stack

### Frontend

- React.js
- JavaScript
- CSS
- Vite

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

### Testing & Evaluation

- Python `unittest`
- Custom labelled evaluation dataset
- Keyword-count baseline
- Accuracy
- Precision
- Recall
- F1-score

---

## 📊 Prototype Evaluation

The current prototype was evaluated on **50 labelled messages**:

- **25 SCAM**
- **25 SAFE**

### ScamLens Results

| Metric | Result |
|---|---:|
| Accuracy | **100%** |
| Precision | **100%** |
| Recall | **100%** |
| F1 Score | **100%** |

### Baseline Comparison

A simple keyword-count baseline was also implemented for comparison.

| Metric | Keyword Baseline | ScamLens |
|---|---:|---:|
| Accuracy | 84% | **100%** |
| Precision | 100% | **100%** |
| Recall | 68% | **100%** |
| F1 Score | 80.95% | **100%** |

The baseline used a simple keyword-count scoring approach, while ScamLens incorporates categorized signals and contextual risk scoring.

> **Important:** The evaluation dataset is small and prototype-specific. The reported 100% metrics should **not** be interpreted as real-world scam detection accuracy.

---

## 🔬 Iterative Development

The risk engine was improved through an evaluation-driven development process.

### Initial Prototype

The initial signal-based prototype was evaluated on an expanded dataset of 50 messages.

Results:

- Accuracy: 84%
- Precision: 100%
- Recall: 68%
- F1-score: 80.95%

### Error Analysis

False negatives were analyzed to identify missed scam patterns.

Several messages, particularly:

- Delivery scams
- Job scams
- Investment scams
- Loan/refund scams

contained relevant signals but were not receiving sufficient contextual risk.

### Improved Risk Engine

The signal taxonomy was expanded and contextual scoring rules were introduced.

The resulting prototype achieved:

- Accuracy: 100%
- Precision: 100%
- Recall: 100%
- F1-score: 100%

on the current 50-message prototype dataset.

---

## 🧪 Testing

The project contains **11 automated tests** covering:

- Text preprocessing
- Bank scam detection
- Delivery scam detection
- Investment scam detection
- Safe message handling
- URL detection
- Explanation generation
- Safety recommendations
- Empty input validation
- Maximum input length validation
- Valid input validation

Run the test suite using:

```powershell
cd backend
python -m unittest discover -s tests -v
```

Expected result:

```text
Ran 11 tests

OK
```

---

## 🔌 API

ScamLens provides a FastAPI backend.

### Health Check

```text
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

### Analyze Message

```text
POST /analyze
```

Example request:

```json
{
  "message": "URGENT! Your bank account will be suspended today. Verify your account immediately."
}
```

The API returns:

- Original message
- Risk score
- Risk level
- Detected indicators
- Explanation
- Safety recommendations
- Processing time

### Interactive API Documentation

When the backend is running:

```text
http://127.0.0.1:8000/docs
```

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

- Python 3.x
- Node.js
- npm

---

### 1. Clone the Repository

```powershell
git clone https://github.com/kalyani-mahajan20/ScamLens.git
cd ScamLens
```

---

### 2. Start the Backend

```powershell
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

### 3. Start the Frontend

Open another terminal:

```powershell
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## 🔐 Current Scope

The current prototype focuses on:

- Suspicious message analysis
- Social-engineering signal detection
- Explainable risk scoring
- Safety recommendations
- Prototype evaluation

The system is designed as an **analysis and awareness tool**, not as an automated enforcement system.

---

## ⚠️ Limitations

The current prototype has several limitations:

- The current risk engine is primarily signal/rule based.
- It does not guarantee detection of every scam.
- It does not replace banks, law-enforcement agencies, or professional security tools.
- It does not automatically block messages or transactions.
- It does not currently perform external URL reputation checking.
- Persistent user history is not included in the current prototype.
- Sender-level risk tracking is not included.
- The evaluation dataset is relatively small.
- A high risk score is not legal proof that a message is fraudulent.

---

## 🔮 Future Enhancements

Future versions of ScamLens can include:

- Machine-learning/NLP classification models
- LLM-based contextual analysis
- Larger and more diverse datasets
- User accounts
- Persistent analysis history
- Sender-level risk history
- Database integration
- External URL reputation checking
- Advanced multilingual analysis
- Production deployment
- Continuous model evaluation

---

## 🎓 Academic Context

ScamLens is developed as a final-year academic project focused on:

- Artificial Intelligence
- Natural Language Processing
- Explainable AI
- Cybersecurity
- Social Engineering
- Web Application Development

The project demonstrates how explainable risk assessment can be used to improve awareness of potential social-engineering attacks.

---

## 👩‍💻 Project

**ScamLens — An Explainable AI-Based Social Engineering Scam Risk Assessment Platform**

Developed as an academic project by:

**Kalyani Mahajan**

GitHub:

https://github.com/kalyani-mahajan20

Repository:

https://github.com/kalyani-mahajan20/ScamLens

---

## ⚠️ Disclaimer

ScamLens is an academic prototype developed for educational and research purposes.

The generated risk score is intended to support user awareness and should not be treated as definitive proof that a message is fraudulent or legitimate.

Users should independently verify suspicious requests through trusted official channels and should never share passwords, OTPs, PINs, or other sensitive credentials based solely on a message.

---
