import requests
import json  # Для форматирования JSON

# Отправляем GET-запрос к API GitHub с параметром поиска
url = "https://api.github.com"
params = {"q": "language:html"}  # Параметр для поиска репозиториев с кодом HTML

# Выполняем запрос
response = requests.get(url, params=params)

# Печатаем статус-код ответа
print("Status Code:", response.status_code)

# Печатаем содержимое ответа в формате JSON
try:
    json_data = response.json()  # Преобразуем ответ в JSON
    formatted_json = json.dumps(json_data, indent=4)  # Преобразуем в читаемый формат
    print("Response JSON:")
    print(formatted_json)
except Exception as e:
    print("Error parsing JSON:", e)
