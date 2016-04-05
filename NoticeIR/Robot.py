from threading import Thread
from NoticeIR.HtmlProcess import HtmlProcess
import time
import urllib.robotparser
import urllib.request
import urllib.response
import urllib.error
import hashlib
import os
import json

class Robot(Thread):
    __rp = None
    __links = []
    __viewed = {}

    def __init__(self, server, first_url, contin=True, history=False):
        Thread.__init__(self)
        self.__server = server
        self.__first_url = first_url
        self.__links.append(first_url)
        if contin:
            self.__load_list()
        if history:
            self.__load_history()

    def __load_history(self):
        try:
            path = "..\\Docs\\"+self.__server
            if os.path.isfile(path+"\\history.dtph"):
                with open("..\\Docs\\history", 'r') as fp:
                    self.__viewed = json.load(fp)
                    fp.close()
        except Exception as e:
            print("Erro ao abrir arquivo de historico. "+repr(e))

    def __write_history(self):
        try:
            path = "..\\Docs\\"+self.__server
            if os.path.exists(path):
                with open(path+"\\history.dtph", 'w') as fp:
                    info = json.dumps(self.__viewed)
                    fp.write(info)
                    fp.close()
        except Exception as e:
            print("Erro ao gravar arquivo de historico. "+repr(e))

    def __load_list(self):
        try:
            path = "..\\Docs\\"+self.__server
            if os.path.isfile(path):
                with open(path+"\\nlinks.dtph", 'r') as fp:
                    self.__links = json.load(fp)
                    fp.close()
        except Exception as e:
            print("Erro ao carregar arquivo de próximos links. "+repr(e))

    def __save_list(self):
        try:
            path = "..\\Docs\\"+self.__server
            if os.path.exists(path):
                with open(path+"\\nlinks.dtph", 'w') as fp:
                    info = json.dumps(self.__links)
                    fp.write(info)
                    fp.close()
        except Exception as e:
            print("Erro ao gravar arquivo de próximos links. "+repr(e))

    def robot_txt(self, url):
        try:
            if url != "":
                self.__rp = urllib.robotparser.RobotFileParser()
                self.__rp.set_url(url)
                self.__rp.read()
        except Exception as e:
            print('Um erro ocorreu ao tentar fazer parse do robot.txt.'+repr(e))

    def __request(self, url):
        try:
            request = urllib.request.build_opener()
            request.add_header = [('User-agent', 'robotunibhmatheus')]
            return request.open(url)
        except urllib.error as e:
            print("Ocorreu um erro ao fazer a requisicao da Url "+url+". "+repr(e))
        except Exception as e:
            print("Ocorreu um erro ao fazer a requisicao da Url "+url+". "+repr(e))

    def __test_url(self, url):
        if self.__rp is not None:
            return self.__rp.can_fetch("*", url)
        else:
            return True

    def __processUrl(self, server, url, content):
        try:
            aux = url.split("/")
            name = aux[len(aux)-1] if aux[len(aux)-1] != "" else aux[len(aux)-2]
            processor = HtmlProcess()
            processor.save(server, name, content)
            processor.process(content)

            self.__links += processor.get_links()

        except Exception as e:
            print("Ocorreu um erro ao processar a Url."+repr(e))

    def execute(self):
        try:
            cnt = 0
            while (cnt < 200000) and (len(self.__links) > 0):
                url = self.__links.pop(0)
                print(url)
                uHash = hashlib.sha512()
                uHash.update(url.encode('ascii', 'backslashreplace'))

                a = self.__test_url(url)
                b = (uHash.hexdigest() not in self.__viewed)
                c = (url.find(self.__server)>=0)

                if a and b and c:
                    try:
                        page = self.__request(url)
                        if (page is not None) and (page.status == 200):
                            content = page.read().decode('utf-8', 'backslashreplace')
                            self.__processUrl(self.__server, url, content)
                        time.sleep(30)
                        cnt += 1
                    except Exception as e:
                        print("Ocorreu um erro que foi ignorado. "+repr(e))
                if uHash.hexdigest() not in self.__viewed:
                    self.__viewed[uHash.hexdigest()] = url
            self.__save_list()
            self.__write_history()
        except Exception as e:
            print("Ocorreu um erro que finalizou a execucao. "+repr(e))

    def run(self):
        print("Iniciando processamento de "+self.__server)
        self.execute()
        print("Finalizado processamento de "+self.__server)