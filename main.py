from tables import create_tables
from services import create_user, create_post



# Craete Tables by calling createTables from tables.py
create_tables()

create_user("Talha Rana", "talharana01@gmail.com")

create_post(1, "Talha Rana AI Engineer", "This is a Talha Rana AL ML Engineer")