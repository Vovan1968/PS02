import requests

# URL для отправки данных
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для отправки
data = {
    "name": "Vovan",
    "email": "vovan@yandex.ru",
    "age": 30,
    "location": "New York",
    }

# Отправка POST-запроса
response = requests.post(url, json=data)

# Вывод ответа
print("Статус-код:", response.status_code)
print("Ответ:", response.text)
