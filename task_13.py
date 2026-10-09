word = input("Enter a word:")

counter = 0
for letter in word:
    if letter == "e":
        counter += 1
print(f"Letter e appears {counter} times")
