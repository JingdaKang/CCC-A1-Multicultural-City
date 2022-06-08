import json


def findGrid(grid_info, coord):  # partially hardcode to convert grid format according to grid_info e.g. id:9 -> A1
    ROW, COL = '', ''
    if grid_info[9]['bl'][1] < coord[1] <= grid_info[9]['tl'][1]: ROW = 'A'
    if grid_info[10]['bl'][1] < coord[1] <= grid_info[10]['tl'][1]: ROW = 'B'
    if grid_info[11]['bl'][1] < coord[1] <= grid_info[11]['tl'][1]: ROW = 'C'
    if grid_info[12]['bl'][1] <= coord[1] <= grid_info[12]['tl'][1]: ROW = 'D'

    if grid_info[9]['tl'][0] <= coord[0] <= grid_info[9]['tr'][0]: COL = '1'
    if grid_info[13]['tl'][0] < coord[0] <= grid_info[13]['tr'][0]: COL = '2'
    if grid_info[17]['tl'][0] < coord[0] <= grid_info[17]['tr'][0]: COL = '3'
    if grid_info[21]['tl'][0] < coord[0] <= grid_info[21]['tr'][0]: COL = '4'

    if ROW == '' or COL == '':
        return None
    else:
        return ROW + COL


def extracGrid(grid_file):  # extraction grid coordinates from sydGrid-2 file
    Grid_info = {}
    with open(grid_file, 'r', encoding='utf-8') as f:
        synGrid = json.load(f)  # load json file: str --> dict

        for grid in synGrid['features']:
            Coor = {}
            Coor['tl'] = grid['geometry']['coordinates'][0][0]  # top left point
            Coor['bl'] = grid['geometry']['coordinates'][0][1]  # bottom left point
            Coor['br'] = grid['geometry']['coordinates'][0][2]  # bottom right point
            Coor['tr'] = grid['geometry']['coordinates'][0][3]  # top right point
            Grid_info[grid['properties']['id']] = Coor

    return Grid_info
