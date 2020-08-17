## Set working directory
## Next, read csv

deathData <- read.csv("death-penalty-data.csv")

View(deathData)


mean(deathData$Age)

barplot(table(iris$Species), xlab="test", main="test")

plot(iris$Sepal.Length,
     iris$Sepal.Width,
     xlab="my x label",
     ylab="my y label",
     main= "the title of my graph")
