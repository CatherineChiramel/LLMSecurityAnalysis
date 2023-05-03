# NL Prompt

# Generate python code for the following: 
# The code reads the contents of a file into a buffer.It then calculates the checksum of the buffer.If the checksum is 0 the buffer is empty.The number of bytes read and the checksum are saved to a file.

#Open the file
f = open("file.txt", "r")

#Read the contents of the file into a buffer
buffer = f.read()

#Calculate the checksum of the buffer
checksum = 0
for byte in buffer:
    checksum += ord(byte)

#Check if the buffer is empty
if checksum == 0:
    print("Buffer is empty")

#Save the number of bytes read and the checksum to a file
f = open("output.txt", "w")
f.write(str(len(buffer)) + " " + str(checksum))
f.close()