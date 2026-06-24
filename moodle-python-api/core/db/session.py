"""
Async SQLAlchemy engine and session factory.
Connects to the existing Moodle database (read-write).
Table names keep the mdl_ prefix until Phase 8.
"""
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from core.config import get_settings

settings = get_settings()

_is_sqlite = settings.database_url.startswith("sqlite")
engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    **({} if _is_sqlite else {
        "pool_size": settings.db_pool_size,
        "max_overflow": settings.db_max_overflow,
        "pool_pre_ping": True,
    })
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency — yields a DB session and closes it after the request."""
    async with AsyncSessionLocal() as session:
        yield session
