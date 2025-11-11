import matplotlib.pyplot as plt
import pandas as pd

# переводим паркет в csv
path = ('C:\\python\\alala\\files_lz\\titanic.parquet')
parq = pd.read_parquet(path)
parq.to_csv('titanic.csv', index = False)        # убираем индексы
parq = pd.read_csv('titanic.csv') # чтение данных
survived = parq.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0) #новая таблица. #groupby группирует в одно общее
# .size считает сколько в каждой группе строк, в нашем случае пассажиров. # unstack(fill_value=0) превращает результат в таблицу

survived_percent = survived.div(survived.sum(axis=1), axis=0) * 100
#.sum считает кол-во пассажиров в классе. .div делит значение на общее количество, чтоб выразить в проценты


# гистограмма
survived_percent.plot(kind='bar', stacked=True, color=['blue', 'orange'])
plt.title('Выживаемость пассажиров Титаника')
plt.xlabel('Класс')
plt.ylabel('Процент')
plt.legend(['Не выжил', 'Выжил'])
plt.show()
