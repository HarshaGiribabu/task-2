def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
input_string = "level"
print(is_palindrome(input_string))