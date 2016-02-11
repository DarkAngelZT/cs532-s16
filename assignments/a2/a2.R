pdf("momento_plot.pdf")
mydata=read.table("momento_R.list",sep="\t",header = FALSE)
h = hist(mydata$V1, plot = F
     )
h$counts=log10(h$counts+1)
plot(h,ylim = c(0,log10(900)), main = "Histogram for momentos", 
     xlab = "number of momentos", ylab = "number of urls(in log10)")
dev.off()