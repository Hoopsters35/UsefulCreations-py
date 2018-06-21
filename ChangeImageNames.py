import os, re, shutil
exp = re.compile(('''
(\w+)
(\.)
(\w+)
'''), re.VERBOSE)
os.chdir('C:\\Users\\justi\\IdeaProjects\\Chess-Java\\Chess\\Images')
for file in os.listdir():
    name_cap = exp.match(file)
    words = name_cap.groups()
    new_name = words[0].upper() + words[1] + words[2]
    shutil.move(file, new_name)
