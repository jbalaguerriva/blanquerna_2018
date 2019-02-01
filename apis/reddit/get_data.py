import json
import pprint
# https://praw.readthedocs.io/en/latest/
# get api data creating an app here: https://www.reddit.com/prefs/apps
import praw
import datetime
# from lib import submission_to_dict, insert_batch_es
import lib

config_file = "config_oscar.json"

config_info = json.load(open(config_file, "r"))

reddit = praw.Reddit(client_id = config_info['client_id'],
                     client_secret = config_info['client_secret'],
                     user_agent = config_info['app_name'],
                     username = config_info['user_name'],
                     password = config_info['user_password'])


today_posts = {'top': [], 'controversial': []}

# Get top submissions

if config_info['search_limit'] != -1:

    listings_top = reddit.subreddit('all').top('day', limit = config_info['search_limit'])

else:
    listings_top = reddit.subreddit('all').top('day')


for listing in listings_top:
    el = {}
    lib.submission_to_dict(listing, el)
    today_posts['top'].append(el)


# Get controversial submissions

if config_info['search_limit'] != -1:

    listings_top = reddit.subreddit('all').controversial('day', limit = config_info['search_limit'])

else:
    listings_top = reddit.subreddit('all').controversial('day')


for listing in listings_top:
    el = {}
    lib.submission_to_dict(listing, el)
    today_posts['controversial'].append(el)



pprint.pprint(today_posts)


now = datetime.datetime.now()

json.dump(today_posts, open("data/data_" + now.strftime("%Y%m%d") + ".json", "w"), indent = 4)

