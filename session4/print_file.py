from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "../P0/sequences/RNU6_269P"  #the file has to be in the same directory

# -- Open and read the file
file_contents = Path(FILENAME).read_text() #reading the file

# -- Print the contents on the console
print(file_contents)