from service import process_user

def handler(user_id):
    result = process_user(user_id)
    return {"status": "ok", "data": result}

if __name__ == "__main__":
    response = handler(42)
    print(response)
