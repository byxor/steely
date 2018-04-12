def get_spoonerised(words):
    starts, ends = [], []
    for word in words:
        start, end = get_start_and_end(word)
        starts.append(start)
        ends.append(end)
    new_words = [x[0] + x[1] for x in zip(starts[::-1], ends)]
    return new_words
        


def get_start_and_end(word):
    patterns = ["ch", "ph", "th"]
    for pattern in patterns:
        if word.lower().startswith(pattern):
            return (word[:2], word[2:])
    return (word[:1], word[1:])
