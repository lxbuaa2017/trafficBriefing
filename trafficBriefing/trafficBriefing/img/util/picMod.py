from PIL import Image
import datetime
import os

p=os.path.dirname(__file__)
p = p[:-5]
source = Image.open('{}/util/font.png'.format(p))
aim = Image.open('{}/0'.format(p))
aim.paste(source, (300, 50))
now = datetime.datetime.now()
date = str(now.year) + '年' + str(now.month) + '月' + str(now.day) + '日' + "全国交通气象预报"

aim.save(('{}/'+date + '.png').format(p))
os.remove('{}/0'.format(p))