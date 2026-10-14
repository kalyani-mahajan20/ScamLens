from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Suspicious message to analyze"
    )


class AnalyzeResponse(BaseModel):
    message: str
    risk_score: int
    risk_level: str
    indicators: list[str]
    explanation: str
    recommendations: list[str]
    processing_time: float