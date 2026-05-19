from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def docs_home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )
