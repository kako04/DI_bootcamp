def wordSequence(words):
    splitted = words.split(",")
    sorted_words = sorted(splitted)
    finished = ",".join(sorted_words)
    return finished
print(wordSequence("without,hello,bag,world"))
