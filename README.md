# Клонируем репозиторий
```
git clone https://github.com/MikhalchenkoD/stepik_selenium_2.git
```
# Активация виртуального окружения (Для Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```
# Активация виртуального окружения (Для Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```
# Установка зависимостей
```bash
cd stepik_selenium_2
pip install -r requirements.txt
```

# Запуск теста (Windows)
```bash
python test.py
```

# Запуск теста (Linux)
```bash
python3 test.py
```