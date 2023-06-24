import re


class TextAnalyze:
    def __init__(self, file_name=None):
        if file_name is None:
            raise Exception("Не указан файл для анализа!")
        self.read_file(file_name)
        self.check_empty_text()
        self.prepare_text()
        self.print_text()

    def read_file(self, file_name):
        """ пытается открыть файл и считать его в строку """
        try:
            with open(file_name, "r", encoding="UTF-8") as content:
                self.file = content  # здесь получается файловый объект
                self.text = self.file.read()  # здесь получается строка текста
        except FileNotFoundError:
            raise Exception(f"Файл {file_name} не найден!")

    def check_empty_text(self):
        if not self.text:
            raise RuntimeError(f"Файл {self.file} пуст, попробуйте другой файл")

    def prepare_text(self):
        self.text = self.text.lower()
        self.clean_text = ''.join(re.findall(r'[\w\s-]', self.text))
        self.words = self.text.split()
        
    def print_text(self):
        """ выводит строку текста на экран """
        print(self.clean_text)
        print(f"В этом тексте {len(self.words)} слов")


TextAnalyze(file_name="text.txt")
