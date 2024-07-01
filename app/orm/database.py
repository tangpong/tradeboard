from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from settings import settings
from models import Base

engine = create_async_engine(
    settings.db_url, echo=settings.db_echo
)

session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)


async def get_session():
    async with session_factory() as session:
        try:
            yield session
        finally:
            await session.close()


async def prepare_database():
    async with engine.begin() as connection:
        print(f"{connection=}")
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
