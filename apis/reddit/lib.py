import json
import pprint
import datetime


# Converts from reddit API format to custom format

def submission_to_dict(submission, el):

    el['author'] = submission.author.name
    el['datetime'] = datetime.datetime.fromtimestamp(submission.created_utc).strftime("%Y%m%d'T'%H%M%SZ")
    el['permalink'] = "https://reddit.com" + submission.permalink
    el['num_comments'] = submission.num_comments
    el['score'] = submission.score
    el['title'] = submission.title
    el['sub'] = submission.subreddit.display_name
    el['is_video'] = submission.is_video
    el['text'] = submission.selftext
    el['upvotes'] = submission.ups
    el['downvotes'] = submission.downs
    el['total_votes'] = el['upvotes'] + el['downvotes']
    el['thumbnail'] = submission.thumbnail
    el['crossposts'] = submission.num_crossposts
    el['flair'] = submission.link_flair_text

    if 'post_hint' in vars(submission):
        if 'video' in submission.post_hint:
            el['hint'] = 'video'
        else:
            el['hint'] = submission.post_hint
    else:
        el['hint'] = "empty"

    if el['is_video']:
        el['video_link'] = submission.media['reddit_video']['fallback_url']
        # pprint.pprint(["VIDEO", el['video_link']])

    el['url'] = submission.url


    return

