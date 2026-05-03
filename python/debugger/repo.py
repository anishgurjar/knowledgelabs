def get_user_from_db(user_id):
    # simulate DB
    if user_id == 42:
        return {"id": 42, "name": "anish"}
    return None
