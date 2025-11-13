file_read = open("sample_file.txt", "r")
print("File in Read Mode")
print(file_read.read())
file_read.close()

#open the file in write mode
file_write = open("sample_file.txt", "w")
file_write.write("File in write mode....")
file_write.write("This is a sample file for read and write demnstration.")
file_write.close()

#open the file in append mode and add some mre content
file_append = open("sample_file.txt", "a")
file_append.write("\nFile in append mode....")
file_append.write("The subjects i love most is as follows:")
file_append.write("\n1.Maths \n2.Physics \n3.Chemistry \n4.Biology \n5.ICT")
file_append.close()
