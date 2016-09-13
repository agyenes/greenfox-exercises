def make_dict(map_x):
    map_dict = []
    for i in range(len(map_x)):
        for j in range(len(map_x[i])):
            row = {}
            row['x'] = j
            row['y'] = i
            if map_x[i][j] == 0:
                row['type'] = 'floor'
            if map_x[i][j] == 1:
                row['type'] = 'wall'
            if map_x[i][j] == 2:
                row['type'] = 'hero'
            map_dict.append(row)
    return map_dict
