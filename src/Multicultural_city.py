import json
import time
from mpi4py import MPI
from collections import Counter
from Grid_extraction import findGrid, extracGrid


def twitter_lines(twitter_file):
    with open(twitter_file, 'r', encoding='utf-8') as f:
        first_line = f.readline()
        first_line = first_line.replace(first_line[-10:], '}')
        dict = json.loads(first_line)
        return dict["total_rows"] - dict["offset"]


def twitter_analyze(row, grid_info, multicul):
    if row['doc']['geo'] != None:
        cell = findGrid(grid_info, row['doc']['coordinates']['coordinates'])
        if cell != None:
            lan = row['doc']['metadata']['iso_language_code']
            if lan != None and lan != 'und':
                multicul[cell]['TotalTweets'] += 1
                if lan in multicul[cell]['languages']:
                    multicul[cell]['languages'][lan] += 1
                else:
                    multicul[cell]['languages'][lan] = 1
    return multicul


def main(twitter_file, grid_info):
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()
    # final global dict for statistical data for multicultral nature of Sydney  !should be stored in the master(head node)!
    # 'languages' stores all the languages and the count number e.g. 'languages':{'en':2,'cn':1, ...}
    multicul = {'A1': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'A2': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'A3': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'A4': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'B1': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'B2': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'B3': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'B4': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'C1': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'C2': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'C3': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'C4': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'D1': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'D2': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'D3': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                'D4': {'TotalTweets': 0, 'NumberofLanguagesUsed': 0, 'Top10Languages-Tweets': [], 'languages': {}},
                }

    # parallel processing twitter file
    # find total number of lines to be processed
    total_lines = twitter_lines(twitter_file)
    # calculate number of lines to be processed by each core
    lines_per_core = total_lines / comm_size
    start_time = time.time()
    start_line = lines_per_core * comm_rank + 1
    # last core processes the rest all lines
    end_line = start_line + lines_per_core
    if comm_rank == comm_size - 1:
        end_line = total_lines + 1

    with open(twitter_file, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f):
            if line_number >= start_line and line_number < end_line:
                if line.endswith(',\n'):
                    row = line[:-2]
                elif line.endswith(']}\n'):
                    row = line[:-3]
                multicul = twitter_analyze(json.loads(row), grid_info, multicul)

    # only one core used
    if comm_size == 1:
        for cell in list(multicul.keys()):
            multicul[cell]['Top10Languages-Tweets'] = dict(Counter(multicul[cell]['languages']).most_common(10))
    # multiple cores used
    else:
        multicul_list = comm.gather(multicul, root=0)
        # gather results in master core
        if comm_rank == 0:
            for i in range(1, comm_size):
                for cell in list(multicul.keys()):
                    multicul[cell]['TotalTweets'] += multicul_list[i][cell]['TotalTweets']
                    multicul[cell]['languages'] = dict(
                        Counter(multicul_list[i][cell]['languages']) + Counter(multicul[cell]['languages']))

            for cell in list(multicul.keys()):
                multicul[cell]['NumberofLanguagesUsed'] = len(multicul[cell]['languages'])
                multicul[cell]['Top10Languages-Tweets'] = dict(Counter(multicul[cell]['languages']).most_common(10))

    process_time = time.time() - start_time

    # master core print info
    if comm_rank == 0:
        print("Process time: {} s".format(process_time))
        print(multicul)


if __name__ == "__main__":
    grid_file = "./sydGrid.json"
    Grid_info = extracGrid(grid_file)  # a dict contains grid id and its coordinates e.g. {23: {'tl': [151.2155, -33.85412], 'bl': [151.2155, -34.00412], 'br': [151.3655, -34.00412], 'tr': [151.3655, -33.85412]}, ...}
    Twitter_file = "./bigTwitter.json"

    main(Twitter_file, Grid_info)
