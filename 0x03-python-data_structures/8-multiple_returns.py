#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        sen_len = len(sentence)
    if not sentence:
        sentence = none
    else:
        sen_len = 0
    return (sen_len, sentence if not sentence else sentence[:1])

