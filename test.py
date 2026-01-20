word_count = {}
with open("input.txt", "r") as rf, open("output.txt", "w") as wf:
    words = rf.read().split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        wf.write(f"{word}:{count}\n")
