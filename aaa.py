from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import os

if os.path.exists('answers.txt'):
    answer = pickle.load(open('answers.txt', 'rb'))
else:
    answer = []

app = FastAPI()
templates = Jinja2Templates(directory="HTML")
app.mount("/static", StaticFiles(directory="HTML"), name="static")

template = Jinja2Templates(directory="HTML")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return (template.TemplateResponse
        ("index.html", context=
        {"request": request, "my_first_header":42}))

@app.post("/SendForm")
async def send_form(request: Request):
    form = await request.form()
    data_from_form = dict(form.items())

    answer.append(data_from_form)
    pickle.dump(data_from_form, open('answers.txt', 'wb'))
@app.get("/answers")
async def read_answers(request: Request):

        return (template.TemplateResponse
                ("index.html", context=
                {"request": request, "data_items": answer}))

@app.get('/shulte')
async def shulte(request: Request):
    return template.TemplateResponse("shulte.html", context=
    {"request": request})
@app.get('/shulteAD')
async def shulte(request: Request):
    return template.TemplateResponse("shulteAD.html", context=
    {"request": request})

@app.middleware("http")
async def add_cache_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.get('/Samosvet')
async def samosvet(request: Request):
    return template.TemplateResponse("Samosvet.html", context=
    {"request": request})