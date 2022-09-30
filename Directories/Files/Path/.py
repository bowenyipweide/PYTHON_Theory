#How to read an open file:
with open("my_flie.txt", mode="r/w/a" ) as file: 
  contents = file.read() or file.write() or file.append #respectively
  print(contents)
  #If file opened weren't created before, it will create a new file.
  
#Absolute file path 
/
/work
/work/report.doc 
/work/project
/work/project/talk.ppt

#Relative file path
./talk.ppt #./ means look into this file in the current folder
../ report.doc


example 

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
  names = names_file.read()
  
with open("./Input/Letters/starting_letter.txt") as letter_file: 
  letter_contents = letter_file.read()
  for name in names: 
    new_letter = letter_conetents.replace(PLACEHOLER, name)
    
  
