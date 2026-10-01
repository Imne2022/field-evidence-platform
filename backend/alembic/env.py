from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app.core.config import settings
from app.core.database import Base
from app import models  # noqa: F401


# Alembic Config object
config = context.config


# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Set database URL from application settings.
config.set_main_option(
    "sqlalchemy.url",
    settings.database_url,
)


# SQLAlchemy metadata used by Alembic autogenerate.
target_metadata = Base.metadata


# PostGIS / extension-managed tables that Alembic must not modify.
EXCLUDED_TABLES = {
    "spatial_ref_sys",
    "geography_columns",
    "geometry_columns",
    "raster_columns",
    "raster_overviews",
    "topology",
    "layer",
}


def include_object(object, name, type_, reflected, compare_to):
    """Exclude extension-managed tables from Alembic autogenerate."""
    if type_ == "table" and reflected and name in EXCLUDED_TABLES:
        return False

    return True


def run_migrations_offline() -> None:
    """Run migrations in offline mode."""

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in online mode."""

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()