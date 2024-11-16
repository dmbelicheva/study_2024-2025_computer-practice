---
## Front matter
title: "Лабораторная работа №1"
subtitle: " Julia. Установка и настройка. Основные принципы."
author: "Беличева Дарья Михайловна"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: false # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: IBM Plex Serif
romanfont: IBM Plex Serif
sansfont: IBM Plex Sans
monofont: IBM Plex Mono
mathfont: STIX Two Math
mainfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
romanfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
sansfontoptions: Ligatures=Common,Ligatures=TeX,Scale=MatchLowercase,Scale=0.94
monofontoptions: Scale=MatchLowercase,Scale=0.94,FakeStretch=0.9
mathfontoptions:
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Основная цель работы — подготовить рабочее пространство и инструментарий для
работы с языком программирования Julia, на простейших примерах познакомиться
с основами синтаксиса Julia.

# Задание

1. Установите под свою операционную систему Julia, Jupyter.
2. Используя Jupyter Lab, повторите примеры из раздела лабораторной работы.
3. Выполните задания для самостоятельной работы.

# Теоретическое введение

Julia -- высокоуровневый свободный язык программирования с динамической типизацией, созданный для математических вычислений [@julialang]. Эффективен также и для написания программ общего назначения. Синтаксис языка схож с синтаксисом других математических языков, однако имеет некоторые существенные отличия.

Для выполнения заданий была использована официальная документация Julia [@juliadoc].

# Выполнение лабораторной работы

У меня уже были установлены Julia и Jupyter (рис. [-@fig:001]).

![Запуск Julia](image/1.png){#fig:001 width=70%}

Теперь повторим простейшие примеры для знакомства с синтаксисом Julia (рис. [-@fig:001]-[-@fig:004]).

![Выполнение примеров из лабораторной](image/2.png){#fig:002 width=70%}

![Выполнение примеров из лабораторной](image/3.png){#fig:003 width=70%}

![Выполнение примеров из лабораторной](image/4.png){#fig:004 width=70%}

Теперь перейдем к выполнению заданий.

**Задание №1**

Изучим документацию по основным функциям Julia для чтения / записи / вывода информации на экран: read(), readline(), readlines(), readdlm(), print(),
println(), show(), write(). Приведем свои примеры их использования, поясняя
особенности их применения.

Для того, чтобы ознакомиться с документацией достаточно поставить знак `?` перед интересующей функцией. Например, `?print`.

Создадим текстовый файл с любым содержанием в папке, где мы работаем. Откроем его на чтение и прочитаем с помощью команды `read()`. Текст вывелся в одну строку с разделителями `\r\n`. Также прочитаем текст используя функцию `readline()` - выведется только первая строка. Чтобы прочитать все строки в файле используем команду `readlines()` (рис. [-@fig:005]).

![Чтение файла](image/5.png){#fig:005 width=70%}

Далее посмотрим, как работает команда `println()`, `print()` и `show()`  (рис. [-@fig:006]-[-@fig:007]).

![Вывод на печать](image/6.png){#fig:006 width=70%}

![Вывод на печать](image/7.png){#fig:007 width=70%}

Посмотрим на работу функции `write()` (рис. [-@fig:008]).

![Команда записи](image/8.png){#fig:008 width=70%}

**Задание №2**

Изучим документацию по функции parse() (рис. [-@fig:009]). Приведем свои примеры её использования, поясняя особенности её применения (рис. [-@fig:010]).

![Документация по функции parse()](image/9.png){#fig:009 width=70%}

![Примеры использования функции parse()](image/10.png){#fig:010 width=70%}

**Задание №3**

Изучим синтаксис Julia для базовых математических операций с разным типом переменных: сложение, вычитание, умножение, деление, возведение в степень, извлечение
корня, сравнение, логические операции. Приведем примеры с пояснениями по
особенностям их применения (рис. [-@fig:011]-[-@fig:012]).

![Примеры базовых математических операций](image/11.png){#fig:011 width=70%}

![Примеры базовых математических операций](image/12.png){#fig:012 width=70%}

**Задание №4**

Приведем несколько примеров с пояснениями с операциями над матрицами
и векторами: сложение, вычитание, скалярное произведение, транспонирование,
умножение на скаляр (рис. [-@fig:013]-[-@fig:014]).

![примеры операций над матрицами](image/13.png){#fig:013 width=70%}

![примеры операций над векторами](image/14.png){#fig:014 width=70%}

# Выводы

В результате выполнения данной лабораторной работы я подготовила рабочее пространство и инструментарий для
работы с языком программирования Julia, на простейших примерах познакомилась
с основами синтаксиса Julia.

# Список литературы{.unnumbered}

::: {#refs}
:::
