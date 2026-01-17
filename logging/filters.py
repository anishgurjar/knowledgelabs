import logging
import os


class DevelopmentFilter(logging.Filter):
    """
    Filter that only allows logs when APP_ENV is 'development'.
    Allows DEBUG and above in development mode.
    """
    
    def filter(self, record):
        app_env = os.getenv("APP_ENV", "production").lower()
        return app_env == "development"


class ProductionFilter(logging.Filter):
    """
    Filter that only allows logs when APP_ENV is NOT 'development'.
    Only allows WARNING and above in production mode.
    """
    
    def filter(self, record):
        app_env = os.getenv("APP_ENV", "production").lower()
        if app_env == "development":
            return False
        # In production, only allow WARNING and above
        return record.levelno >= logging.WARNING
