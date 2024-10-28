# Summarize the Data
summary(sunil)
test1 <- data.frame(
  course = c("BCA","MCA","BTech","M.Tech"),
  Age = c(25,30,28,40),
  addr = c("Delhi","Meerut","Khatauli","Noida")
)
test1[1]     # by using single bracket
test1[["course"]] # By using [[]] double bracket
test1$course   # By using $ sign
# add rows  rbind()
school <- rbind(test1,c("DPS","MPS","DDPS","RKGIT"))
school
test1
# add new column in a data frame cbind()
name <- cbind(test1,name = c("Sumit","mohit","tarun","vikas"))
name
# Remove Rows and Columns
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

# Remove the first row and column
Data_Frame_New <- Data_Frame[-c(1), -c(1)]
Test_new <- test1[-c(1),]
# Print the new data frame
Test_new
# Amount of Rows and Columns
dim(test1)
# ncol() columns and nrow() to find the number of rows:
ncol(test1)
nrow(test1)
# to find the number of column :
length(test1)
# Combining Data Frames

sunil <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

amit <- data.frame (
  Training = c("Stamina", "Stamina", "Strength"),
  Pulse = c(140, 150, 160),
  Duration = c(30, 30, 20)
)

New_Data_Frame <- rbind(sunil, amit, test1)
New_Data_Frame
