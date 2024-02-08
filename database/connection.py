from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db = {
    'user': 'root',
    'password': 'server',
    'host': '127.0.0.1',
    'port': '3307',
    'database': 'dyd'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

engine = create_engine(DB_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
