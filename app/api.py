import logging
from fastapi import FastAPI, HTTPException, Header
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


from app import models

logger = logging.getLogger(__name__)

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates/static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def add_context(context: models.CreateContext, x_auth_key: str = Header(None)):
    """
    Add or update a context with the given context key
    """

    logger.info("Auth Key : %s", x_auth_key)
    logger.info("Context : %s", context)

    if config.DEV_PASSWORD != x_auth_key:
        raise HTTPException(status_code=403, detail="Unauthorized")

    context_key = context.context_key
    new_context = context.new_context

    contexts[context_key] = new_context

    return "Context Changed Successfully"


@app.post("/")
def graph():
    return templates.TemplateResponse(
        ("graph.html"),
        {userName: selected_File, corrValue: result.toString(), userNameImage: Image},
    )
