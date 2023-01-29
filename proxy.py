from flask import Flask
import yaml, json

app = Flask(__name__)

@app.route("/conf1")
def conf1():
    import requests
    url = "http://95.217.10.184:9999/"
    res = requests.get(url)
    datas = yaml.load(res.content.decode(encoding="utf-8"), Loader=yaml.FullLoader)
    with open("conf.json", "w") as f:
        f.write(json.dumps(datas))
    with open("conf.json", "r", encoding="utf-8") as f:
        datas = json.load(f)
        yamlDatas = yaml.dump(datas, indent=5, sort_keys=False)
    return yamlDatas

@app.route("/conf2")
def conf2():
    import requests
    url = "http://106.75.10.21:9001/"
    res = requests.get(url)
    datas = yaml.load(res.content.decode(encoding="utf-8"), Loader=yaml.FullLoader)
    with open("conf.json", "w") as f:
        f.write(json.dumps(datas))
    with open("conf.json", "r", encoding="utf-8") as f:
        datas = json.load(f)
        yamlDatas = yaml.dump(datas, indent=5, sort_keys=False)
    return yamlDatas

@app.route("/conf3")
def conf3():
    import requests
    url = "http://154.31.50.37/"
    res = requests.get(url)
    datas = yaml.load(res.content.decode(encoding="utf-8"), Loader=yaml.FullLoader)
    with open("conf.json", "w") as f:
        f.write(json.dumps(datas))
    with open("conf.json", "r", encoding="utf-8") as f:
        datas = json.load(f)
        yamlDatas = yaml.dump(datas, indent=5, sort_keys=False)
    return yamlDatas

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000)



