## FastAPI Hello World (Docker)

### Запуск через Docker

Сборка образа:

```bash
docker build -t fastapi-hello .
```

Запуск контейнера:

```bash
docker run --rm -p 8000:8000 fastapi-hello
```

### Запуск через Docker Compose

```bash
docker compose up --build
```

Остановка:

```bash
docker compose down
```

Проверка:

- Откройте `http://localhost:8000/`
- Или:

```bash
curl http://localhost:8000/
```

