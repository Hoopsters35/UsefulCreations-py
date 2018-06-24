directory = "C:\\Users\\justi\\Python-Workspace\\ProjectEuler\\"
filename = 'problem{num}.py'

nums = []
with open('eulerissues.txt', 'r') as issuesdoc:
    nums = issuesdoc.readlines()

for probnum in nums:
    with open(directory + filename.format(num=probnum.rstrip('\n')), 'a') as outfile:
        outfile.write('\n\n# Initial issue loading problem, likely graphic on site')
