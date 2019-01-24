#f = open('files/relative_data.txt', 'r')       #open the file.....relative path
f = open('/home/ubuntu/workspace/files/relative_data.txt', 'r')     #absolute path
lines = f.read()           #read gives 4 seperate lines. appears as text not as a list of strings(like readlines does)                         #readlines gives ['This is the first line\n', 'Andthis is the second line\n', 'Here is the                             third line\n', 'And here, the fourth'](4 seperate strings)
f.close()
print(lines)