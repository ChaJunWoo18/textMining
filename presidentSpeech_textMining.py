ysy = open('president_speech.txt.txt', encoding='UTF-8').read()
#print(ysy)

import re
ysy = re.sub('[^가-힣]', ' ', ysy)

import konlpy
import os 

os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17\bin'

hannanum = konlpy.tag.Hannanum()
text = "안녕하세요, 자동화 및 업무자동화 시스템자동화 강의를 진행하고 있는 강사 오토코더 입니다. 앞으로 잘부탁드립니다."
nouns = hannanum.nouns(ysy)
#print(nouns)
import pandas as pd
df_speech = pd.DataFrame({'speech':nouns})
df_speech['count'] = df_speech['speech'].str.len()
#print(df_speech)

df_speech = df_speech.query('count >=2')
df_speech.sort_values('count')

df_speech = df_speech.groupby('speech', as_index=False).agg(n=('speech', 'count')).sort_values('n', ascending=False)
#print(df_speech)

top20 = df_speech.head(20)
#print(top20)

import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family' : 'Malgun Gothic',
                     'figure.dpi' : 150,
                     'figure.figsize' : [7,6]})
sns.barplot(data=top20, x = 'n', y = 'speech')
plt.show()