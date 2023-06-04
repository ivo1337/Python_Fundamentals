string = input()
counter = 0

while string != "END":
    if string == "coding" or string == "dog" or string == "cat" or string == "movie":
        counter += 1
    elif string == "CODING" or string == "DOG" or string == "CAT" or string == "MOVIE":
        counter += 2
    string = input()
if counter > 5:
    print("You need extra sleep")
else:
    print(counter)