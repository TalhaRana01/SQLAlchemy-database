from db import engine
from tables import users, posts    # import users and post from tables file
from sqlalchemy import insert, select, update, delete





# Insert Or Create User
# def create_user(name: str, email:str):
#   with engine.connect() as conn:
#     stmt = insert(users).values(name=name, email=email)
#     conn.execute(stmt)
#     conn.commit()
    
# Insert or create post 
# def create_post(user_id: int, title:str, content: str):
#   with engine.connect() as conn:
#     stmt = insert(posts).values(user_id=user_id, title=title, content=content)
#     conn.execute(stmt)
#     conn.commit()
