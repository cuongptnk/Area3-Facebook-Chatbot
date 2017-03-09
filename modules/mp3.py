import requests
import re
import json
import reply

def process(sender, message):
    if message == 'mp3:':
        reply.send(sender, "[Cú pháp] mp3: <link bài hát Zing Mp3>")
    else:
        parameter = message.replace("mp3: ", "")
        url_valid = re.match("(https?:\/\/)?mp3\.zing\.vn\/bai-hat\/[\w\d\-]+/([\w\d]{8})\.html", parameter)
        if url_valid:
            string_valid = re.search("([A-Z0-9]{8})", parameter).group(1)
            content = requests.get('http://phulieuminhkhang.com/images/Sanpham/api.php?parameter='+string_valid).text
            decoded = json.loads(content)
            reply.send(sender, "Bài hát: "+decoded['title']+", Ca sĩ: "+decoded['artist'])
            reply.send(sender, "[128Kbps] "+decoded['link_download']['128'])
            reply.send(sender, "[320Kbps] "+decoded['source']['320'])
        else:
            reply.send(sender, "Bạn đã nhập sai rồi 😡")