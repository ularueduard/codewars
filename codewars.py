
"""
def spin_words(sentence):
    reversed_list = []
    sentence_list = sentence.split(' ')
    for word in sentence_list:
        if len(word) >= 4:
            reversed_list.append(word[::-1])
        else:
            reversed_list.append(word)
            return " ".join(word for word in reversed_list)
"""


def spin_words(sentence):
    reversed_list = []
    sentence_list = sentence.split(' ')
    for word in sentence_list:
        if len(word) >= 4:
            reversed_list.append(word[::-1])
        else:
            reversed_list.append(word)
        print(sentence_list)


spin_words("declaseaza un fisier din staging")
