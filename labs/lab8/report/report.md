---
## Front matter
title: "Лабораторная работа № 8"
subtitle: "Оптимизация"
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

Основная цель работы -- освоить пакеты Julia для решения задач оптимизации.

# Задание

1. Используя JupyterLab, повторите примеры.

2. Выполните задания для самостоятельной работы.

# Теоретическое введение

Julia -- высокоуровневый свободный язык программирования с динамической типизацией, созданный для математических вычислений [@julialang]. Эффективен также и для написания программ общего назначения. Синтаксис языка схож с синтаксисом других математических языков, однако имеет некоторые существенные отличия.

Для выполнения заданий была использована официальная документация Julia [@juliadoc].

# Выполнение лабораторной работы

Выполним примеры из лабораторной работы (рис. [-@fig:001]-[-@fig:011]).

![Линейное программирование](image/1.png){#fig:001 width=70%}

![Векторизованные ограничения и целевая функция оптимизации](image/2.png){#fig:002 width=70%}

![Оптимизация рациона питания](image/3.png){#fig:003 width=70%}

![Оптимизация рациона питания](image/4.png){#fig:004 width=70%}

![Оптимизация рациона питания](image/5.png){#fig:005 width=70%}

![Путешествие по миру](image/6.png){#fig:006 width=70%}

![Портфельные инвестиции](image/7.png){#fig:007 width=70%}

![Портфельные инвестиции](image/8.png){#fig:008 width=70%}

![Восстановление изображения](image/9.png){#fig:009 width=70%}

![Восстановление изображения](image/10.png){#fig:010 width=70%}

![Восстановление изображения](image/11.png){#fig:011 width=70%}

Теперь выполним задания для самостоятельный работы (рис. [-@fig:012]-[-@fig:016]).

![Задание 1. Линейное программирование](image/12.png){#fig:012 width=70%}

![Задание 2. Линейное программирование. Использование массивов](image/13.png){#fig:013 width=70%}

![Задание 3. Выпуклое программирование](image/14.png){#fig:014 width=70%}

![Задание 4. Оптимальная рассадка по залам](image/15.png){#fig:015 width=70%}

![Задание 5. План приготовления кофе](image/16.png){#fig:016 width=70%}

# Выводы

В резцльтате выполнения данной лабораторной работы я оосвоила пакеты Julia для решения задач оптимизации.

# Список литературы{.unnumbered}

::: {#refs}
:::
