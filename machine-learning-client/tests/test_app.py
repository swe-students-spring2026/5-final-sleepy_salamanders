import pytest
from unittest.mock import patch, MagicMock
from src.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("src.main.client.chat.completions.create")
def test_get_priority_score(mock_openai, client):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "7"
    mock_openai.return_value = mock_response

    response = client.post(
        "/api/get_priority_score",
        json={
            "task_description": "Finish homework",
            "task_days_to_complete": 3,
        },
    )

    assert response.status_code == 200
    assert response.get_json() == {"score": 7}
