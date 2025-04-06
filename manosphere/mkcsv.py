#!/usr/bin/env python3
import json
import csv
#import argparse
import sys

contents = {}
fname = 'musk_28_03_2025.json'
if len(sys.argv) > 1:
    fname = sys.argv[1]

with open(fname) as file:
    contents = json.loads(file.read())

wanted = ['tweet_id', 'created_at', 'text', 'lang', 'conversation_id', 'bookmarks', 'views', 'favorites', 'quotes', 'replies', 'retweets']
ekeys0 = ['urls', 'user_mentions', 'hashtags', 'symbols', 'timestamps']
qkeys0 = ['text', 'tweet_id', 'author', 'image', 'video', 'media']
qkeys = ['quoted.' + q for q in qkeys0]
sheetheader = wanted + ['image', 'video'] + qkeys + ['entities.' + ky for ky in ekeys0]
print(sheetheader)
#with open(fname.replace('.json','.tsv'), 'w', newline="\r\n") as tsvfile:
with open(fname.replace('.json','.tsv'), 'w') as tsvfile:
    writer = csv.DictWriter(tsvfile, fieldnames=sheetheader, delimiter='\t')
    writer.writeheader()
    for res in contents['timeline']:
        sheetDict = {}
        for key in sheetheader:
            sheetDict[key] = ''
        if isinstance(res['media'], list):
            if len(res['media']) > 0:
                print('Unexpected media')
                print(json.dumps(res['media']))

        for key in sheetheader:
            if key in res:
                sheetDict[key] = res[key]
        if isinstance(res['media'], dict): 
            if 'quoted' in res:
                print(f'row has both media and quoted {json.dumps(res)}')
                #print(json.dumps(res))
            if 'photo' in res['media']:
                print(res['media']['photo'][0]['media_url_https'])
                #row.append(image)
                sheetDict['image'] = image
            if 'video' in res['media']:
                print(res['media']['video'][0]['media_url_https'])  # brittle code
                image = res['media']['video'][0]['media_url_https']        
                #row.append(image) # potentially clobbering the previous photo
                sheetDict['image'] = image
                if len(res['media']['video']) > 1:
                    video1 = res['media']['video'][1]
                    sheetDict['video'] = video1
                    print(f'Adding Video {video1}')

        entities = res['entities']
        #print(res.keys())
        if 'quoted' in res:
            quoted = res['quoted']
            quoted['image'] = ''
            quoted['video'] = ''
            if 'media' in quoted:
                #print(quoted['media'])
                if 'video' in quoted['media']:
                    quoted['image'] = quoted['media']['video'][0]['media_url_https']
                    quoted['video'] = quoted['media']['video'][0]['variants'][1]['url']
                if 'photo' in quoted['media']:
                    #print(res['media']['photo'][0]['media_url_https'])
                    quoted['image'] = quoted['media']['photo'][0]['media_url_https']
                quoted['media'] = json.dumps(quoted['media'])

            if 'author' in quoted:
                #quoted['author'] = json.dumps(quoted['author'])
                sheetDict['quoted.author'] = json.dumps(quoted['author'])
            for key in qkeys0:
                print(f'sheetDict[quoted.{key}] = {quoted[key]}')
                sheetDict['quoted.'+key] = quoted[key]

        for key in ekeys0:
            sheetDict['entities.'+key] = entities[key]
            #if key in entities and key in sheetheader:

        writer.writerow(sheetDict)
