from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="Disaster Credibility API")

class DisasterInput(BaseModel):
    text: str
    location: str
    time: str

def simple_ai_analysis(text):
    # MVP：用規則 + 隨機模擬 AI
    keywords_high = ["淹水", "爆炸", "倒塌", "受困"]
    keywords_low = ["好像", "可能", "聽說"]

    score = 0.5

    if any(k in text for k in keywords_high):
        score += 0.3
    if any(k in text for k in keywords_low):
        score -= 0.2

    score = max(0, min(1, score + random.uniform(-0.1, 0.1)))

    if score > 0.75:
        level = "高"
        reason = "描述具體且包含災害關鍵字"
    elif score > 0.5:
        level = "中"
        reason = "資訊部分明確但仍有不確定性"
    else:
        level = "低"
        reason = "資訊模糊或缺乏佐證"

    return score, level, reason

@app.post("/analyze")
def analyze(data: DisasterInput):
    score, level, reason = simple_ai_analysis(data.text)

    return {
        "可信度": round(score, 2),
        "風險等級": level,
        "不確定性說明": reason
    }