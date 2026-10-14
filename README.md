# ScamLens

## Explainable AI-Based Social Engineering Scam Risk Assessment Platform

ScamLens is a web-based platform for analyzing suspicious messages and identifying social-engineering scam indicators.

> **Project status:** Working prototype for academic evaluation.

## Features

- Suspicious message analysis
- Social-engineering signal detection
- Contextual risk scoring
- LOW, MEDIUM and HIGH risk classification
- Explainable risk indicators
- Safety recommendations
- URL detection
- Input validation
- Automated testing and evaluation

## Technology Stack

- React.js
- JavaScript
- CSS
- Python
- FastAPI
- Pydantic
- Uvicorn

## Risk Levels

| Score | Risk Level |
|------:|------------|
| 0-39 | LOW |
| 40-69 | MEDIUM |
| 70-100 | HIGH |

## System Workflow

User -> React Frontend -> FastAPI Backend -> Preprocessing -> Signal Detection -> Risk Scoring -> Explanation -> Safety Recommendations

## Evaluation

The current prototype was evaluated on 50 labelled messages: 25 SCAM and 25 SAFE.

| Metric | Result |
|--------|-------:|
| Accuracy | 100% |
| Precision | 100% |
| Recall | 100% |
| F1 Score | 100% |

A simple keyword-count baseline achieved 84% accuracy, 68% recall and 80.95% F1-score.

> **Important:** The evaluation dataset is small and prototype-specific. These results must not be interpreted as real-world scam detection accuracy.

## Testing

The project includes 11 automated tests covering preprocessing, scam detection, safe messages, URL detection, explanations, recommendations and input validation.

## Limitations

- The current risk engine is primarily signal/rule based.
- It does not guarantee detection of every scam.
- It does not currently perform external URL reputation checking.
- Persistent user history and sender-level tracking are not included in the current prototype.
- The evaluation dataset is small.

## Future Enhancements

- Machine-learning/NLP models
- LLM-based contextual analysis
- User accounts and analysis history
- Sender-level risk history
- Database integration
- URL reputation checking
- Larger evaluation datasets
- Production deployment

## Setup

### Backend

`powershell
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
` 

Backend: http://127.0.0.1:8000
Swagger: http://127.0.0.1:8000/docs

### Frontend

`powershell
cd frontend
npm install
npm run dev
` 

Frontend: http://localhost:5173

## Disclaimer

ScamLens is an academic prototype developed for educational and research purposes. The risk score is intended to support user awareness and is not definitive proof that a message is fraudulent or legitimate.

