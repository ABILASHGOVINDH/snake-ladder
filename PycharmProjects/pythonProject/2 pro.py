with open("story.txt","r") as f:
    story = f.read()

words = set()
start = -1
traget_start ="<"
traget_end =">"

for i, char in enumerate(story):
    if  char  == traget_start:
        start = i
    if char == traget_end and start != -1:
        word = story[start: i+1 ]
        words.add(word)
        start-1

answers ={}

for  word in words:
    answer = input(f" enter the word {word}:")
    answers[word] = answer

for word in words:
    story=story.replace(word, answers[word])

print(story)