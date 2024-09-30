def calculate_letter_frequency(sentence):
    letter_freq = {}

    for char in sentence:
        if char.isalpha():
            char = char.lower()
            letter_freq[char] = letter_freq.get(char,0)+1

    return letter_freq
    
sentence = input("Enter a sentence : ")
letter_freq = calculate_letter_frequency(sentence)
print(letter_freq)