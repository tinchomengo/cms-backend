import os
import sys

# Insert the project root directory into sys.path
# __file__ is the path to env.py. 
# os.path.dirname(__file__) is the 'alembic' folder. 
# We go one level up to reach 'cms-backend'.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv
from app.database import Base  # Import your Base
from app.models import *

load_dotenv()
config = context.config

# Override sqlalchemy.url from .env
db_url = os.getenv('DATABASE_URL_DEV')
config.set_main_option('sqlalchemy.url', db_url)

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Set target_metadata to your models' metadata
target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
