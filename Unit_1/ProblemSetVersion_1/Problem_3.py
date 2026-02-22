def tiggerfy(word):
    word = word.lower()
    word = word.replace("t", "").replace("i", "").replace("gg", "").replace("er", "")
    print(word)


word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
