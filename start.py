from os import system as cmd 
import json

def updateNodes(url):
    with open("./config_template/providers.json") as prov:
        data = json.load(prov)
    for subscribe in data['subscribes']:
        if subscribe['tag'] == 'tag_1':
            subscribe['url'] = url
            break
    print(data)
    with open("./providers.json", "w") as prov:
        json.dump(data, prov, indent=4, ensure_ascii=False)

updateNodes(getenv('subLink')) #TODO: using flask finish here
cmd("python3 main.py --template_index=0")
cmd("./sing-box run")
