pdf("age_plot.pdf")
mydata=read.table("cd.list",sep="\t",header = FALSE)
plot(mydata$V2,mydata$V1, main = "Plot for mementos with ages", 
     xlab = "number of mementos", ylab = "days of age")
dev.off()