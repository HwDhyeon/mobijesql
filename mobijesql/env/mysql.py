import os
import dotenv


dotenv.load_dotenv()


host = os.getenv('MYSQL_HOST', '127.0.0.1')
port = os.getenv('MYSQL_PORT', 3306)
user = os.getenv('MYSQL_USER', 'root')
password = os.getenv('MYSQL_PASSWORD', 'rootpassword')
db = os.getenv('MYSQL_DB', 'mysql')
