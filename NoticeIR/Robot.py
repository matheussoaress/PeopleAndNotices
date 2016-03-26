import threading
import time
import urllib.robotparser
import urllib.request
import urllib.response
import html.parser

class Robot(threading.Thread):

    def __init__(self, site, url, robotTxt):
        threading.Thread.__init__(self)
        self.setRobotTxt(robotTxt)
        self.__list = [url]
        self.__viewed = []

    def setRobotTxt(self, robotTxt):
        self.__rp = urllib.robotparser.RobotFileParser()
        self.__rp.set_url(robotTxt)
        self.__rp.read()

    def __request(self, url):
        request = urllib.request.build_opener()
        request.add_header = [('User-agent', 'robotunibhmatheus')]
        return request.open(url)

    def __execute(self):
        num = 0
        while((len(self.__list)>0) and (num<20000)):
            url = self.__list.pop(0)
            if(self.__rp.can_fetch("*", url)):
                site = self.__request(url)
                if(site.status == 200):
                    self.__process(site.read().decode('utf-8'))
                self.__viewed.append(url)
                num+=1
            time.sleep(30)


    def __process(self, info):
        print('OK')
        pass

    def run(self):
        self.__execute()


site = "Globo.com"
url = "http://www.globo.com/"
robot = "http://g1.globo.com/robots.txt"

a = Robot(site=site, url=url, robotTxt=robot)
a.start()