# check_gag.py
import requests
from bs4 import BeautifulSoup
import tweepy
import os

# X (Twitter) 認証情報
X_API_KEY = os.environ["X_API_KEY"]
X_API_SECRET = os.environ["X_API_SECRET"]
X_ACCESS_TOKEN = os.environ["X_ACCESS_TOKEN"]
X_ACCESS_SECRET = os.environ["X_ACCESS_SECRET"]

# Tweepyで認証
auth = tweepy.OAuth1UserHandler(X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET)
api = tweepy.API(auth)

# スケジュールページを取得
url = "https://omiya.yoshimoto.co.jp/schedule/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# 「GAG」が含まれてるイベントを探す
events = soup.select(".c-schedule__performance-title")
gag_events = [e.text.strip() for e in events if "GAG" in e.text]

# 仮の投稿（あとで重複防止追加）
if gag_events:
    tweet = f"大宮ラクーンでGAG出演予定あり！\n{gag_events[0]}\n\n詳細→ {url}"
    api.update_status(tweet)
