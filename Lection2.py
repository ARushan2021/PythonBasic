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
word2 = "abc\nabc"
print(word2)
word2 = "abc\tabc"
print(word2)

word2 = "python"
print(word2[::2])
print(word2[1:4:1])
print(word2[::-1])

word2 = "python" + " 3 "
print(word2*2)

word = 'find a substring'
print(word.find('ing'))

seq = ['one','two','three']
sep = ' + '
print(sep.join(seq))

word = 'find a substring'
print(word.split(' '))

word = 'one two three'
print(word.replace('two', 'wow'))

word = '   one two three    '
print(word.strip()) # удаление пробелов в начале и конце строки

word = 'rrrone two three    '
print(word.lstrip('r'))

print(str('1')) # из числа в строку
print(int('1')) # из строки в число
print(ord('2')) # из числа в байт
print(chr(49)) # из байта в число

