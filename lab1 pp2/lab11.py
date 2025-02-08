print("".join(word.capitalize() if i else word for i, word in enumerate(input().split("_"))))
