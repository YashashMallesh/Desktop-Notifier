import requests
import xml.etree.ElementTree as ET
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml" 
def loadRSS():
  '''
  utility function to load RSS feed
  '''
  resp = requests.get(RSS_FEED_URL)
  return resp.content 
def parsXML(rss):
  '''
  utility function to parse XML format rss feed
  '''
  root = ET.formstring(rss)
  newsitems = []
  for item in root("./channel/item"):
    news = {}
    for child in item:
       if child.tag == '{http://search.yahoo.com/mrss/}content':
          news['media'] = child.attrib['url']
        else:
          news[child.tag] = child.text.encode('utf8')
    newsitems.append(news)
  return newsitems
def topstories():
  '''
  main function to generate and return newsitems
  '''
  rss = loadRSS()
  newsitems = parseXML(RSS)
  return newsitems
