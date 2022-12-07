#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    if len_s < 1:
        return (len_s, None)
    return (len_s, sentence[0])
