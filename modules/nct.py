import requests
import re
import reply

def process(sender, message):
    if message == 'nct:':
        reply.send(sender, "[Cú pháp] nct: <link bài hát NhacCuaTui>")
    else:
        parameter = message.replace("nct: ", "")
        url_valid = re.match("https?:\/\/www\.nhaccuatui\.com\/bai-hat\/[-.a-z0-9A-Z]+\.html", parameter)
        if url_valid:
            content = requests.get(parameter).text
            xml = re.search("https?:\/\/www\.nhaccuatui\.com\/flash\/xml\?key1=[0-9a-z]{30,40}", content).group(0)
            headers = {'content-type': 'application/xml'}
            xmlcontent = requests.get(xml, headers=headers).text
            link = re.search("https?:\/\/[^\/]+\.nixcdn\.com\/[-_\/a-zA-Z0-9]+\.mp3", xmlcontent).group(0)
            reply.send(sender, "[Download] "+link)
        else:
            reply.send(sender, "Bạn đã nhập sai rồi 😡")

