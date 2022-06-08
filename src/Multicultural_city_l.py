import json
from collections import Counter
from src.Grid_extraction import findGrid, extracGrid

tweets = [] # an array storing all eligible tweets for debugging, can be deleted in the final version
grid_file = "D:/Documents/Tencent Files/879829366/FileRecv/UoM master course/Cluster and Cloud Computing/A1/sydGrid-2.json"
Grid_info = extracGrid(grid_file) # a dict contains grid id and its coordinates e.g. {23: {'tl': [151.2155, -33.85412], 'bl': [151.2155, -34.00412], 'br': [151.3655, -34.00412], 'tr': [151.3655, -33.85412]}, ...}

# final global dict for statistical data for multicultral nature of Sydney  !should be stored in the master(head node)!
# 'languages' stores all the languages and the count number e.g. 'languages':{'en':2,'cn':1, ...}
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
#
# with open(
#         "D:/Documents/Tencent Files/879829366/FileRecv/UoM master course/Cluster and Cloud Computing/A1/tinyTwitter.json",
#         encoding="utf-8") as f:
#     dict = json.load(f) # load json file: str --> dict
#
#     for row in dict['rows']:
#         tweet = {} # e.g. {'cell':A1, 'lan':'en'}
#         if row['doc']['geo'] != None:
#             tweet['cell'] = findGrid(Grid_info, row['doc']['coordinates']['coordinates'])
#             if tweet['cell'] != None:
#                 tweet['lan'] = row['doc']['metadata']['iso_language_code']
#                 if tweet['lan'] != None or tweet['lan'] != 'und':
#                     multicul[tweet['cell']]['TotalTweets'] += 1
#                     if tweet['lan'] == 'zh-cn' or tweet['lan'] == 'zh-tw': tweet['lan'] = 'cn' # convert 'zh-cn' and 'zh-tw' -> 'cn'
#                     if tweet['lan'] in multicul[tweet['cell']]['languages']: multicul[tweet['cell']]['languages'][tweet['lan']] += 1
#                     else:
#                         multicul[tweet['cell']]['languages'][tweet['lan']] = 1
#                         multicul[tweet['cell']]['NumberofLanguagesUsed'] += 1
#
#                     multicul[tweet['cell']]['Top10Languages-Tweets'] = Counter(multicul[tweet['cell']]['languages']).most_common(10)
#                     tweets.append(tweet)
#
#     # print(tweets)
    # print(len(tweets))
    # print(dict['doc']['metadata']['iso_language_code'])
    # print(dict['doc']['user'])
    # print(dict['doc']['geo'])
    # print(dict['doc']['coordinates'])
    # print(dict['doc']['user']['geo_enabled'])
with open(
        "D:/Documents/Tencent Files/879829366/FileRecv/UoM master course/Cluster and Cloud Computing/A1/smallTwitter.json",
        encoding="utf-8") as f:

    dict = json.load(f) # load json file: str --> dict

    for row in dict['rows']:
        tweet = {}  # e.g. {'cell':A1, 'lan':'en'}
        if row['doc']['geo'] != None:
            tweet['cell'] = findGrid(Grid_info, row['doc']['coordinates']['coordinates'])
            if tweet['cell'] != None:
                tweet['lan'] = row['doc']['metadata']['iso_language_code']
                if tweet['lan'] != None or tweet['lan'] != 'und':
                    multicul[tweet['cell']]['TotalTweets'] += 1
                    if tweet['lan'] == 'zh-cn' or tweet['lan'] == 'zh-tw': tweet[
                        'lan'] = 'cn'  # convert 'zh-cn' and 'zh-tw' -> 'cn'
                    if tweet['lan'] in multicul[tweet['cell']]['languages']:
                        multicul[tweet['cell']]['languages'][tweet['lan']] += 1
                    else:
                        multicul[tweet['cell']]['languages'][tweet['lan']] = 1
                        multicul[tweet['cell']]['NumberofLanguagesUsed'] += 1

                    multicul[tweet['cell']]['Top10Languages-Tweets'] = Counter(
                        multicul[tweet['cell']]['languages']).most_common(10)
                    tweets.append(tweet)
print(tweets)
print(len(tweets))
print(multicul)