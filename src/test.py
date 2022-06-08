import json
from collections import Counter
import time


with open("D:/Documents/Tencent Files/879829366/FileRecv/UoM master course/Cluster and Cloud Computing/A1/ttinyTwitter.json", 'r', encoding='utf-8') as f:

    #line_number = 1 # record the number of lines read
    for line_number,line in enumerate(f):
        if line.endswith(',\n'):
            li = json.loads(line[:-2])
            print(li)
        if line.endswith(']}\n'):
            li = json.loads(line[:-3])
            print(li)
multicul = {'A1':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'A2':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'A3':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'A4':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'B1':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'B2':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'B3':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'B4':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'C1':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'C2':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'C3':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'C4':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'D1':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'D2':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'D3':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                'D4':{'TotalTweets':0, 'NumberofLanguagesUsed':0, 'Top10Languages-Tweets':[], 'languages':{}},
                }
print(list(multicul.keys()))
d={'b':1,'c':6}
d1={'b':1,'c':5}

print(d==d1)