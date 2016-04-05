from html.parser import HTMLParser
import os

class HtmlProcess(HTMLParser):
    __links = []
    __content = {}
    __data = []
    exc = ('!','"','"','#','$','%','&','','(',')','*','+','-','.','/',':',';','<','=','>','?','@','[','\'','\\','\n','\t',']','^','_','`','a','abaixo','acima','acordo','ainda','além','ante','antes','ao','aos','apesar','após','assim','atenção','através','atrás','até','até','caso','causa','cima','com','como','conforme','consoante','contanto','contra','contudo','da','de','defronte','dela','dele','depois','desde','despeito','desta','deste','devido','disto','do','durante','e','em','embaixo','embora','entre','entretanto','face','favor','fim','frente','instâncias','junto','já','logo','longe','mas','mediante','medida','mesmo','na','naquela','naquele','nem','nessa','nesse','no','num','numa','não','obediência','obstante','ora','ou','par','para','pela','pelo','pena','per','perante','pois','por','porque','portanto','porém','proporção','quando','que','se','segundo','sem','sob','sobre','também','todavia','trás','virtude','visto','{','}','~','¢','£','§','¨','©','ª','¬','®','°','²','³','´','¹','º','ß','à','àquela','àquele','às','Ý','ý','Þ','þ')

    def process(self, content):
        try:
            self.feed(content)
        except Exception as e:
            self.__links = []
            print("Ocorreu um erro ao tentar processar o HTML. "+repr(e))

    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            name = value = None
            for attr in attrs:
                if attr[0] == 'name':
                    name = attr[1]
                if attr[0] == 'content':
                    value = attr[1]
                if value is not None and value.find('NOFOLLOW')>=0:
                    raise Exception('Erro ao seguir', 'Proibido capturar os links')
                if name is not None and value is not None:
                    self.__content[name]=value
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.__links.append(attr[1])

    def handle_data(self, data):
        content = data.split(" ")
        while len(content)>0:
            info = content.pop(0)
            if info not in self.exc:
                self.__data.append(info)

    def save(self, server, name, content):
        pre = "ÁáÂâÀàÅåÃãÄäÆæÉéÊêÈèËëÐðÍíÎîÌìÏïÓóÔôÒòØøÕõÖöÚúÛûÙùÜüÇçÑñ®©ÝýÞþß'\"!@#$%¨&*()_+=-¹²³£¢¬§`{}^<>:?´[~],.;/ªº°"
        pos = "AaAaAaAaAaAaEeEeEeEeEeEeIiIiIiIiOoOoOoOoOoOoUuUuUuUuUuNn_cYy__B________________123____________________aoo"
        trans = str.maketrans(pre, pos)
        name = name.translate(trans)
        path = "..\\Docs\\"+server+"\\"+name+".dtpn"
        try:
            if not os.path.exists("..\\Docs"):
                os.mkdir("..\\Docs")
            if not os.path.exists("..\\Docs\\"+server):
                os.mkdir("..\\Docs\\"+server)
            with open(path, 'wb') as fp:
                fp.write(content.encode('ascii', 'backslashreplace'))
                fp.close()
        except Exception as e:
            try:
                with open(path, 'wb') as fp:
                    fp.write(content.encode('utf-8', 'ignore'))
                    fp.close()
            except Exception as e:
                print("Erro ao salvar o arquivo. "+repr(e))

    def get_data(self):
        return self.__data

    def get_links(self):
        return self.__links