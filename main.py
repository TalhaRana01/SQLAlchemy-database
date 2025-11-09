from tables import create_tables
from services import create_user, create_post, get_user_by_id, get_all_users, get_post_by_user, get_all_post, update_user_email, update_post_title



# Craete Tables by calling createTables from tables.py
create_tables()


##------------------------------------
# Create User in User Table in DATABASE
##------------------------------------
#  👥 USERS
# create_user("Talha Rana", "taharana01@gmail.com")
# create_user("Ali Rana", "This is a Ali Rana")



##------------------------------------
# Get User from User Table in DATABASE
##------------------------------------
# print(get_all_users())      # Get all users
# print(get_user_by_id(1))    # Get Single User  by ID


##------------------------------------
# Update User from User Table in DATABASE
##------------------------------------
# update_user_email(1, "example@gmail.com")

##------------------------------------
# Create Post in Post Table in DATABASE
##------------------------------------
# create_post(2, "Ali ahmed", "This is a businessmen")
# create_post(3, "Ahsan", "Hi Ahsan how are you")


##------------------------------------
# Get Post in Post Table in DATABASE
##------------------------------------
# print(get_all_post())         # Get All Posts
# print(get_post_by_user(3))  # Get post by User ID


update_post_title(1, "This is new updated title")











