def test_get_activities_returns_200_and_payload(client):
    # Arrange - fixture provides clean state
    # Act
    resp = client.get("/activities")
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert "Chess Club" in data


def test_signup_adds_participant(client):
    # Arrange
    email = "tester@example.com"
    activity = "Chess Club"
    # Act
    resp = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert resp.status_code == 200
    data = client.get("/activities").json()
    assert email in data[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    email = "dup@example.com"
    activity = "Chess Club"
    # Act
    resp1 = client.post(f"/activities/{activity}/signup?email={email}")
    resp2 = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert resp1.status_code == 200
    assert resp2.status_code == 400


def test_remove_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "removable@example.com"
    resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert resp.status_code == 200
    # Act
    del_resp = client.delete(f"/activities/{activity}/participants?email={email}")
    # Assert
    assert del_resp.status_code == 200
    data = client.get("/activities").json()
    assert email not in data[activity]["participants"]
