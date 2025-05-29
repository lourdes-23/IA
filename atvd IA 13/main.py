import nltk
from nltk.tokenize import sent_tokenize
from textblob import TextBlob
nltk.download('punkt_tab')
texto = "I hate exams. I love learning"
frases = sent_tokenize(texto)

for frase in frases:
    blod = TextBlob(frase)
    sentimento = blod.sentiment.polarity
    status = "\033[42m positivo \033[m" if sentimento > 0 else "\033[41m negativo \033[m" if sentimento < 0 else "\033[43m neutro \033[m"
    print(f"frase: {frase} → {status} (score: {sentimento: .2f})")                                                                                                                                                                                                                                 