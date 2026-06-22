from romeo_and_juliet import PLAY


def get_words(words):
    word_list = words.split()
    return word_list


def words_frequency(basic_words):
    unique_words = get_unique_words(basic_words)
    no_count_dict = create_dict(unique_words)
    count_dict = counted_list(no_count_dict, basic_words)
    return count_dict


def get_unique_words(basic_words):
    unique_words = []
    for word in basic_words:
        if word in unique_words:
            continue
        else:
            unique_words.append(word)
    return unique_words


def create_dict(unique_words):
    no_count_dict = {}
    for word in unique_words:
        no_count_dict[word] = 0
    return no_count_dict


def counted_list(no_count_dict, basic_words):
    for word in basic_words:
        no_count_dict[word] += 1
    return no_count_dict


def top_n_words(freq, n):
    working_freq = freq.copy()
    for i in range(n):
        most_common_word = max(working_freq, key=working_freq.get)
        most_common_value = working_freq[most_common_word]
        print(f"{most_common_word}: {most_common_value}")
        del working_freq[most_common_word]


def main():
    basic_words = get_words(PLAY)
    freq = words_frequency(basic_words)
    n = int(input("How many words should be shown? "))
    top_n_words(freq, n)


if __name__ == "__main__":
    main()