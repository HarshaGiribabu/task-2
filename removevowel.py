def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return " ".join(char for char in string if char not in vowels)

string = "helloguviO"

result = remove_vowels(string)
print("vowels removed:", result)
