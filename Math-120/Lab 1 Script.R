# Hashtags make comments

# Comments aren't executed as code.  They're for us humans to 
# know what's going on!

2+2

3+5

# ANy time you want to actually *do* something in R, you 
# use a function.  

# Example: sqrt(5)  Note:  this is a function called sqrt

sqrt(5)

(4.2-3.6)/(1.8/sqrt(40))

# Note: if + in console, click and escape!  Try again!

# To make R "remember" stuff, we need to assign it to a
# variable

# to do this, use     <-     (an arrow)

# example: save "5" as variable "a"

a <- 5

b <- 7

a+b

#  We work with tidy data (rectangular data).  It's stored 
# as a matrix

# Example: the iris dataset.  Built-in data, measurements of
# 150 iris flowers

# best command for looking at data:  head.  It returns the
# first few rows

head(iris)

# What are the variables?  Use colnames()

colnames(iris)

# we can choose entries using [].  First row, then column.

iris[2,2]

# usually, we'll want a whole variable.  Choose variables 
# with $

iris$Sepal.Length


# Example:  find the mean Sepal Length in iris

mean(iris$Sepal.Length)

# Usually, function names are easy to guess.  But sometimes
# you might not know!

# Example: standard deviation

standarddeviation(iris$Sepal.Length)

# What to do?  Answer:  google is your friend

# Exercise:  find standard deviation of Sepal Length

# function name: sd

sd(iris$Sepal.Length)

# A particularly useful function: summary()

# Example:  summary of iris sepal length

summary(iris$Sepal.Length)

# How we can we add funcionality to R?  Sometimes old tools 
# Get replaced with new.

# The answer:  libraries.  Libraries are packages/collections
# of functions.  Downloading them lets you expands the 
# capabilities of the software.

# Two steps:  first download with install.packages()

# install.packages("tidyverse")

# Step two: load it with the "library" command

library(tidyverse)

#Plotting:  plot for scatterplot, hist for histogram, barplot 

#Example:  Make a histogram of sepal length in iris data

hist(iris$Sepal.Length, breaks=20)


# Example:  make a scatterplot of Sepal Length vs Sepal Width
# Is there a relationship?

plot(iris$Sepal.Length, iris$Sepal.Width)

# Feelings:  weird that there doesn't seem to be a relationship
# Idea:  what if species is obscuring the relation?

head(iris)
table(iris$Species)

# Neat trick:  use color!

plot(iris$Sepal.Length, iris$Sepal.Width, col=iris$Species)

# Woah!  Looks like individual species *do* show relation

# Examine the subset

setosaData <- subset(iris, Species == "setosa")

plot(setosaData$Sepal.Length, setosaData$Sepal.Width)
