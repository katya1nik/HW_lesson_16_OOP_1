
class TxtFileHandler:
    """Создала класс для работы с файлом"""
    def read_file(self, filepath: str) -> str:
        """Метод для чтения файла, возвращает содержимое (строку)"""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return ""
handler =  TxtFileHandler()    
# Добавила исключения для обработки ошибок при чтении файла.
content = handler.read_file("test.txt")
print(content)
