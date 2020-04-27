首先要有python3的环境
然后pip（或者conda） install scrapy
然后进入到trafficBriefing/trafficBriefing目录，
命令行执行 scrapy crawl briefing -o brief.json -s FEED_EXPORT_ENCODING=UTF-8 
将在weatherBriefingSpider文件夹下生成brief.json
然后直接运行briefGenerator文件夹里的trainsition.py 
将会在该文件夹下生成brief.docx 文档

