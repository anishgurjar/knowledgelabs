class Database:
    
    _instance = None
    _connString: str
    _initialized = None
    _connected = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, connectionString: str):
        if not Database._initialized:
            self._connString = connectionString
            Database._initialized = True

    def connect(self) -> None:
        print(f"Connected to {self._connString}")
        self._connected = True

    def disconnect(self) -> None:
        print(f"Disconnected from {self._connString}")
        self._connected = False

    def status(self) -> bool:
        return self._connected
    
db = Database("postgresql://localhost:5432/mydb")
print(db.status())
db.connect()
print(db.status())
db.disconnect()
print(db.status())

db = Database("postgresql://localhost:5432/somenewrandomdb")
print(db.status())
db.connect()
print(db.status())
db.disconnect()
print(db.status())