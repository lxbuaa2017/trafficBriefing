首先要有python3的环境
然后pip（或者conda） install scrapy

Linux系统下直接进入项目根目录，运行run.sh脚本即可

Windows系统下具体操作为：
进入到trafficBriefing/trafficBriefing目录，
命令行执行 scrapy crawl briefing -o brief.json -s FEED_EXPORT_ENCODING=UTF-8 
将在trafficBriefing文件夹下生成brief.json
再去运行trafficBriefing/trafficBriefing/img/util/picMod.py修改图片

然后直接运行briefGenerator文件夹里的trainsition.py 
将会在该文件夹下生成brief.docx 文档

