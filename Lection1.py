word = 'python'
word = word[:3] + 'x' + word[4:]
print(word)
print(word[2])
print(word[-1])

word = word.replace('x', 'y')
print(word)

word2 = "py'123'thon"
print(word2)
word2 = 'py\
123thon'
print(word2)
word2 = """py
123thon"""
print(word2)