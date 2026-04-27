def test_root_hello_world(client) -> None:
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, world!"}

