from repo import get_user_from_db
from utils import format_user

def process_user(user_id):
    user = get_user_from_db(user_id)
    if not user:
        raise ValueError("User not found")

    formatted = format_user(user)
    return formatted
