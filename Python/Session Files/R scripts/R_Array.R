# R-array
thisarray <- c(1:24)      # single dimension array
thisarray
# More than one dimension array
multiarray <- array(thisarray, dim = c(4, 3, 2))
multiarray

# R-Data frame
sunil <- data.frame (
  student = c("Amit","Sumit","Tarun","Vivek"),
  age = c(25,30,35,50),
  course =c("BCA","MCA","B.Tech","MTech")
)
sunil
