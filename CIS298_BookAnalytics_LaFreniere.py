# Mark LaFreniere
# 4/9/21
# Finds top 50 longest and most frequent words in a txt. 
# txt must have at least 50 unique words
import matplotlib.pyplot as plt

ifs = open("Frankenstein.txt")
if ifs.readable() == False:
    print("File not readable: Check ' or \"")
fileString = ifs.read()
words = [['',0,0]]
word = ''
i = 0
fileString = fileString.lower()

# Start collection
while i < len(fileString):
    # When a word is detected, start appending into a string
    if fileString[i].isalnum() == True:
        while fileString[i].isalnum() or fileString[i] == '\'':
            word += fileString[i]
            i += 1
        lenWord = len(word)
        # Search for word in existing data list
        for j in range(0,len(words)):
            # If the word is found in the list, increment its frequency
            if words[j][0] == word:                   
                words[j][2] += 1 
                break
            # If word is not found in the list, append it as a new entry
            elif j == len(words) - 1:    
                wordSet = [word, lenWord, 1]
                words.append(wordSet)           
    
    word = ""
    i += 1

# pop initialization entry from words
words.pop(0)
top50Length = []
top50Freq = []

# sort words in descending order based on length
words.sort(key = lambda x: x[1])
# get top 50 
for i in range(len(words) - 50, len(words)):
    top50Length.append(words[i])

# sort words in descending order based on frequency
words.sort(key = lambda x: x[2])
# get top 50
for i in range(len(words) - 50, len(words)):
   top50Freq.append(words[i])

# plot Length plot
plt.bar([top50Length[i][0] for i in range(0,len(top50Length))], [top50Length[i][1] for i in range(0,len(top50Length))])
plt.xticks([top50Length[i][0] for i in range(0,len(top50Length))], [top50Length[i][0] for i in range(0,len(top50Length))])
plt.xticks(rotation = 45, fontsize = 8, ha='right')
plt.title("Top 50 Longest Words")
plt.ylabel("Length")
plt.text(1,19,"Largest Word:")
plt.text(7,19,top50Length[49][0])
for i in range(0,len(top50Length)):
    plt.text(i, top50Length[i][1], top50Length[i][1], fontsize = 8, ha='center', va='bottom')
plt.show()

# plot Frequency plot
plt.bar([top50Freq[i][0] for i in range(0,len(top50Freq))], [top50Freq[i][2] for i in range(0,len(top50Freq))])
plt.xticks([top50Freq[i][0] for i in range(0,len(top50Freq))], [top50Freq[i][0] for i in range(0,len(top50Freq))])
plt.xticks(rotation = 45, fontsize = 8, ha='right')
plt.title("Top 50 Most Frequent Words")
plt.ylabel("Length")
plt.text(1,4500,"Most Frequent Word:")
plt.text(9,4500,top50Freq[49][0])
for i in range(0,len(top50Freq)):
    plt.text(i, top50Freq[i][2], top50Freq[i][2], fontsize = 8, ha='center', va='bottom')
plt.show()