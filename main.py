#create a new file
new_file = open('nemfile.txt', 'x')
new_file.close()

#check if a fie exists
import os
print("checking if my_file exists or not....")
if os.path.exists("file.txt"):
    os.remove("file.txt")
    else:
        print("The file does not exist")

        #create a new if it doesn't
        my_file = open("newfile.txt","w")
        my_file.write("Hi! I am Ebuka and I am 20 yr old.")
        my_file.close()

        #delete file named codingal
        os.remove("file.txt")

        #delete the folder
        os.rmdir('folder')