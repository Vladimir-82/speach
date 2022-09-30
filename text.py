from textblob import TextBlob


blob = TextBlob("bonjour")


print(blob.detect_language())