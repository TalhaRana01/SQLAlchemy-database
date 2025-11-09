from tables import create_tables
from services import create_user, create_post, get_user_by_id, get_all_users, get_post_by_user



# Craete Tables by calling createTables from tables.py
create_tables()

# Create User in User Table in DATABASE

# create_user("Talha Rana", "taharana01@gmail.com")
# create_user("Ali Rana", "This is a Ali Rana")

# Create Post in Post Table in DATABASE
# create_post(1, "Talha Rana AI Engineer", "This is a Talha Rana AL ML Engineer")
create_post(2, "Ali ahmed", "This is a businessmen")
# create_post(3, "Ahsan", "Hi Ahsan how are you")

# Read single user data
# print(get_user_by_id(1))

# Read all users
# print(get_all_users())


# Get Post by User

# print(get_post_by_user(3))
