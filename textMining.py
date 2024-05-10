from konlpy.tag import Okt
import os 

os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17\bin'

okt = Okt()

text = "안녕하세요, '오토코더' 입니다. 자동화 강의 및 강좌를 촬영하고 공유하고 있습니다."

print(okt.nouns(text))
okt_list = []

for noun in okt.nouns(text):
    if len(noun) >= 2:
        print(noun)