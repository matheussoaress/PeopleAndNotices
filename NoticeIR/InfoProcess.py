from html.parser import HTMLParser
import os
import binascii

class InfoProcess(HTMLParser):

    def __init__(self, site):
        try:
            HTMLParser.__init__(self)
            self.__links = []
            self.__site = site
            if not os.path.exists("..\\Docs"):
                os.mkdir("..\\Docs")
            if not os.path.exists("..\\Docs\\"+site):
                os.mkdir("..\\Docs\\"+site)
        except ValueError:
            print(ValueError)
        except Exception:
            print("Um erro desconhecido ocorreu no metodo InfoProcess.__init__")

    def setFile(self, name, file):
        try:
            self.save( file, name)
            self.feed(file)
        except ValueError:
            print(ValueError)
        except Exception:
            print("Um erro desconhecido ocorreu no metodo InfoProcess.setFile")

    def handle_starttag(self, tag, attrs):
        if(tag == 'a'):
            for attr in attrs:
                if attr[0] == 'href':
                    self.__links.append(attr[1])

    def save(self, file, name):
        try:
            fp = open("..\\Docs\\"+self.__site+"\\"+name+".dtpn", 'wb')
            fp.write(file.encode('ascii', 'backslashreplace'))
        except ValueError:
            print(ValueError)
        except Exception:
            print("Um erro desconhecido ocorreu no metodo InfoProcess.save")
        else:
            fp.close()

    def getLinks(self):
        return self.__links