
# f = open('/Users/robertelias/Desktop/UdacityDataStructuresAlgorithms/Script_Folder/some_file.txt', 'r')
# file_data = f.read()
# f.close()
# print(file_data)


f = open('/Users/robertelias/Desktop/UdacityDataStructuresAlgorithms/Script_Folder/my_file.txt', 'w')
f.write("Hello there!")
f.close()

#too many files opened
# files = []
# for i in range(10000):
#     files.append(open('some_file.txt', 'r'))
#     print(i)

# auto closes the file
with open('/Users/robertelias/Desktop/UdacityDataStructuresAlgorithms/Script_Folder/some_file.txt', 'r') as f:
    file_data = f.read()
    f.close()
    print(file_data)
