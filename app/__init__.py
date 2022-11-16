from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from logging import config as LogConfig
import os
from core.config import config
from core.exceptions import CustomException
from core.fastapi.dependencies import Logging
from api import router

log_path = os.getcwd()
LogConfig.fileConfig(
    'logging.conf',
    disable_existing_loggers=False,
    defaults={'logfilename': f"{log_path}/app.log"}
)


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routers(app: FastAPI) -> None:
    app.include_router(router)


def init_listeners(app: FastAPI) -> None:
    # Exception handler
    @app.exception_handler(CustomException)
    async def custom_exception_handler(
        request: Request, exc: CustomException
    ):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def on_auth_error(request: Request, exc: Exception):
    status_code, error_code, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content={"error_code": error_code, "message": message},
    )


def init_middleware(app: FastAPI) -> None:
    pass


def create_app() -> FastAPI:
    app = FastAPI(
        title="Crypto Markets",
        description="Crypto Markets API to view the " +
                    "Crypto market currency updates",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        dependencies=[Depends(Logging)],
    )
    init_routers(app=app)
    init_cors(app=app)
    init_listeners(app=app)
    init_middleware(app=app)
    return app


app = create_app()
