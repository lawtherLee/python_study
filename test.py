def find_words_by_group(words):
    row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
    res = []
    for word in words:
        lower_word = word.lower()
        first_c = lower_word[0]

        if first_c in row1:
            target = row1
        elif first_c in row2:
            target = row2
        else:
            target = row3

        is_all_in = all(c in target for c in lower_word)

        if is_all_in:
            res.append(word)
    return res


print(find_words_by_group(["Hello", "Alaska", "Dad", "Peace"]))
