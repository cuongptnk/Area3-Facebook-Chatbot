import requests
import re
import json
import reply

def process(sender, message):
    if message == 'fb:':
        reply.send(sender, "[Cú pháp] fb: <link video Facebook>")
    else:
        parameter = message.replace("fb: ", "")
        url_valid = re.match("https?:\/\/www\.facebook\.com\/[.\w\s]{6,30}\/videos\/[0-9]{10,18}\/(.+)?", parameter)
        if url_valid:
            id = re.search("([0-9]{10,18})", parameter).group(1)
            s = requests.get('https://www.facebook.com/video/embed?video_id='+id).text
            content = s[s.index('"videoData":[')+len('"videoData":['):s.index('],"minQuality":')]
            decoded = json.loads(content)
            if not decoded['sd_src']:
                reply.send(sender, "[HD quality] "+decoded['hd_src'])
            elif not decoded['hd_src']:
                reply.send(sender, "[SD quality] "+decoded['sd_src'])
            else:
                reply.send(sender, "[SD quality] "+decoded['sd_src'])
                reply.send(sender, "[HD quality] "+decoded['hd_src'])
        else:
            reply.send(sender, "Bạn đã nhập sai rồi 😡")