import pyperclip
import random
words = ["across", "and", "boy", "down", "hall", "large", "the", "the", "the", "threw", "skunk", "walked"]
num_reps = 20
string = ""
for i in range(num_reps):
    random.shuffle(words)
    string += str(i + 1) + ") "
    string += " ".join(words)
    string += ".\n"

print(string)
pyperclip.copy(string)