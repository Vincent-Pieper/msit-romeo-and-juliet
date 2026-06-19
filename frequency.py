from romeo_and_juliet import PLAY


def get_words(words):
    word_list = words.split()
    return word_list


def words_frequency(basic_words):
    unique_words = get_unique_words(basic_words)
    no_count_dict = create_dict(unique_words)
    count_dict = counted_list(no_count_dict, basic_words)
    print(count_dict)
    #continue Step 3 on cosio


def get_unique_words (basic_words):
    unique_words = []
    for word in basic_words:
        if word in unique_words:
            continue
        else:
            unique_words.append(word)
    return unique_words


def create_dict (unique_words):
    no_count_dict = {}
    for word in unique_words:
        no_count_dict[word] = 0
    return no_count_dict


def counted_list(no_count_dict, basic_words):
    for word in basic_words:
        no_count_dict[word] += 1
    return no_count_dict




def main():
    basic_words = get_words(PLAY)
    words_frequency(basic_words)

if __name__ == "__main__":
    main()