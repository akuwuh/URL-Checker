import random
from urllib import request
from time import sleep
from threading import Thread

allchar = []

base_url = 'http://steamcommunity.com/groups/'

zebi = 'abcdefghijklmnopqrstuvwxyz'

def pad_right(string, n_chars):
    return string + (' ' * (n_chars - len(string)))

#initializing web browser search
class Id:
    def __init__(self, url):
        req = request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        html = request.urlopen(req).read().decode('utf-8')
        self.exist = not 'No group could be retrieved for the given URL.' in html


#Search algorithm
def loop1():
    while True:
        #concatenating base url with 3 random letters
        url = base_url + random.choice(zebi)+random.choice(zebi)+random.choice(zebi)
        
        if not url in allchar:
            try:
                allchar.append(url)
                curr = Id(url)
                url_space = len(base_url) + 1
                url = pad_right(url, url_space)
                if not curr.exist:
                    print(f'{url} | not taken')
                    with open("results.txt", "a") as file:
                        file.write(str(url)+"\n")
                else:
                    print(f'{url} | taken')
            except:
                pass
    

if __name__ == '__main__':
    
    for i in range(0, 100):
        thread = Thread(target=loop1)
        thread.start()
