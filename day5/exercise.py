def merge_dicts(x, y):
    merged = {}
    for key in (*x.keys(), *y.keys()):
        if (val := y.get(key, x.get(key))) is y.get(key, None) and key in x:
            merged[key] = (x[key], val)
        else:
            merged[key] = val
    return merged

group1= {'tasneem':1, 'layan': 2}
group2 = {'layan': 3, 'leen': 4}
print(merge_dicts(group1, group2))
