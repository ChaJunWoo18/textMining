#pip install pytagcloud pygame simplejson
#pygame : counter쓰려고

from collections import Counter
from wordcloud import WordCloud

nouns = list()
nouns.extend(['AutoCoder' for i in range(10)])
nouns.extend(['Automation' for i in range(8)])
nouns.extend(['Python' for i in range(6)])
#print(nouns)
count = Counter(nouns)
tag = count.most_common() #최빈값

wc = WordCloud(font_path='malgun' , width=400, height=400, scale = 2.0, max_font_size=250)
freq= Counter(nouns) 
print(freq)
generate = wc.generate_from_frequencies(freq)
wc.to_file('C:\\AutoCoder\\wordCloudTest.png')
