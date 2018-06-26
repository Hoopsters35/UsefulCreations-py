import requests, bs4, re

comic_num_regex = re.compile(r'''(
(/)
(\d+)
(/$)
)''', re.VERBOSE)

next_comic_exists = True

#Starting URL
URL = 'http://explosm.net/comics/oldest'

while(next_comic_exists):
    #Get site
    site = requests.get(URL)
    site.raise_for_status()

    source = bs4.BeautifulSoup(site.text)

    #Download image
    image_url = 'http:' + source.select('#main-comic')[0].get('src')
    image = requests.get(image_url)

    comic_num = comic_num_regex.findall(source.select('meta[property=og:url]')[0].get('content'))[0][2]
    print('Downloading comic #{}'.format(comic_num))
    file_loc = './CyanideAndHappiness/{}'.format(comic_num)

    #Write the image to a file
    with open(file_loc, 'wb') as write_file:
        for chunk in image.iter_content(100000):
            write_file.write(chunk)

    #Keep going until the next button no longer works
    next_comic_exists = source.select('a[title="Next comic"]')[0].get('class') is not 'nav-next disabled'

    #Get the next URL
    if (next_comic_exists):
        URL = 'http://explosm.net' + source.select('a[title="Next comic"]')[0].get('href')