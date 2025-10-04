import pytest
from UserManager.main import UserManager

@pytest.fixture
def user_manager():
    """Create a fesh instance of UserManager before each test"""
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("anish", "agurjar@lower.com") == True
    assert user_manager.add_user("ajay", "ajay.gurjar@yaskawa.in") == True

def test_add_duplicate_user(user_manager):
    user_manager.add_user("anish", "agurjar@lower.com")
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_user("anish", "agurjar@lower.com")

