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
sites.append(["ebc", "http://www.ebc.com.br/noticias", ""])
sites.append(["em", "http://www.em.com.br/", "http://www.em.com.br/robots.txt"])
sites.append(["exame", "http://exame.abril.com.br/", "http://exame.abril.com.br/robots.txt"])
sites.append(["reuters", "http://br.reuters.com/", "http://www.reuters.com/robots.txt"])

bots = []

for site in sites:
    bot = Robot(server=site[0], first_url=site[1], contin=True, history=True)
    bot.robot_txt(site[2])
    bots.append(bot)


for bot in bots:
    # bot.execute()
    bot.start()

for bot in bots:
    bot.join()