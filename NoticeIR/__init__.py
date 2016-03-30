from NoticeIR.Robot import Robot

threads = []

site = "globo.com"
url = "http://www.globo.com/"
robot = "http://g1.globo.com/robots.txt"

a = Robot(site=site, url=url, robotTxt=robot)
a.start()
threads.append(a)

site = "terra.com.br"
url = "http://www.terra.com.br/"
robot = "http://www.terra.com.br/robots.txt"

b = Robot(site=site, url=url, robotTxt=robot)
b.start()
threads.append(b)

site = "uol.com.br/"
url = "http://www.uol.com.br/"
robot = "http://www.folha.uol.com.br/robots.txt"

c = Robot(site=site, url=url, robotTxt=robot)
c.start()
threads.append(c)

site = "folha.uol.com.br/"
url = "http://www.folha.uol.com.br/"
robot = "http://www.folha.uol.com.br/robots.txt"

d = Robot(site=site, url=url, robotTxt=robot)
d.start()
threads.append(d)

for tr in threads:
    tr.join()

