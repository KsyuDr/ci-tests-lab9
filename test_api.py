"""Автотесты REST API JSONPlaceholder (повторяют тесты из Postman).
Запуск: python3 -m pytest -v test_api.py
"""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

USER_FIELDS = {"id", "name", "username", "email", "address", "phone", "website", "company"}


def test_get_user():
    """GET: получить пользователя с id = 1."""
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)

    # статус и формат ответа
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert response.elapsed.total_seconds() < 3

    user = response.json()

    # структура JSON
    assert set(user.keys()) == USER_FIELDS
    assert "city" in user["address"]
    assert "name" in user["company"]

    # типы полей
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["address"], dict)

    # значения полей
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["username"] == "Bret"
    assert "@" in user["email"]


def test_create_user():
    """POST: создать пользователя."""
    new_user = {
        "name": "Ksenia Drozd",
        "username": "kdrozd",
        "email": "ksenia.drozd@mail.ru",
        "phone": "+7 916 123-45-67",
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user, timeout=10)

    assert response.status_code == 201

    user = response.json()
    assert user["id"] == 11  # JSONPlaceholder выдаёт новому пользователю id = 11
    for field, value in new_user.items():
        assert user[field] == value


def test_update_user():
    """PUT: обновить пользователя с id = 1."""
    updated_user = {
        "id": 1,
        "name": "Ksenia Drozd (updated)",
        "username": "kdrozd_new",
        "email": "ksenia.new@mail.ru",
    }
    response = requests.put(f"{BASE_URL}/users/1", json=updated_user, timeout=10)

    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 1
    assert user["name"] == updated_user["name"]
    assert user["username"] == updated_user["username"]
    assert user["email"] == updated_user["email"]


def test_get_not_existing_user():
    """GET: запрос несуществующего пользователя возвращает 404."""
    response = requests.get(f"{BASE_URL}/users/999", timeout=10)

    assert response.status_code == 404
    assert response.json() == {}
