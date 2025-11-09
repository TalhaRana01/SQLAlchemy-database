from sqlalchemy import create_engine

#  db.py sy DATABASE connection bane ga
DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(DATABASE_URL, echo=True)
