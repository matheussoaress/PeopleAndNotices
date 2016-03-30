from NoticeIR.Robot import Robot

threads = []

sites = []
sites.append(["globo","http://g1.globo.com/", "http://g1.globo.com/robots.txt"])
sites.append(["terra", "http://noticias.terra.com.br/brasil/", "http://www.terra.com.br/robots.txt"])
sites.append(["uol", "http://noticias.uol.com.br/", "http://www.folha.uol.com.br/robots.txt"])
sites.append(["folha", "http://www.folha.uol.com.br/", "http://www.folha.uol.com.br/robots.txt"])
sites.append(["r7", "http://noticias.r7.com/brasil", "http://www.r7.com/robots.txt"])
sites.append(["bol", "http://noticias.bol.uol.com.br/brasil/", "https://www.bol.com/robots.txt"])
sites.append(["ig", "http://ultimosegundo.ig.com.br/politica/", ""])
sites.append(["estadao", "http://www.estadao.com.br/", "http://www.estadao.com.br/robots.txt"])
sites.append(["ebc", "http://www.ebc.com.br/noticias", ""])

bots = []

for site in sites:
    bots.append(Robot(site=site[0], url=site[1], robotTxt=site[2]))

for bot in bots:
    bot.start()

for bot in bots:
    bot.join()