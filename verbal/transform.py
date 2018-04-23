import json

src = open('../static/data3000.json')
dst = open('../static/dic.json','w')

data = json.load(src)
dic = {}
for lk in data:
    for uk in data[lk]:
        unit = data[lk][uk]
        for word in unit:
            for key in word:
                if key not in dic:
                    dic[key] = {}
                    dic[key]['usage'] = []
                    dic[key]['synref'] = []
                    dic[key]['acrref'] = []
                dic[key]['usage']= word[key]
                for usage in word[key]:
                    for t in ['syn','acr']:
                        for syn in usage.get(t + 'onym',[]):
                            w = []
                            for c in syn:
                                if c.islower() or c == ' ':
                                    w.append(c)
                            syn = ''.join(w)
                            if not syn in dic:
                                dic[syn] = {}
                                dic[syn]['usage'] = []
                                dic[syn]['synref'] = []
                                dic[syn]['acrref'] = []

                            dic[syn][t+'ref'].append(key)



json.dump(dic,dst,indent=4,ensure_ascii=False)