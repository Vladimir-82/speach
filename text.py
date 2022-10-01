from langdetect import detect
from langdetect import detect_langs

# Single language detection
print(detect("War doesn't show who's right, just who's left."))
print(detect("Ein, zwei, drei, vier"))
print(detect("李红：不，那不是杂志。那是字典"))
print(detect("Доброе утро"))
print(detect("voulez vous manger avec moi"))


# language probabilities best match
print(detect_langs("Otec matka syn."))
