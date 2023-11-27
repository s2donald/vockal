# %%

dict = {}
file = open("lang.txt", "r")
# reading each line
dict = {}
i = 0
key = ""
for line in file:
    # reading each word
    for word in line.split():
        print(word + " " + str(i))
        if i == 0:
            key = word
            i = i + 1
        else:
            dict[key] = word
            print(key + " " + word)
            i = i - 1

print(dict)
