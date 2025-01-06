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
    
# Добавила исключения для обработки ошибок при чтении файла.


    def write_file(self,filepath: str, *data: str) -> None:
        """Метод для записи данных в файл"""
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                for line in data:
                    file.write(line + '\n')
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")

handler =  TxtFileHandler()

content = handler.read_file("test.txt")
print(content)
handler.write_file("test.txt", "This is a test string.\n")