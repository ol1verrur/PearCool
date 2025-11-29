# main.py (Очищенная версия)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import os

# from random import random # Импорт random больше не используется

# Инициализация списка answers и файла pickle, если они нужны для других маршрутов
if os.path.exists('answers.txt'):
    answers = pickle.load(open('answers.txt', 'rb'))
else:
    # Оставляем инициализацию, чтобы избежать ошибок, даже если answers пока пуст
    answers = []

app = FastAPI()

# Монтируем статические файлы из папки "html"
# Примечание: Обычно статику (CSS/JS/Images) монтируют из папки "static",
# но в вашем коде используется "html" как для шаблонов, так и для статики.
# Если вы используете url_for('static', path='...') в HTML, этот app.mount должен быть правильным.
app.mount("/html", StaticFiles(directory="html"), name="static")

# Указываем Jinja2 искать шаблоны в папке "html"
templates = Jinja2Templates(directory="html")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return (templates.TemplateResponse("12345.html", context={"request": request, "my_first_header": "42"}))


@app.get("/summarise/{a}/{b}")
async def summarise(a: int, b: int):
    return {"answer": str(a + b)}


@app.post("/sendForm")
async def send_form(request: Request):
    form = await request.form()
    data_from_from = dict(form.items())

    answers.append(data_from_from)
    pickle.dump(answers, open('answers.txt', 'wb'))

    # После сохранения данных формы, обычно пользователя перенаправляют или
    # возвращают ответ. Ваш исходный код просто заканчивал выполнение функции.
    # FastAPI по умолчанию вернет 200 OK.


# НОВЫЙ МАРШРУТ ДЛЯ ОТВЕТОВ (на верхнем уровне)
@app.get("/answers")
async def get_answers(request: Request):
    return templates.TemplateResponse(
        "answers.html",
        context={"request": request, "data_items": answers}
    )


@app.get('/shulte')
async def shulte(request: Request):
    return templates.TemplateResponse("shulte.html", context=
    {"request": request})


@app.get('/auth')
async def html(request: Request):
    return templates.TemplateResponse("index.html", context=
    {"request": request})


@app.get('/shulteAD')
async def shulte(request: Request):
    return templates.TemplateResponse("shulteAD.html", context=
    {"request": request})


# Ваш целевой маршрут для Samosvet, который теперь правильно расположен
@app.get('/Samosvet')
async def samosvet(request: Request):
    return templates.TemplateResponse("Samosvet.html", context=
    {"request": request})


@app.middleware("http")
async def add_cache_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.get('/shulte_results')
async def shulte_results(request: Request):
    # Эта функция будет рендерить новую страницу с результатами
    return templates.TemplateResponse("shulte_results.html", context=
    {"request": request})