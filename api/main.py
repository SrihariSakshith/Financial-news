from fastapi import FastAPI
from rag_pipeline.summarizer import Summarizer
from rag_pipeline.compliance_monitor import ComplianceMonitor

app = FastAPI()

summarizer = Summarizer(api_key="your_openai_api_key")
compliance_monitor = ComplianceMonitor(keywords=["SEC", "regulation", "compliance"])

@app.post("/summarize/")
def summarize_news(text: str):
    summary = summarizer.summarize(text)
    risks = compliance_monitor.detect_risks(text)
    return {"summary": summary, "risks": risks}
