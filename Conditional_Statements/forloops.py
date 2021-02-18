# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []

# # write your for loop here
# for name in names:

#     usernames.append(name.lower().replace(" ", "_"))

# print(usernames)


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing",
             "Phoebe Buffay"]

for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace( " ", "_")
print(usernames)

print("----------------------------------------")

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == "<" and token[-1] == ">":
        count = count + 1

print(count)

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line,
# it does the characters that are after it in html_str
# are on the next line

for item in items:
    html_str = html_str + "<li>" + str(item) + "<li>" "\n"

html_str = html_str + "<ul>"

print(html_str)