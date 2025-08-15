from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from .image_service import generate_image

app = FastAPI()

# Static files & templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=BASE_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "image_path": None})

@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, prompt: str = Form(...)):
    try:
        image_path = os.path.join(BASE_DIR, "generated_image.png")
        generate_image(prompt, output_file=image_path)
        return templates.TemplateResponse("index.html", {"request": request, "image_path": "static/generated_image.png"})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "error": str(e), "image_path": None})
