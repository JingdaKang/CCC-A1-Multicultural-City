import json

geo_info = []
with open("D:/Documents/Tencent Files/879829366/FileRecv/UoM master course/Cluster and Cloud Computing/A1/smallTwitter.json", 'r', encoding="utf-8") as f:

    # line = f.readlines()[1]
    
    line = f.readline()
    try:
        while True:
            line = f.readline()
            dict = json.loads(line.strip('\n').strip(','))
            tweets = {}

            if (dict['doc']['geo']!=None):
                tweets['geo'] = dict['doc']['geo']
                tweets['cor'] = dict['doc']['coordinates']
                geo_info.append(tweets)
    except:
        print(geo_info)
        print(len(geo_info))

        # print(dict['doc']['metadata']['iso_language_code'])
        # print(dict['doc']['user'])
        # print(dict['doc']['geo'])
        # print(dict['doc']['coordinates'])
        # print(dict['doc']['user']['geo_enabled'])
with open("D:/Documents/Tencent Files/879829366/FileRecv/UoM master course/Cluster and Cloud Computing/A1/smallTwitter.json", encoding="utf-8") as f:

    # line = f.readlines()[1]

    line = f.readline()
    try:
        while True:
            line = f.readline()
            dict = json.loads(line.strip('\n').strip(','))
            tweets = {}

            if (dict['doc']['geo']!=None):
                tweets['geo'] = dict['doc']['geo']
                tweets['cor'] = dict['doc']['coordinates']
                geo_info.append(tweets)
    except:
        print(geo_info)
        print(len(geo_info))


