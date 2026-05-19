from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes.docs import router as docs_router
from app.routes.execute import router as execute_router
from app.routes.uploads import router as uploads_router
from app.routes.artifacts import router as artifacts_router


app = FastAPI(
    title="June Python Sandbox"
)

# static assets
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# templates
templates = Jinja2Templates(
    directory="app/templates"
)

# routers
app.include_router(docs_router)
app.include_router(execute_router)
app.include_router(uploads_router)
app.include_router(artifacts_router)
