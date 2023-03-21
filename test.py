from fuzzywuzzy import fuzz
from fuzzywuzzy import process


test = fuzz.ratio('Привет', 'ты здесь')
if test >= 50:
	print("Эти две строки похожы.")
else:
	print("Никак нет!")
print("Шанс похожести: "+str(test))