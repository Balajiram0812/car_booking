from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import status
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
from starlette.exceptions import HTTPException as StarletteHTTPException

# Handle HTTP errors (raised with HTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "message": exc.detail},
    )

# Handle validation errors (Pydantic schema)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"status": "fail", "errors": exc.errors()},
    )

# Handle DB errors (unique constraint, foreign key, etc.)
async def sqlalchemy_exception_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        # status_code=status.HTTP_400_BAD_REQUEST,
        content={"status":status.HTTP_400_BAD_REQUEST , "message": "Database integrity error"},
    )

# Handle unexpected errors
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"status": "error", "message": "Something went wrong, please try again later"},
    )
