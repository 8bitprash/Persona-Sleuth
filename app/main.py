from typing import Optional
from fastapi import FastAPI, UploadFile, File, Form, HTTPException

app = FastAPI(title="Persona-Sleuth")

@app.post("/ingest")
async def ingest(
    image: Optional[UploadFile] = File(None),
    name: Optional[str] = Form(None)
):
    if image is None and (name is None or name.strip() == ""):
        raise HTTPException(400, "Provide either image or non-empty name")
    return {"received": "ok", "type": "image" if image else "name"}