from dateutil.parser import parse
import feedparser

from helpers import get_new_entries, send_entries, convert_rss_date_to_datetime

from conf import redis

for key in redis.keys():
    rss_url, chat_id = key.decode().split('|')
    rss_updated = parse(redis.get(key).decode())
    rss = feedparser.parse(rss_url)
    rss_modified = convert_rss_date_to_datetime(rss.feed.modified)
    if rss_modified <= rss_updated:
        continue
    new_entries = get_new_entries(rss, rss_updated)
    send_entries(new_entries, chat_id)
    redis.set(key, rss_modified)
