#!/usr/bin/env python3

class MyString:
    '''A class that represents a string and provides methods to analyze its content.'''

    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        '''Returns True if the string ends with a period.'''
        return self.value.endswith('.')

    def is_question(self):
        '''Returns True if the string ends with a question mark.'''
        return self.value.endswith('?')

    def is_exclamation(self):
        '''Returns True if the string ends with an exclamation mark.'''
        return self.value.endswith('!')

    def count_sentences(self):
        '''Returns the number of sentences in the string.'''
        import re
        sentences = re.findall(r'[^.!?]+[.!?]+', self.value)
        return len(sentences)
  
