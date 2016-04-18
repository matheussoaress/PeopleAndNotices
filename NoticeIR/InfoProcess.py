from html.parser import HTMLParser
import os
import binascii

class InfoProcess(HTMLParser):

    ''' 
    '  Método construtor da classe:
    '  @input String site
    '
    '''
    def __init__(self, site):
        try:
            HTMLParser.__init__(self)
            self.__links = []
            self.__meta = []
            self.__site = site
            if not os.path.exists("..\\Docs"):
                os.mkdir("..\\Docs")
            if not os.path.exists("..\\Docs\\"+site):
                os.mkdir("..\\Docs\\"+site)
        except ValueError:
            print(ValueError)
        except Exception:
            print("Um erro desconhecido ocorreu no metodo InfoProcess.__init__")

    ''' 
    '  Inicia o processamento do documento e o salva
    '  @input String name
    '  @input String file
    '
    '''
    def setFile(self, name, file):
        try:
            self.save( file, name)
            self.feed(file)
        except ValueError:
            print(ValueError)
        except Exception:
            print(Exception.mro())

    ''' 
    '  Captura as tags e seus atributos e verifica se o site pode ser coletado.
    '  @input String tag
    '  @input String attrs
    '
    '''
    def handle_starttag(self, tag, attrs):
        if(tag == 'meta'):
            for attr in attrs:
                if attr[0] == 'content':
                    atInfo = attr[1]
                    if atInfo.find('NOFOLLOW')>=0:
                        raise Exception("Site não coletavel")
                    else:
                        self.__meta.append(attr[1])

        if(tag == 'a'):
            for attr in attrs:
                if attr[0] == 'href':
                    self.__links.append(attr[1])
    ''' 
    '  Sava o documento no disco
    '  @input String file
    '  @input String name
    '
    '''
    def save(self, file, name):
        try:
            pre = "ÁáÂâÀàÅåÃãÄäÆæÉéÊêÈèËëÐðÍíÎîÌìÏïÓóÔôÒòØøÕõÖöÚúÛûÙùÜüÇçÑñ®©ÝýÞþß'\"!@#$%¨&*()_+=-¹²³£¢¬§`{}^<>:?´[~],.;/ªº°"
            pos = "AaAaAaAaAaAaEeEeEeEeEeEeIiIiIiIiOoOoOoOoOoOoUuUuUuUuUuNn_cYy__B________________123____________________aoo"
            trans = str.maketrans(pre, pos)
            name = name.traslate(trans)
            with open("..\\Docs\\"+self.__site+"\\"+name+".dtpn", 'wb') as fp:
                fp.write(file.encode('ascii', 'backslashreplace'))
        except ValueError:
            print(ValueError)
        except Exception:
            try:
                with open("..\\Docs\\"+self.__site+"\\"+name+".dtpn", 'wb') as fp:
                    fp.write(file.encode('utf-8', 'ignore'))
            except Exception as e:
                print(repr(e))
                print("Um erro desconhecido ocorreu no metodo InfoProcess.save")
            else:
                fp.close()
        else:
            fp.close()

    ''' 
    '  Retorna a lista de links capturados
    '
    '  @return String[]
    '
    '''
    def getLinks(self):
        return self.__links
        
    ''' 
    '  Retorna a lista de metadados capturados
    '
    '  @return String[]
    '
    '''
    def getMeta(self):
        return self.__meta