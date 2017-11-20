
def word_checker(self, url, word):
    from bs4 import BeautifulSoup
    import requests

    r = requests.get(url)
    result = ""
    soup = BeautifulSoup(r.content, 'lxml')

    for link in soup.find_all('li'):
        #  https://stackoverflow.com/questions/34077659/cant-find-string-in-text-file
        if any(word.lower() in line for line in link):
            result += link.text + " "
        if any(word in line for line in link ):
            result += link.text + " "
    if result != "":
        return result[:len(result) -1] # to eliminate the last empty char
    return "No"
