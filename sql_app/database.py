# import
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# create data base url for the sqlalchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# if using pstgresql


# create the sqlalchemy engine, the argument only for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False}
    )


# create a sessionlocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# create a base class
Base = declarative_base()
