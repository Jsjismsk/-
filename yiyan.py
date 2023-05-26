import requests
import json

url = "https://api.wrdan.com/hitokoto"
text = open('1.txt', 'w', )#新建文件
temp=''

for i in range(1,888):
    back = requests.get(url)
    back = back.content.decode("unicode_escape")
    back = json.loads(back)

    if(back!=temp):
        text = open('1.txt', 'a', encoding='UTF-8')  # a,追加模式
        text.write(f"{i}: {back['text']}\n")
        temp=back
    else:
        i=i-1
        continue


    print(back["text"])

    text.close()

