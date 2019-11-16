chars=set()
for i in range(26):
    chars.add(chr(ord("a")+i))
    chars.add(chr(ord("A")+i))
a = input()
for word in a:
    if word in chars:
        print(word,end="")
