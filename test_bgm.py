# -*- coding:utf-8 -*-
import json

anime_rank = []
with open("anime.json", 'r', encoding='utf-8') as f:
    for anime in json.load(f):
        anime_rank.append(anime['rank'])

full_rank = ['%s' % i for i in range(1, 244)]

print(set(full_rank) - set(anime_rank))
