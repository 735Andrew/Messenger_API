from httpx import AsyncClient
import pytest

from conftest import ac


@pytest.mark.parametrize(
    "input_data,code,title",
    [
        ("    Frontend  ", 201, "Frontend"),
        pytest.param("", 422, "Chat", marks=pytest.mark.xfail),
    ],
)
async def test_chat_create(input_data, code, title, ac: AsyncClient):
    response = await ac.post("/chats", json={"title": input_data})
    assert response.status_code == code
    assert response.json()["title"] == title


@pytest.mark.parametrize(
    "id,input_data,code,message_id,chat_id,",
    [
        (2, "I’ve updated the sprint board — please review your tasks", 201, 6, 2),
        pytest.param(1, "", 201, 7, 1, marks=pytest.mark.xfail),
        pytest.param(100, "Chill", 201, 7, 100, marks=pytest.mark.xfail),
    ],
)
async def test_send_message(id, input_data, code, message_id, chat_id, ac: AsyncClient):
    response = await ac.post(f"/chats/{id}/messages", json={"text": input_data})
    assert response.status_code == code
    assert response.json()["id"] == message_id
    assert response.json()["chat_id"] == chat_id
