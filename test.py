import configParsing as conf

st = conf.getAppList()
i = 0
while i < len(st):
    print(st[i][0])
    i = i+1