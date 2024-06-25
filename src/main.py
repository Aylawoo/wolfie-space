from sanic import Sanic, request
from sanic.response import text

app = Sanic("wolfie-space")
app.extend(config={
        "templating_path_to_templates": "html/"
    }
)
app.static("static/", "static/")

@app.get("/")
@app.ext.template("home.html")
async def home(req: request) -> dict:
    return {}
