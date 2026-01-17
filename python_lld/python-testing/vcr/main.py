import requests


def get_user_profile(user_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def get_articles() -> dict:
    url = "https://api.capacity.com/v1/articles?page=1&limit=1000"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer 848ed846-d60b-401d-a340-5c7f0e5ef136",
        "x-capacity-id": "ab13142e-81db-4b67-8592-87e0ba3bbc23",
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    
    data = get_articles()
    print(data)
