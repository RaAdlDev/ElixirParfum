from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from routers import auth

app = FastAPI()
app.include_router(auth.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.exception_handler(RequestValidationError)
async def validation_exception(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": True, "detail": "Bad request. Please check the input data."})

@app.exception_handler(HTTPException)
async def http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": True, "detail": exc.detail})


@app.exception_handler(Exception)
async def exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code= 500,
        content={"error": True, "detail" : "An unexpected error occurred."})

