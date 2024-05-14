def most_frequent_character(s):
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    max_freq_char = max(char_freq, key=char_freq.get)
    return max_freq_char
input_string = "falll rainingjdasdjkahdnadkj"
print("Most frequent character:", most_frequent_character(input_string))
