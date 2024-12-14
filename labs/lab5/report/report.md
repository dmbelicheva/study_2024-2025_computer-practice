---
## Front matter
title: "Лабораторная работа № 5"
subtitle: "Построение графиков"
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

Основная цель работы -- освоить синтаксис языка Julia для построения графиков.

# Задание

1. Используя JupyterLab, повторите примерыи. При этом дополните графики
обозначениями осей координат, легендой с названиями траекторий, названиями
графиков и т.п.

2. Выполните задания для самостоятельной работы.

# Теоретическое введение

Julia -- высокоуровневый свободный язык программирования с динамической типизацией, созданный для математических вычислений [@julialang]. Эффективен также и для написания программ общего назначения. Синтаксис языка схож с синтаксисом других математических языков, однако имеет некоторые существенные отличия.

Для выполнения заданий была использована официальная документация Julia [@juliadoc].

# Выполнение лабораторной работы

Выполним примеры из лабораторной работы для знакомства с пакетами по отрисовки графиков и их функциями (рис. [-@fig:001]-[-@fig:019]).

![Основные пакеты для работы с графиками в Julia](image/1.png){#fig:001 width=70%}

![Основные пакеты для работы с графиками в Julia](image/2.png){#fig:002 width=70%}

![Опции при построении графика](image/3.png){#fig:003 width=70%}

![Опции при построении графика](image/4.png){#fig:004 width=70%}

![Точечный график](image/5.png){#fig:005 width=70%}

![Точечный график](image/6.png){#fig:006 width=70%}

![Аппроксимация данных](image/7.png){#fig:007 width=70%}

![Полярные координаты](image/8.png){#fig:008 width=70%}

![График поверхности](image/9.png){#fig:009 width=70%}

![Линии уровня](image/10.png){#fig:010 width=70%}

![Векторные поля](image/11.png){#fig:011 width=70%}

![Анимация](image/12.png){#fig:012 width=70%}

![Гипоциклоида](image/13.png){#fig:013 width=70%}

![Errorbars](image/14.png){#fig:014 width=70%}

![Errorbars](image/15.png){#fig:015 width=70%}

![Использование пакета Distributions](image/16.png){#fig:016 width=70%}

![Подграфики](image/17.png){#fig:017 width=70%}

![Подграфики](image/18.png){#fig:018 width=70%}

![Подграфики](image/19.png){#fig:019 width=70%}

## Задания для самостоятельного выполнения

Выполним задания (рис. [-@fig:020]-[-@fig:030]).

![Задание №1 и №2](image/20.png){#fig:020 width=70%}

![Задание №3](image/21.png){#fig:021 width=70%}

![Задание №4](image/22.png){#fig:022 width=70%}

![Задание №5](image/23.png){#fig:023 width=70%}

![Задание №6](image/24.png){#fig:024 width=70%}

![Задание №7 и №8](image/25.png){#fig:025 width=70%}

![Задание №9](image/26.png){#fig:026 width=70%}

![Задание №10](image/27.png){#fig:027 width=70%}

![Задание №10](image/28.png){#fig:028 width=70%}

![Задание №11](image/29.png){#fig:029 width=70%}

![Задание №11](image/30.png){#fig:030 width=70%}

# Выводы

В результате выполнения данной лабораторной работы я освоила синтаксис языка Julia для построения графиков.

# Список литературы{.unnumbered}

::: {#refs}
:::
