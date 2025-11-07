from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String


## creating metadata
metadata = MetaData()


## Creating using Table
## import Metadata, table and Columns
users = Table(
  "users",
  metadata,
  Column("id", Integer, primary_key=True),
  Column("name", String(length=50), nullable=False),
  Column("email", String, nullable=False, unique=True),
)


## Craeting Table in Database
# method 1.
# metadata.create_all(engine)
def create_tables():
  metadata.create_all(engine)

# ## Delete Table in Database
# def drop_table():
#   metadata.create_all(engine)
  