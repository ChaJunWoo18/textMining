#pip install pytagcloud pygame simplejson
from collections import Counter
import pytagcloud

nouns = list()
nouns.extend(['AutoCoder' for i in range(10)])
nouns.extend(['Automation' for i in range(8)])
nouns.extend(['Python' for i in range(6)])
#print(nouns)
count = Counter(nouns)
tag = count.most_common() #최빈값
taglist = pytagcloud.make_tags(tag, maxsize=50)
pytagcloud.create_tag_image(
    taglist, 'C:\\AutoCoder\\pytagCloudTest.jpg', size=(1200,900), 
    fontname='Nobile', 
    rectangular=False)