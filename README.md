# Streamlit-приложение с разведочным анализом 

Осуществлена предобработка [исходных данных](https://github.com/aiedu-courses/stepik_linear_models/tree/main/datasets): удаление дубликатов и аномальных значений, агрегирование данных клиентов по общему количеству ссуд и количеству погашенных ссуд, а также объединение данных в один файл `D_dataset.csv`.

Проведен разведочный анализ данных `D_dataset.csv` с построением графиков распределений признаков, 
матрицы корреляций, графиков зависимостей целевой переменной (отклик на маркетинговую кампанию) и признаков, 
а также вычисление характеристик распределения числовых столбцов.

## Streamlit app

Приложение развернуто по ссылке https://edaofbankclients.streamlit.app/

## Files
- `BD_homework.ipynb`: preprocessing data Jupyter Notebook
- `app.py`: streamlit app file
- `D_dataset.csv`: data file
- `requirements.txt`: package requirements files

