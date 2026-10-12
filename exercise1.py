counts = dict()
print("Enter a filename: ")
filename = input('')

with open(filename, "r") as f:
    line = f.read()
    words = line.split()

print("Words: ", words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)