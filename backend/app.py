from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Capitalize On Compass', version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://[a-z0-9-]+\.vercel\.app",
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
PRODUCT = {"project_id": "45643e43-3b7e-4d82-b161-78a4cce47bf9", "product_name": "Capitalize On Compass", "idea": "Capitalize on the trillion-dollar AI boom by building software that reduces manual labor for businesses. High-value concepts include multi-agent orchestration platforms, department-specific legal and financial AI assistants, and AI tools for lead generation and automated sales follow-ups.", "problem": "Engineering, platform, and developer-experience teams need a safer, faster way to reduce the time from a risky change to a verified release decision. The opportunity should be tested through one repeatable decision workflow.", "elevator_pitch": "Capitalize On Compass helps engineering, platform, and developer-experience teams turn scattered evidence into a human-approved next action and prove whether the workflow improves a measurable outcome.", "target_users": ["engineering, platform, and developer-experience teams", "domain specialists", "an engineering or platform leader"], "features": ["Structured case or workflow intake", "Evidence-backed recommendation with confidence and rationale", "Human approval and override with an audit trail", "Pilot dashboard for time, quality, and adoption outcomes"], "market_gap": "A narrow software delivery workflow that links evidence, a human approval, and a measurable outcome remains more defensible than another general AI chat surface."}

@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "generated-mvp-api"}

@app.get("/api/overview")
def overview() -> dict:
    return {
        "product_name": PRODUCT["product_name"],
        "pitch": PRODUCT["elevator_pitch"],
        "problem": PRODUCT["problem"],
        "target_users": PRODUCT["target_users"],
        "features": PRODUCT["features"],
        "demo_data": True,
    }
