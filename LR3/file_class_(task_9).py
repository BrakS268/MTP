import json
from typing import Dict, Any


class FileManager:
    def __init__(self, filename: str):
        self.filename = filename

    def write_text(self, text: str):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(text)

    def read_text(self) -> str:
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()

    def append_text(self, text: str):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(text)

    def write_json(self, data: Dict[str, Any]):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def read_json(self) -> Dict[str, Any]:
        with open(self.filename, 'r', encoding='utf-8') as file:
            return json.load(file)


if __name__ == "__main__":

    file_manager = FileManager("example.txt")

    file_manager.write_text("Первая строка текста.\n")
    file_manager.append_text("Вторая строка текста.\n")

    content = file_manager.read_text()
    print("Содержимое текстового файла:")
    print(content)

    json_manager = FileManager("data.json")
    sample_data = {
        "users": [
            {"name": "Иван", "age": 25},
            {"name": "Мария", "age": 30}
        ]
    }
    json_manager.write_json(sample_data)

    loaded_data = json_manager.read_json()
    print("Данные из JSON файла:")
    print(loaded_data)
