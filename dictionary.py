mydict = {}
vowels_permuted = "eaiuo"
different_permutation = "iuoae"
VOWELS_LOWER = "aeiou"
VOWELS_UPPER = "AEIOU"

print(vowels_permuted[0])
print(VOWELS_LOWER[0])


# i is the index that I am looping through e.g, 0,1,2,3,4,5
# char is the literal character value of where the index is sitting, so if index
# is 0 and the string is vowels_permuted, the character is "e"
for i, char in enumerate(vowels_permuted):
    mydict[char] = VOWELS_LOWER[i]  # name i and char for what they are, i is index
    # don't confuse yourself by naming i as some other variable
    # it is not going to change, it's i or index
    mydict[char.upper()] = VOWELS_UPPER[i]

alphabet = "abcdefghijklmnopqrstuvwxyz"

# always map one unique key to a value for a dict
# you can have many values be the same, but keys are completely unique
#
empty_dict = {}

for i, char in enumerate(alphabet):
    empty_dict[i] = char

print(empty_dict)
print(mydict)

new_dict = {}

friends = ["Gawrath", "Daniel", "Charles", "Michael", "Owen", "Peter"]
ages = [28, 29, 28, 28, 29, 27]

for index, friend in enumerate(friends):
    new_dict[friend] = ages[index]

new_dict["Charles"] = 30
new_dict["Charles"] = "Charles"

# print(new_dict.keys())
# print(new_dict.values())
# print(new_dict)
# new_dict.pop("Gawrath")  # pop removes a value from the dictionary
# print(new_dict.get("Ross", 100))

new_friends = friends[-2:]
print(new_friends)


text = "hello world"

swapped_vowels = ""

for letter in text:
    if letter in mydict:
        swapped_vowels += mydict[letter]
    else:
        swapped_vowels += letter

print("Swapped vowels string", swapped_vowels)
