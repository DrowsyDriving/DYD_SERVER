data = {
    'user': 'root',
    'password': 'server',
    'host': '127.0.0.1',
    'port': '3307',
    'database': 'dyd'
}

DB_URL = f"mysql+mysqlconnector://{data['user']}:{data['password']}@{data['host']}:{data['port']}/{data['database']}?charset=utf8"
