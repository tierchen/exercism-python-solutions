from collections import Counter


def detect_anagrams(word, candidates):
    result = []
    word = word.lower()
    letters = Counter(word)
    for candidate in candidates:
        if Counter(candidate.lower()) == letters and candidate.lower() != word:
            result.append(candidate)
    return result
