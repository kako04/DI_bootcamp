class AnagramChecker:
    def __init__(self, word_list_file):
        with open(word_list_file, 'r') as f:
            self.words = set(word.strip().lower() for word in f)

    def is_valid_word(self, word):
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        anagrams = []
        for w in self.words:
            if self.is_anagram(word, w) and word.lower() != w.lower():
                anagrams.append(w)
        return anagrams
