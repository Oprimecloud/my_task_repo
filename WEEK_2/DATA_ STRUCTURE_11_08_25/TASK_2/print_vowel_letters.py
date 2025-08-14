# number 9 TASK 2
# input
Words=str(input("ENTER A SENTENCE IN CAPITAL LETTER: "))
vowel_a =Words.upper().count("A") # find vowels 
vowel_e =Words.upper().count("E") 
vowel_i =Words.upper().count("I")
vowel_o =Words.upper().count("O")
vowel_u =Words.upper().count("U")
total_vowel = (vowel_a + vowel_e + vowel_i + vowel_o + vowel_u)
print(total_vowel)
