from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
from starlette.responses import JSONResponse
import uvicorn
from starlette.routing import Mount
from conversions.tasks import convert_currency
from starlette.schemas import SchemaGenerator


schemas = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Example API", "version": "1.0"}}
)



routes = [
    Route('/convert', convert_currency,methods=['POST']),

]


app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)