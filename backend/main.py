from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from time import perf_counter

from models.schemas import AnalyzeRequest, AnalyzeResponse

from analyzer.preprocessing import preprocess_text
from analyzer.signals import detect_signals
from analyzer.risk_engine import calculate_risk_score, get_risk_level
from analyzer.explanation import generate_explanation
from analyzer.recommendations import generate_recommendations

app = FastAPI(
    title="ScamLens API",
    description="Explainable AI-Based Social Engineering Scam Risk Assessment Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "ScamLens API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_message(request: AnalyzeRequest):

    start_time = perf_counter()

    # 1. Preprocess the submitted message
    cleaned_text = preprocess_text(request.message)

    # 2. Detect social-engineering warning signals
    signals = detect_signals(cleaned_text)

    # 3. Calculate numerical risk score
    risk_score = calculate_risk_score(signals)

    # 4. Convert score into risk category
    risk_level = get_risk_level(risk_score)

    # 5. Generate evidence-based explanation
    explanation = generate_explanation(signals)

    # 6. Generate safety recommendations
    recommendations = generate_recommendations(signals)

    # 7. Calculate processing time
    processing_time = round(perf_counter() - start_time, 4)

    # 8. Return complete analysis
    return {
        "message": request.message,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "indicators": list(signals.keys()),
        "explanation": explanation,
        "recommendations": recommendations,
        "processing_time": processing_time
    }