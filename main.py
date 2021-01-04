from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
from starlette.responses import JSONResponse
import uvicorn
from starlette.routing import Mount
from conversions import convert_currency


routes = [
    Route('/convert', convert_currency,methods=['POST']),

]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)