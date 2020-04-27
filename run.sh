#爬虫
CURRENT_DIR=$(cd $(dirname $0); pwd)
cd trafficBriefing/trafficBriefing
scrapy crawl briefing -o brief.json -s FEED_EXPORT_ENCODING=UTF-8

#如果同时装有python2和python3那么这里需要改为python3
python $CURRENT_DIR/trafficBriefing/trafficBriefing/img/util/picMod.py

