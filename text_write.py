with open("output.txt", "r") as text_file:
    text_in_file = text_file.readlines()

# change data here
new_text = text_in_file
print(new_text)

with open("output.txt", "a") as text_file:
    text_file.writelines(new_text)
