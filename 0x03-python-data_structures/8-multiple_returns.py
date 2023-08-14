#!/usr/bin/python3
def multiple_returns(sentence):
    len_of_sentence = len(sentence[:])
    first_char = sentence[0]
    if len_of_sentence == 0:
        return 0, None
    return len_of_sentence, first_char
