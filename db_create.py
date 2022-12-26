from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

# create a database which use the MySQL
link = create_engine('mysql+pymysql://root:123456@localhost:3306/Canteen_System')
if not database_exists(link.url):
    create_database(link.url)
    print("Success to create a database!")
else:
    print("The database is existed!")