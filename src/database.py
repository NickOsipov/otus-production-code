"""
Module: database.py
Description: This module is responsible for creating the connection to the database.
"""

import os

from sqlalchemy import create_engine

# conn_str = 'mysql+pymysql://root:password@db-mysql-test:3306/machine_learning'
conn_str = os.getenv("DATABASE_URL")

engine = create_engine(conn_str)
