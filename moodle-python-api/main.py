"""
Moodle Python API — FastAPI application entry point.

Phase 0 deliverable: running service with /health endpoint.
Nginx proxy routes covered Moodle web service functions here;
all others continue to PHP-FPM until each phase is complete.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.auth.router import router as auth_router
from app.courses.router import router as courses_router
from app.users.router import router as users_router
from core.config import get_settings
from core.db.session import engine
from core.logging import configure_logging

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    # Verify DB connectivity on startup
    async with engine.connect() as conn:
        await conn.execute(__import__("sqlalchemy").text("SELECT 1"))
    yield
    await engine.dispose()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tighten per-environment in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prometheus metrics at /metrics
Instrumentator().instrument(app).expose(app)

# Routers
app.include_router(auth_router,    prefix="/api/v1")
app.include_router(users_router,   prefix="/api/v1")
app.include_router(courses_router, prefix="/api/v1")


@app.get("/health", tags=["ops"])
async def health():
    """Liveness probe — used by Nginx, Docker, and k8s."""
    return {
        "status": "ok",
        "version": settings.app_version,
        "environment": settings.environment,
    }


@app.get("/api/v1/site/info", tags=["webservice"])
async def site_info():
    """
    Mirrors core_webservice_get_site_info.
    Stub — full implementation in MTP-58.
    """
    return {
        "sitename": settings.app_name,
        "siteurl": "",
        "release": settings.app_version,
        "functions": [],
    }
