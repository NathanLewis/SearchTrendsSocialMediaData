#!/usr/bin/env python3
import json
import csv

contents = {}
with open('musk_28_03_2025.json') as file:
    contents = json.loads(file.read())

wanted = ['tweet_id', 'created_at', 'text', 'lang', 'conversation_id', 'bookmarks', 'views', 'favorites', 'quotes', 'replies', 'retweets']
ekeys = ['urls', 'hashtags', 'symbols', 'timestamps']
qkeys = ['text', 'tweet_id', 'author', 'media']
#eheader = wanted + ['entities.' + ky for ky in ekeys] + ['quoted.' + q for q in qkeys]
eheader = wanted + ['image'] + ['quoted.' + q for q in qkeys] + ['entities.' + ky for ky in ekeys]
with open('output.tsv', 'w', newline="\r\n") as tsvfile:
    writer = csv.DictWriter(tsvfile, fieldnames=eheader, delimiter='\t')
    writer.writeheader()
    for res in contents['timeline']:
        #intersection = [ x for x in res.keys() if x in wanted]
        if isinstance(res['media'], list):
            if len(res['media']) > 0:
                print('Unexpected media')
                print(json.dumps(res['media']))

        row = [ res[key] for key in wanted]
        if isinstance(res['media'], dict): 
            if 'quoted' in res:
                print('row has both media and quoted')
                print(json.dumps(res))
            if 'photo' in res['media']:
                print(res['media']['photo'][0]['media_url_https'])
            if 'video' in res['media']:
                print(res['media']['video'][0]['media_url_https'])
                image = res['media']['video'][0]['media_url_https']        
                row.append(image)
        else:
            row.append('')
        entities = res['entities']
        #print(res.keys())
        if 'quoted' in res:
            quoted = res['quoted']
            qrow = [ quoted[key] for key in qkeys ]
        else:
            qrow = [ '' for key in qkeys ]
        erow = [ entities[key] for key in ekeys ]
        #writer.writerow(dict(zip(eheader, row + erow + qrow)))
        writer.writerow(dict(zip(eheader, row + qrow + erow)))
