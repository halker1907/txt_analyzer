﻿from typing import NoReturn
from string import punctuation
import re
import pymorphy3


"""
скачать текст
загрузить ТХТ файл
ТОП 10/20 глаголов/существительных/прилагательных в этом тексте
создать картинку - облако слов
"""

class TextAnalyzer:
    def __init__(self, file_name="text.txt", mode="r", encoding="UTF-8", pos_list=["VERB", "NOUN"]) -> None:
        if file_name is None:
            raise Exception("Не указан файл для анализа!")
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.pos_list = pos_list
        self.read_file()
        self.check_empty_file()
        self.prepare_text()
        self.sorting_words()
        self.print_text()

    def read_file(self) -> None | NoReturn:
        """ Пытается открыть файл и считать его в строку """
        try:
            with open(self.file_name, self.mode, encoding=self.encoding) as file:
                self.content = file
                self.text = self.content.read()
        except FileNotFoundError:
            raise Exception(f"Файл {self.file_name} не найден!")

    def check_empty_file(self) -> None | NoReturn:
        """ проверяет пустой ли файл """
        if not self.text:
            raise RuntimeError(f"Файл {self.file_name} пустой!")

    def prepare_text(self):
        """ Приводит текст к нижнему регистру и убирает все лишние знаки препинания """
        self.text = self.text.lower()
        self.words = re.findall(r'\b[\w-]+\b', self.text)

    def sorting_words(self) -> list:
        morph = pymorphy3.MorphAnalyzer()
        self.words_by_pos = []

        for word in self.words:
            parsed_word = morph.parse(word)[0]
            pos = parsed_word.tag.POS
            if pos in self.pos_list:
                self.words_by_pos.append(parsed_word.normal_form)

    def print_text(self) -> None:
        """ Выводит строку текста на экран """
        print(self.words_by_pos)

TextAnalyzer(file_name = “text.txt”)
