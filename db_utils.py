import streamlit as st
import pandas as pd
import os
import sqlalchemy
from sqlalchemy import create_engine, text

from logger import Logger
logger = Logger.get_logger(__name__)

def get_current_db_path():
    """Return the current database path stored in session state"""
    # Default database if not already set
    if "db_path" not in st.session_state:
        st.session_state.db_path = "enterprise_database.sqlite"
        logger.info(f"Database path set to default: {st.session_state.db_path}")
    return st.session_state.db_path

def get_database_connection():
    """Create a database connection"""
    try:
        db_path = get_current_db_path()
        if not os.path.exists(db_path):
            st.error(f"Database file not found: {db_path}")
            logger.error(f"Database file not found: {db_path}")
            return None

        engine = create_engine(f"sqlite:///{db_path}")
        logger.info(f"Connected to database: {db_path}")
        return engine
    except Exception as e:
        st.error(f"Error connecting to database: {str(e)}")
        logger.error(f"Error connecting to database: {str(e)}")
        return None


def get_all_table_names():
    engine = get_database_connection()
    if engine is None:
        return []
    try:
        inspector = sqlalchemy.inspect(engine)
        tables = inspector.get_table_names()
        logger.info(f"Available tables: {tables}")
        return tables
    except Exception as e:
        st.error(f"Error fetching table names: {str(e)}")
        logger.error(f"Error fetching table names: {str(e)}")
        return []

def get_table_data(table_name):
    """Fetch all rows from the specified table"""
    engine = get_database_connection()
    if engine is None:
        logger.error("Database connection failed in get_table_data()")
        return None

    try:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, engine)
        logger.info(f"Fetched {len(df)} rows from table '{table_name}'")
        return df
    except Exception as e:
        logger.error(f"Error fetching data from '{table_name}': {str(e)}")
        st.error(f"Error fetching data: {str(e)}")
        return None

