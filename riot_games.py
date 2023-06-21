from riotwatcher import LolWatcher, ApiError
import pandas as pd
import pprint

# golbal variables
api_key = 'RGAPI-59b2d4e1-13f9-4957-a36d-ad5091e97b37'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'Sensei Buttcheek')

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
pprint.pprint(my_ranked_stats)