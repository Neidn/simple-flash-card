# Parse csv file and return a dataframe
# Path: service/data.py

import pandas


class WordData:

    def __init__(self, file_path):
        self.used_words = []
        self.file_path = file_path
        self.data = pandas.read_csv(self.file_path)

    def get_data(self):
        return self.data

    def get_random_word(self):
        word = self.data.sample()

        random_word = {
            'French': word['French'].values[0],
            'English': word['English'].values[0]
        }

        # Check if the word has been used before
        while random_word['French'] in self.used_words:
            random_word = self.data.sample()

        # Add the word to the used words list
        self.used_words.append(random_word)

        # Check if all words have been used
        if len(self.used_words) == len(self.data):
            self.used_words = []

        return random_word
