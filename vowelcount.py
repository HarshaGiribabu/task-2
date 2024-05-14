vowels = 'aeiou'
string = "Guvi Geeks Network private limited"
vowel_dict = {ch: 0 for ch in vowels}
for char in string.lower():
  if char in vowel_dict:
    vowel_dict[char] += 1
total_vowels = sum(vowel_dict.values())
print(f"Total number of vowels found: {total_vowels}")
for key, value in vowel_dict.items():
  print(f"Count of {key}: {value}")
