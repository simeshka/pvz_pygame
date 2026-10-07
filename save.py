import json # превращает питоновские слова в текст и обратно
import os # модуль для сохранения пути к файлу
save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "save.json")
# __file__ переменная, которая отвечает за путь к файлу save.py на диске.
# os.path.abspath - превращает в полный путь от корня системы (/), от фразы "absolute path" - полный путь
# os.path.dirname - оставляет только название папки, и уберает имя файла
# os.path.join - склеивает папку и файл через /
data = {
    max_level: "1"
}