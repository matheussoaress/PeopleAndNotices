from html.parser import HTMLParser
from html.entities import codepoint2name

class InfoProcess(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__links = []

    def setFile(self, file, name):
        self.save( file, name)
        self.feed(file)

    def handle_starttag(self, tag, attrs):
        if(tag == 'a'):
            for attr in attrs:
                if attr[0] == 'href':
                    self.__links.append(attr[1])

    def save(self, file, name):
        fp = open(name)
        fp.write(file)