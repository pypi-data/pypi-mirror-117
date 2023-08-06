from fastapi import *
from fastapi.responses import *

app = FastAPI()


@app.middleware('http')
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except TypeError as ex:
        return JSONResponse(status_code=500, content=dict(detail=str(ex)))
