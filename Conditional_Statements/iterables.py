print("==========================================")
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

print("==========================================")


for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(cities)

print("==========================================")
for i in range(3):
    print("Hello, Robert Elias!")

print("==========================================")
sentence = ["the", "quick", "brown", "fox",
            "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for word in sentence:
    print(word)

print("==========================================")
# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for i in range(5, 35, 5):
    print(i)
