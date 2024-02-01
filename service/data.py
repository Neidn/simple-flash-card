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
        # and remove it from the dataframe
        self.remove_word(random_word)

        # Add the word to the used words list
        self.used_words.append(random_word)

        print(len(self.data))

        # Check if all words have been used
        if len(self.used_words) == len(self.data):
            self.used_words = []

        return random_word

    def remove_word(self, word):
        self.data = self.data[self.data.French != word['French']]

        # save the dataframe to the csv file
        self.data.to_csv(self.file_path, index=False)
        return self.data
