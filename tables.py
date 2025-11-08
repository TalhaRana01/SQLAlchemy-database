from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey


## creating metadata
metadata = MetaData()


## Creating using Table
## import Metadata, table and Columns
# User table
users = Table(
  "users",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("name", String(length=50), nullable=False),
  Column("email", String, nullable=False, unique=True),
  Column("phone", Integer, nullable=False, unique=True),
  
)

# relationship one to many users and post
posts = Table(
  "posts",
  metadata,
   Column("id", Integer, primary_key=True),
   Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True),
   Column("title", String, nullable=False),
   Column("content", String, nullable=False),
)


##---------------------------
## Table as a practice
##---------------------------

# address = Table(
#   "address",
#   metadata,
#   Column("id", Integer, primary_key=True),
#   Column("street", String(length=50), nullable=False),
#   Column("dist", String, nullable=False, unique=True),
#   Column("country", String, nullable=False, unique=True),
# )


## Craeting Table in Database
# method 1.
# metadata.create_all(engine)
def create_tables():
  metadata.create_all(engine)

# ## Delete Table in Database
# def drop_table():
#   metadata.create_all(engine)
  