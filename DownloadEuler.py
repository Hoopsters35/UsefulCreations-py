"""Download all problems from the Project Euler site"""
#install beautiful soup first as well as selenium
import requests, bs4, selenium

number_of_problems = 619
#Navigate to website
url_base = 'https://projecteuler.net/problem={}'
dosctring = '"""Solution to problem {num} on project euler"""\n'
directory = "C:\\Users\\justi\\Python-Workspace\\ProjectEuler\\"
filename = 'problem{num}.py'

probnum = 1
for probnum in range(24, number_of_problems + 1):
    print('working on problem {}'.format(probnum))
    url = url_base.format(str(probnum))
    try:
        #Open URL
        site = requests.get(url)
        site.raise_for_status()

        #Open new file
        with open(directory + filename.format(num=probnum), 'w') as outfile:

            #Write the header
            outfile.write(dosctring.format(num=probnum))
            outfile.write('# ' + url + '\n\n')

            #Get the description
            bs = bs4.BeautifulSoup(site.text, "html5lib")
            content = bs.select('div.problem_content')
            description = bs4.BeautifulSoup(str(content), "html5lib").select('p')

            #Print each line of the description as a comment
            for paragraph in description:
                outfile.write('# ' + paragraph.getText() + "\n")


    except:
        print('Error loading problem number: ' + str(probnum))
        with open('eulerissues.txt', 'a') as errfile:
            errfile.write(str(probnum) + "\n")

print('done')



