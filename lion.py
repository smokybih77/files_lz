from collections import Counter         # счетчик
import string
import docx
import pandas as pd
import matplotlib.pyplot as plt


path = ('C:\\python\\alala\\files_lz\lion.docx')       # прямой путь к файлу  lion.docx

# извлечем текст из файла
document = docx.Document(path)
full_text = []
for i in document.paragraphs:
    full_text.append(i.text)
text = ' '.join(full_text)

t = str.maketrans('', '', string.punctuation)          # удаляем знаки препинания и переводем весь текст в мелкий шрифт
text = text.translate(t).lower()

# считаем сколько встречались слова
words = text.split()
word_count = Counter(words)

total_words = sum(word_count.values())              # подсчет общей суммы всех слов
word_frequency = {word: (count / total_words) * 100 for word, count in word_count.items()}  # выразим в процентах

# сохранение в файл excel
word_spisok = [(word, count, word_frequency[word]) for word, count in word_count.items()]
df = pd.DataFrame(word_spisok, columns = ['Слово', 'Количество', 'Частота (%)'])
df.to_excel('words_table.xlsx', index = False) # index=False чтобы не записывать столбец индекса

# счет сколько встретились буквы
letters = [item for item in text if item.isalpha() and item in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'] #cоздаем список letters, который содержит только буквы из переменной text. 
letter_count = Counter(letters)                                                                   # item.isalpha() проверяет является ли элемент item буквой 

#вывод в виде гистограммы
df_letters = pd.DataFrame(letter_count.items(), columns = ['Буква', 'Частота'])
plt.bar(df_letters['Буква'], df_letters['Частота'])
plt.title('Частота встречаемости букв')
plt.xlabel('Буквы')
plt.ylabel('Частота')
plt.show()
