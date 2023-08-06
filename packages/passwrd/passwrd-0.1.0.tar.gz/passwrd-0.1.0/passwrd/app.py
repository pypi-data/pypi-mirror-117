from random import SystemRandom
from string import digits, punctuation


class Passwrd:
    def __init__(self, dictionary_file: str) -> None:
        self.rng = SystemRandom()
        self.dictionary = self.__get_words_list(dictionary_file)
        self.symbols = list(digits + punctuation)

    @staticmethod
    def __get_words_list(dictionary_path: str) -> list:
        with open(dictionary_path, "r") as f:
            dictionary = f.read()

        return dictionary.splitlines()

    @property
    def random_word(self) -> str:
        return self.dictionary[self.rng.randint(0, len(self.dictionary))]

    @property
    def random_symbol(self) -> str:
        return self.symbols[self.rng.randint(0, len(self.symbols))]

    def gen_password(self, min_length: int) -> str:
        password = ""
        while len(password) < min_length:
            password += self.random_word + self.random_symbol

        return password
