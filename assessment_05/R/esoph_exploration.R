# Inspect the esoph built-in data set
esophData <- esoph
dataDim <- dim(esophData)
cat("The esoph data set has", dataDim[1], "rows and", dataDim[2], "columns.")
cat("The colnames are the following:")
colnames(esophData)

cat("All entries from the esoph data set ordered by the amount of cancer cases: ")
esophCases <- esophData[order(esophData$ncases),order(esophData$ncontrols),]
esophCases

cat("The summary from the esoph data set: ")
summary(esophData)
