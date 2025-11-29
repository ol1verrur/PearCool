## Как запустить сайт (нужен git и python)
### Клонируем репозиторий через git bash
```
git clone https://github.com/ol1verrur/PearCool
```
### Внутри папки PearCool запускаем windows powershell
```
py -m venv .venv
.\venv\Scripts\activate.ps1
pip install uvicorn fastapi jinja2
```
### Запуск сайта через powershell (из папки проекта) 
```
uvicorn main:app
```
Ссылкой будет http://127.0.0.1:8000