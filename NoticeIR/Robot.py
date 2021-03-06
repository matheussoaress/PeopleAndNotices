import threading
import time
import urllib.robotparser
import urllib.request
import urllib.response
import urllib.error
import hashlib
from NoticeIR.InfoProcess import InfoProcess

class Robot(threading.Thread):

    ''' 
    '  Método construtor da classe:
    '  @input String site
    '  @input String url
    '  @input String robotTxt
    '
    ''' 
    def __init__(self, site, url, robotTxt):
        try:
            threading.Thread.__init__(self)
            self.__robotTxt = False
            if robotTxt != '':
                self.setRobotTxt(robotTxt)
                self.__robotTxt = True
            self.__site = site
            self.__list = [url]
            self.__viewed = {}
            self.__content = {}
        except ValueError:
            print(ValueError)
        except Exception:
            print("Um erro desconhecido ocorreu no metodo Robot.__init__")

    '''
    '  Configura o protocolo de exclusão com base no endereço do Robots.txt
    '  @input String robotTxt
    '
    '''
    def setRobotTxt(self, robotTxt):
        try:
            self.__rp = urllib.robotparser.RobotFileParser()
            self.__rp.set_url(robotTxt)
            self.__rp.read()
        except ValueError:
            print(ValueError)
        except Exception:
            print("Um erro desconhecido ocorreu no metodo Robot.setRobot")

    '''
    '  Método reponsável por fazer a requisição do site para o servidor.
    '  @input String url
    '
    '  @return urllib.response
    '
    '''
    def __request(self, url):
        try:
            request = urllib.request.build_opener()
            request.add_header = [('User-agent', 'matheushssrobot/site:matheushsoaress.wordpress.com')]
            return request.open(url)
        except urllib.error.ContentTooShortError as e:
            print("Ocorreu um erro de Urllib: "+repr(e))
        except urllib.error.HTTPError as e:
            print("Ocorreu um erro de Urllib: "+repr(e))
        except urllib.error.URLError as e:
            print("Ocorreu um erro de Urllib: "+repr(e))
        except ValueError as e:
            print(repr(e))
        except Exception as e:
            print(repr(e))
            print("Um erro desconhecido ocorreu no metodo Robot.__request")

    '''
    '  Verifica se é possível capturar a url
    '  @input String url
    '
    '  @return boolean
    '''
    def __validaUrl(self, url):
        if self.__robotTxt:
            return self.__rp.can_fetch("*", url)
        else:
            return True

    '''
    '  Inicia a execução da busca, verifica se o site já foi buscado e faz o sistema esperar 30 segundos até a próxima requisição
    '
    '''
    def execute(self):
        try:
            num = 0
            while((len(self.__list)>0) and (num<200000)):
                try:
                    url = self.__list.pop(0)
                    print(url)
                    hs = hashlib.sha512()
                    hs.update(url.encode('ascii', 'backslashreplace'))

                    if((self.__validaUrl(url)) and (hs.hexdigest() not in self.__viewed) and (url.find(self.__site)>=0)):
                        site = self.__request(url)
                        if(site != None) and (site.status == 200):
                            hsC = hashlib.sha512()
                            content = site.read()
                            hsC.update(content)
                            if hsC.hexdigest() not in self.__content:
                                self.__process(url, content.decode('utf-8', 'backslashreplace'))
                                self.__content[hsC.hexdigest()] = url
                            else:
                                print("A url "+url+"ja joi capturada")
                        num+=1
                        time.sleep(30)
                    if hs.hexdigest() not in self.__viewed:
                        self.__viewed[hs.hexdigest()] = url
                except urllib.error.ContentTooShortError as e:
                    print("Ocorreu um erro de Urllib: "+repr(e))
                except urllib.error.HTTPError as e:
                    print("Ocorreu um erro de Urllib: "+repr(e))
                except urllib.error.URLError as e:
                    print("Ocorreu um erro de Urllib: "+repr(e))
                except ValueError as e:
                    print(repr(e))
                except Exception as e:
                    print(repr(e))
                    print("Um erro desconhecido ocorreu no loop e foi ignorado")
        except Exception as e:
            print(repr(e))
            print("Um erro desconhecido ocorreu no metodo Robot.execute que interrompeu o uso")


    '''
    '  Realiza o processamento texto do documento e adiciona os links achados na lista de espera
    '  @input String url
    '  @input String 
    '
    '''
    def __process(self, url, info):
        try:
            link = url.split("/")
            if link[len(link)-1]!= "":
                name = link[len(link)-1]
            else:
                name = link[len(link)-2]
            prs = InfoProcess(self.__site)
            prs.setFile(name, info)
            links = prs.getLinks()
            self.__list+=links
        except urllib.error.ContentTooShortError:
            print("Ocorreu um erro de Urllib")
        except urllib.error.HTTPError:
            print("Ocorreu um erro de Urllib")
        except urllib.error.URLError:
            print("Ocorreu um erro de Urllib")
        except ValueError:
            print(ValueError)
        except Exception:
            print("Um erro desconhecido ocorreu no metodo Robot.__process")

    '''
    '  Inicia a thread
    '
    '''
    def run(self):
        print(self.__site+" foi iniciado!")
        self.execute()
        print(self.__site+" foi finalizado!")