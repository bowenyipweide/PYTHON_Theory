#How to read an open file:
with open("my_flie.txt", mode="r/w/a" ) as file: 
  contents = file.read() or file.write() or file.append #respectively
  print(contents)
  #If file opened weren't created before, it will create a new file.
