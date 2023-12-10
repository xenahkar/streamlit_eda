import pandas as pd
import streamlit as st
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt



st.title('Взаимодействие банка с клиентами')
st.markdown(
    """Один из способов повысить эффективность взаимодействия банка с клиентами
     — отправлять предложение о новой услуге не всем клиентам, а только некоторым, которые
     выбираются по принципу наибольшей склонности к отклику на это предложение.
     Проведен разведочный анализ собранных для этой задачи данных с построением графиков распределений признаков,
     матрицы корреляций, графиков зависимостей целевой переменной (отклик на маркетинговую 
     кампанию) и признаков, а также вычисление числовых характеристик распределения числовых столбцов.""")

img = Image.open('bank_photo.png')
st.image(img)

df = pd.read_csv("D_dataset.csv")

tab1, tab2, tab3, tab4 = st.tabs([
    "1️⃣ Распределения признаков",
    "2️⃣ Матрица корреляций",
    "3️⃣ Зависимость целевой переменной",
    "4️⃣ Числовые характеристики распределения"
])

with tab1:
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)
    col11, col12 = st.columns(2)
    col13, col14 = st.columns(2)

    with col1:
        fig = plt.figure(figsize=(8, 8))
        sns.histplot(data=df, x="PERSONAL_INCOME", kde=True, bins=20)
        plt.xlabel('Доход, руб')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение личных доходов клиентов банка")
        st.pyplot(fig)

    with col2:
        fig = plt.figure(figsize=(8, 8))
        sns.histplot(data=df, x="AGE", kde=True, bins=20)
        plt.title("Распределение возраста клиентов банка")
        plt.xlabel('Возраст')
        plt.ylabel('Количество клиентов')
        st.pyplot(fig)

    with col3:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['TARGET'].value_counts())
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(['не было зарегистрировано', 'был зарегистрирован'])
        plt.title("Распределение клиентов по отклику на маркетинговую кампанию")
        plt.xlabel('Отклик')
        plt.ylabel('Количество клиентов')
        st.pyplot(fig)

    with col4:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['SOCSTATUS_WORK_FL'].value_counts())
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(['не работает', 'работает'])
        plt.title("Распределение социального статуса клиента относительно работы")
        plt.xlabel('Социальный статус')
        plt.ylabel('Количество клиентов')
        st.pyplot(fig)

    with col5:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['SOCSTATUS_PENS_FL'].value_counts())
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(['не пенсионер', 'пенсионер'])
        plt.xlabel('Социальный статус')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение социального статуса клиента относительно пенсии")
        st.pyplot(fig)

    with col6:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['GENDER'].value_counts())
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(['женщина', 'мужчина'])
        plt.xlabel('Пол клиента')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение клиентов по полу")
        st.pyplot(fig)

    with col7:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['CHILD_TOTAL'].value_counts())
        plt.xlabel('Количество детей')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение клиентов по количеству детей")
        st.pyplot(fig)

    with col8:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['DEPENDANTS'].value_counts())
        plt.xlabel('Количество иждивенцев')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение клиентов по количеству иждивенцев")
        st.pyplot(fig)

    with col9:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['FAMILY_INCOME'].value_counts())
        plt.xticks(rotation=90)
        plt.xlabel('Уровень семейного дохода')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение клиентов по семейному доходу")
        st.pyplot(fig)

    with col10:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['EDUCATION'].value_counts())
        plt.xticks(rotation=90)
        plt.xlabel('Уровень образования')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение клиентов по уровню образования")
        st.pyplot(fig)

    with col11:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['FL_PRESENCE_FL'].value_counts())
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(['нет', 'есть'])
        plt.xlabel('Наличие квартиры')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение клиентов по наличию в собственности квартиры")
        st.pyplot(fig)

    with col12:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['OWN_AUTO'].value_counts())
        plt.xlabel('Коичество автомобилей')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение клиентов по наличию в собственности автомобилей")
        st.pyplot(fig)

    with col13:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['LOAN_NUM_TOTAL'].value_counts())
        plt.xlabel('Количество ссуд клиента')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение клиентов по количеству ссуд")
        st.pyplot(fig)

    with col14:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.barplot(df['LOAN_NUM_CLOSED'].value_counts())
        plt.xlabel('Количество закрытых ссуд клиента')
        plt.ylabel('Количество клиентов')
        plt.title("Распределение клиентов по количеству закрытых ссуд")
        st.pyplot(fig)

with tab2:
    st.header("Матрица корреляций")
    st.text("""\n
      TARGET — отклик на маркетинговую кампанию\n
      AGE — возраст клиента\n
      SOCSTATUS_WORK_FL — социальный статус клиента относительно работы\n
      SOCSTATUS_PENS_FL — социальный статус клиента относительно пенсии\n
      GENDER — пол клиента\n
      CHILD_TOTAL — количество детей клиента\n
      DEPENDANTS — количество иждивенцев клиента\n
      OWN_AUTO — количество автомобилей в собственности\n
      FL_PRESENCE_FL — наличие в собственности квартиры\n
      PERSONAL_INCOME — личный доход клиента (в рублях)\n
      LOAN_NUM_TOTAL — количество ссуд клиента\n
      LOAN_NUM_CLOSED — количество погашенных ссуд клиента""")

    options = st.multiselect(
        'Выберите параметры для оценки корреляции',
        ['TARGET', 'AGE', 'SOCSTATUS_WORK_FL', 'SOCSTATUS_PENS_FL', 'GENDER',
         'CHILD_TOTAL', 'DEPENDANTS', 'OWN_AUTO', 'FL_PRESENCE_FL',
         'PERSONAL_INCOME', 'LOAN_NUM_TOTAL', 'LOAN_NUM_CLOSED'],
        ['TARGET'])
    fig, ax = plt.subplots(figsize=(20, 10))
    ax = sns.heatmap(df[options].corr(), annot=True, ax=ax)
    st.pyplot(fig)

with tab3:
    st.text("Графики зависимостей отклика на маркетинговую кампанию и признаков:")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)
    col11, col12 = st.columns(2)
    col13, col14 = st.columns(2)

    with col1:
        fig = plt.figure(figsize=(8, 8))
        sns.histplot(data=df, x="PERSONAL_INCOME", hue="TARGET", multiple="dodge", shrink=.8, bins=15)
        plt.title("Зависимость отклика от личного дохода")
        plt.xlabel('Доход, руб')
        plt.ylabel('Количество клиентов')
        plt.legend(['был зарегистрирован', 'не было зарегистрировано'])
        st.pyplot(fig)

    with col2:
        fig = plt.figure(figsize=(8, 8))
        sns.histplot(data=df, x="AGE", hue="TARGET", multiple="dodge", shrink=.8, bins=15)
        plt.title("Зависимость отклика от возраста клиентов банка")
        plt.xlabel('Возраст')
        plt.ylabel('Количество клиентов')
        plt.legend(['был зарегистрирован', 'не было зарегистрировано'])
        st.pyplot(fig)

    with col3:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['SOCSTATUS_WORK_FL'], hue=df['TARGET'])
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(['не работает', 'работает'])
        plt.xlabel('Социальный статус относительно работы')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от социального статуса клиента")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col4:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['SOCSTATUS_PENS_FL'], hue=df['TARGET'])
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(['не пенсионер', 'пенсионер'])
        plt.xlabel('Социальный статус относительно пенсии')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от социального статуса клиента")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col5:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['GENDER'], hue=df['TARGET'])
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(['женщина', 'мужчина'])
        plt.xlabel('Пол клиента')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от пола клиента")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col6:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['CHILD_TOTAL'], hue=df['TARGET'])
        plt.xlabel('Количество детей')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от количества детей")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col7:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['DEPENDANTS'], hue=df['TARGET'])
        plt.xlabel('Количество иждивенцев')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от количества иждивенцев")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col8:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['FAMILY_INCOME'], hue=df['TARGET'])
        plt.xticks(rotation=90)
        plt.xlabel('Уровень семейного дохода')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от семейного дохода")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col9:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['EDUCATION'], hue=df['TARGET'])
        plt.xticks(rotation=90)
        plt.xlabel('Уровень образования')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от уровня образования")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col10:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['FL_PRESENCE_FL'], hue=df['TARGET'])
        ax.set_xticks(ax.get_xticks())
        ax.set_xticklabels(['нет', 'есть'])
        plt.xlabel('Наличие квартиры')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от наличия в собственности квартиры")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col11:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['OWN_AUTO'], hue=df['TARGET'])
        plt.xlabel('Коичество автомобилей')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от наличия в собственности автомобилей")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col12:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['LOAN_NUM_TOTAL'], hue=df['TARGET'])
        plt.xlabel('Количество ссуд клиента')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от количества ссуд")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

    with col13:
        fig = plt.figure(figsize=(8, 8))
        ax = sns.countplot(x=df['LOAN_NUM_CLOSED'], hue=df['TARGET'])
        plt.xlabel('Количество закрытых ссуд клиента')
        plt.ylabel('Количество клиентов')
        plt.title("Зависимость целевой переменной от количества закрытых ссуд")
        plt.legend(['не было зарегистрировано', 'был зарегистрирован'])
        st.pyplot(fig)

with tab4:
    st.text("")
    st.text("""\n
      TARGET — отклик на маркетинговую кампанию\n
      AGE — возраст клиента\n
      SOCSTATUS_WORK_FL — социальный статус клиента относительно работы\n
      SOCSTATUS_PENS_FL — социальный статус клиента относительно пенсии\n
      GENDER — пол клиента\n
      CHILD_TOTAL — количество детей клиента\n
      DEPENDANTS — количество иждивенцев клиента\n
      OWN_AUTO — количество автомобилей в собственности\n
      FL_PRESENCE_FL — наличие в собственности квартиры\n
      PERSONAL_INCOME — личный доход клиента (в рублях)\n
      LOAN_NUM_TOTAL — количество ссуд клиента\n
      LOAN_NUM_CLOSED — количество погашенных ссуд клиента""")

    options = st.multiselect(
        'Выберите параметры для определения описательной статистики',
        ['TARGET', 'AGE', 'SOCSTATUS_WORK_FL', 'SOCSTATUS_PENS_FL', 'GENDER',
         'CHILD_TOTAL', 'DEPENDANTS', 'OWN_AUTO', 'FL_PRESENCE_FL',
         'PERSONAL_INCOME', 'LOAN_NUM_TOTAL', 'LOAN_NUM_CLOSED'],
        ['AGE', 'PERSONAL_INCOME'])

    st.table(df[options].describe())

