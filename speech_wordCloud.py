ysy = open('president_speech.txt.txt', encoding='UTF-8').read()
import re
import os 
import konlpy
import pandas as pd
from wordCloud import WordCloud

ysy = re.sub('[^가-힣]',' ', ysy)
#print(ysy)

os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17\bin'
hannanum = konlpy.tag.Hannanum()
nouns = hannanum.nouns(ysy)

df_word = pd.DataFrame({'word' : nouns})

df_word['count'] = df_word['word'].str.len()

df_word = df_word.query('count >= 2')
#print(df_word.sort_values('count'))

df_word = df_word.groupby('word', as_index=False).agg(n=('word', 'count')).sort_values('n', ascending=False)
print(df_word)

top10 = df_word.head(10)
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family' : 'Malgun Gothic',
                     'figure.dpi': 120,
                     'figure.figsize' : [6.5, 6]})
sns.barplot(data=top10, x='n', y = 'word')
#plt.show()

#dic형태로 변경
dic_word = df_word.set_index('word').to_dict()['n']
print(dic_word)

wc = WordCloud(random_state = 1234,
               width = 400,
               height=400,
               font_path = r'C:\\Windows\Fonts\Malgunsl.ttf',
               background_color='white')
img_wordCloud = wc.generate_from_frequencies(dic_word)
plt.figure(figsize=(10,10))
plt.axis('off')
plt.imshow(img_wordCloud)
plt.show()