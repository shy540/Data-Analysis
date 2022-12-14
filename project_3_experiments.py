# -*- coding: utf-8 -*-
"""Project 3 Experiments.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10QXWt4yzlmgKZZRsDIdmFa-jgkZv-_-S
"""

library(ggplot2)

"""**% Individual Stopped per Race with Respect to Population**

The following code creates a dataframe that determines the percentage of individuals per race stopped in proportion to their population. 

The meaning for each of the variables is as follow: 

*   population_count = The population in Texas for each race
*   population_per = The population percentage in Texas for each race
*   stopped_count = The count of individuals stopped in Texas for each race
*   stopped_per = The percentage of individuals stopped in Texas for each race
*   per_stopped_pop = The percentage of individuals stopped in Texas for each race with respect to population
*   prop_stopped = The proportion of individuals stopped in Texas for each race with respect to population



"""

race = c("White", "Hispanic", "Black", "Asian", "Other")

population_count = c(11812100, 10438600,3241460,1263620, 466990)
population_per = c(43, 38.8, 11.8, 4.6, 1.7)

stopped_count = c(800860, 673554, 169820, 30725, 8997)
stopped_per = c(45.88, 38.59, 9.73, 1.76, 0.52)

per_stopped_pop = (stopped_count/population_count) * 100
prop_stopped = stopped_per/population_per

df_stopped = data.frame(race, population_count, stopped_count,per_stopped_pop)
head(df_stopped)

"""The following graph shows the 'Percentage of Individuals Stopped by Race with Respect to Population'"""

ggplot(df_stopped) +
  geom_col(aes(x=race, y = per_stopped_pop))

"""**% Individual Stopped per Race by Gender with Respect to Population**

The following code creates a dataframe that determines the percentage of individuals per race by gender stopped in proportion to their population. 

The meaning for each of the variables is as follow: 

*   race_g = Race and gender
*   population_g_count = The population in Texas for each race by gender
*   population_g_per = The population percentage in Texas for each race by gender
*   stopped_g_count = The count of individuals stopped in Texas for each race by gender
*   stopped_g_per = The percentage of individuals stopped in Texas for each race by gender
*   per_stopped_g_pop = The percentage of individuals stopped in Texas for each race by gender with respect to population

"""

race_g = c("White_F","White_M", "Hispanic_F", "Hispanic_M", "Black_F","Black_M", "Asian_F", "Asian_M", "Other_F","Other_M")
gender = c("F","M", "F", "M", "F", "M", "F", "M", "F", "M")

population_g_per_ = c(21.6, 21.3, 19.5, 19.2, 5.9, 5.8, 2.3, 2.2, .85, .84)
population_g_count = c(5933520, 5851110, 5356650, 5274240, 1620730, 1593260, 631810, 604340, 2334950, 2307480)

stopped_g_count = c(284587, 516273, 202542, 471000, 60764, 109056, 8629,22096, 2403, 6592 )
per_stopped_g_pop = (stopped_g_count/population_g_count) * 100

df_stopped_gender = data.frame(race_g, gender, population_g_count, stopped_g_count,per_stopped_pop)
head(df_stopped_gender)

"""The following graph shows the 'Percentage of Individuals Stopped by Race by Gender with Respect to Population'

The colors reflect gender, with pink referring to female individuals and blue referring to male individuals. 
"""

ggplot(df_stopped_gender) +
  geom_col(aes(x=race_g, y = per_stopped_g_pop, fill = gender))

"""**% Female Individual Stopped per Race with Respect to Population**

The following code creates a dataframe that determines the percentage of female individuals per race stopped in proportion to their population. 
"""

race_F = c("White_F", "Hispanic_F","Black_F", "Asian_F", "Other_F")
population_count_F = c(5933520, 5356650, 1620730, 631810, 2334950)
stopped_count_F = c (284587, 202542, 60764, 8629, 2403 )
per_stopped_F = (stopped_count_F/population_count_F) * 100
df_stopped_F = data.frame(race_F, population_count_F,stopped_count_F, per_stopped_F)
head(df_stopped_F)

"""The following graph shows the 'Percentage of Female Individuals Stopped by Race with Respect to Population'"""

ggplot(df_stopped_F) +
  geom_col(aes(x=race_F, y = per_stopped_F))

"""**% Male Individual Stopped per Race with Respect to Population**

The following code creates a dataframe that determines the percentage of male individuals per race stopped in proportion to their population. 
"""

race_M = c("White_M", "Hispanic_M","Black_M", "Asian_M", "Other_M")
population_count_M = c(5851110, 5274240, 1593260, 604340, 2307480)
stopped_count_M = c(516273, 471000, 109056,22096, 6592)
per_stopped_M = (stopped_count_M/population_count_M) * 100
df_stopped_M = data.frame(race_M, population_count_M,stopped_count_M, per_stopped_M)
head(df_stopped_M)

"""The following graph shows the 'Percentage of Male Individuals Stopped by Race with Respect to Population'"""

ggplot(df_stopped_M) +
  geom_col(aes(x=race_M, y = per_stopped_M))