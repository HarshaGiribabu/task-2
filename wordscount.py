def count_words(s):
    words = s.split()
    return len(words)
input_string = "Hello, how are you?"
print("Number of words:", count_words(input_string))
