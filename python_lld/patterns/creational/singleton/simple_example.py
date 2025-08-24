import datetime

class Logger:

    _instance = None
    _initialized = None
    _logfile = None 

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, filepath="main.log"):
        if not Logger._initialized:
            self._logfile = filepath
            with open(self._logfile, "a") as f:
                f.write("\n=== Logging Started===\n")
            Logger._initialized = True
        # if initialized don't do anything
    
    def log(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self._logfile, "a") as f:
            f.write(f"[{timestamp}] {message} \n")

logger = Logger("mylog.txt")
logger.log("First message")

logger2 = Logger("a.txt")
logger2.log("second message")

