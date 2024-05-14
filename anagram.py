def is_anagram(str1, str2):

    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)
string1 = "state"
string2 = "taste"
print(is_anagram(string1, string2))
