def get_n_longest_unique_words(words, n):
    unique_words = []
    for word in words:
        # append word to list if is the 1st time it appears
        if word not in unique_words:
            unique_words.append(word)
        # remove the word from unique words list if it appears again. It was not truly unique
        else:
            unique_words.remove(word)
    
    sorted_words = sorted(unique_words, key= lambda w : len(w), reverse=True)
    return sorted_words[:n]


# words = ["Longer", "Whatever", "Longer", "Ball", "Rock", "Rocky", "Rocky"]
# n = 3
# expected = ["Whatever", "Ball", "Rock"]

# words = ["Longer", "Whatever", "Longer", "Ball", "Rock", "Rocky", "Rocky"]
# n = 1
# expected = ["Whatever"]

# words = ["Longer", "Whatever", "Longer", "Ball", "Rock", "Rocky", "Rocky"]
# n = 0
# expected = []

# words = ["Hello", "AlgoExpert", "Algo", "Testing", "Programming", "Programming", "Coding",
#     "Python", "JavaScript", "Coding", "Ruby"]
# n = 5
# expected = ["AlgoExpert", "JavaScript", "Testing", "Python", "Hello"]