text = "Hello, how are you doing today?"

vowels = {char.upper() for char in text if char.lower() in 'aeiou'}

print(vowels)
