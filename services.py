from db import engine
from tables import users, posts    # import users and post from tables file
from sqlalchemy import insert, select, update, delete




# Create Users
def create_user(name: str, email:str):
  with engine.connect() as conn:
    stmt = insert(users).values(name=name, email=email)
    conn.execute(stmt)
    conn.commit()


# Get all Users
def get_all_users():
  with engine.connect() as conn:
    stmt = select(users)
    result = conn.execute(stmt).fetchall()
    return result
    
    
# Get single users 
def get_user_by_id(user_id: int):
  with engine.connect() as conn:
    stmt = select(users).where(users.c.id == user_id)
    result = conn.execute(stmt).first()
    return result


# Delete User
def delete_user(user_id: int):
  with engine.connect() as conn:
    stmt = delete(users).where(users.c.id == user_id)
    conn.execute(stmt)
    conn.commit()
    
  
# Update User Email
def update_user_email(user_id: int, new_email: str):
  with engine.connect() as conn:
    stmt = update(users).where(users.c.id == user_id).values(email=new_email)
    conn.execute(stmt)
    conn.commit()
    
  
# Create Post
def create_post(user_id: int, title:str, content: str):
  with engine.connect() as conn:
    stmt = insert(posts).values(user_id=user_id, title=title, content=content)
    conn.execute(stmt)
    conn.commit()


# Get All Posts
def get_all_post():
  with engine.connect() as conn:
    stmt = select(posts)
    result = conn.execute(stmt).fetchall()
    return result
  
  
# Get Post by User
def get_post_by_user(user_id: int):
  with engine.connect() as conn:
    stmt = select(posts).where(posts.c.user_id == user_id)
    result = conn.execute(stmt).fetchall()
    return result
   

# Update Post title
def update_post_title(post_id: int, update_title: str):
  with engine.connect() as conn:
    stmt = update(posts).where(posts.c.id == post_id).values(title=update_title)
    conn.execute(stmt)
    conn.commit()
    
    
# Delete Post
def delete_post(post_id: int):
  with engine.connect() as conn:
    stmt = delete(posts).where(posts.c.id == post_id)
    conn.execute(stmt)
    conn.commit()