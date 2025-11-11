file_read = open('codingal_report.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

#open the file in append mode
file_write = open('codingal_report.txt','w')

file_write.write(" File in write mode ....")
file_write.write("Hi! I am a penguin. i am 1 year old.")
file_write.close()

file_append = open('codingal_report.txt','a')
file_append.write("\n File in append mode ...")
file_append.write("Hi! i am a penguin. I am 1 year old.")
file_append.close()