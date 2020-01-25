2+2

# Everything after a hashtag is a "comment"

# It's not execiuted as computer code

# Be sure to always comment your code so that
#later, your remember what the heck is going on!

# often, we want to save stuff
# do this with the "assignment" operator

#       <-  

23.545612


# Let's store this long number as a variable
# PIck a name:  numberIcareAbout

numberIcareAbout <- 23.545612

numberIcareAbout

a <- 2
b <- 6


a+b


# R has lots of built-in datasets for experimentation

# Let's look at the "iris" dataset.  It's a built-in dataset
# that contains measurments taken about 150 iris flowers in 
# the 1950s

head(iris)


# I want a histogram of the sepal lengths for iris

# first, here's how choose a variable.  do it with "$"

iris$Sepal.Length

hist(iris$Sepal.Length)

# Sultan's question:  what's wrong

hist(iris$Petal.Length)

head(iris)

# The above are examples of "functions"

# the name comes first

# the "input" comes in the ()

# The inputs are called "arguments"

#Some functions take multiple agruments

#Ex:  make a scatterplot of petal length and 
# petal width:

plot(iris$Petal.Length, iris$Petal.Width)

# SPot the mistake:

plot(iris$Petal.Length, iris$Petal.Length)

# the above is a great reason to always use scripts!!


# Other useful functions: mean, median, mode, stdev
# Most of them have easy-to guess names

# Example: find the mean sepal length of iris


mean(iris$Sepal.Length)

# Example:  find the standard deviation of sepal length

standarddeviation(iris$Sepal.Length)

sd(iris$Sepal.Length)


# Last cool function: summary

summary(iris$Sepal.Length)


# Packages are collection of functions that we load in 
# to the R environment

# Packages let us add new functions (thus, new capability)
# to R

# Two steps to loading a package.  

# First, install.  I do this in the console, becuase
# you only do it once.  

# Second, you need to import it into your environment
# Do this with the "library()" command.

library(dplyr)


## ONe of the coolest features of dplyr is the
# "pipe"   

#  Sybol:    %>%  

# We use the pipe to "chain together" output

hist(iris$Sepal.Length)

# we could do this with a pipe:

iris$Sepal.Length %>% hist

# These are identical!

# If you need to perform multiple operations on
# data, pipes are way easier.  We'll see examples

library(ggplot2)

# Example:  Let's use ggplot to make a histogram 
# of iris sepal lengths

ggplot(iris, aes(Sepal.Length))+
  geom_histogram()


# Example:  scatter plot of sepal length vs
# sepal width

ggplot(iris, aes(Sepal.Length, Sepal.Width))+
  geom_point()

icouldcallthiswhatev <- read.csv("GarlicMustardData.csv")

View(icouldcallthiswhatev)

icouldcallthiswhatev

help(geom_point)


ggplot(iris, aes(Sepal.Length))+
  geom_histogram()+
  labs(title="This is an example")

unique(GarlicMustardData$Region)

