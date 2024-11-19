import requests

# URL для запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры
params = {"userId": 1}

try:
    # Отправка GET-запроса
    response = requests.get(url, params=params)
    response.raise_for_status()  # Проверка HTTP-ошибок

    # Обработка ответа
    posts = response.json()
    for post in posts:
        print(f"ID: {post['id']}")
        print(f"Заголовок: {post['title']}")
        print(f"Содержание: {post['body']}")
        print("-" * 50)

except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")
