import jieba
from wordcloud import WordCloud

with open('华为笔记本.txt','r',encoding='utf-8') as file:
    s=file.read()

lst=jieba.lcut(s)

stopword=[]

txt=''.join(lst)
wordcloud=WordCloud(background_color='white',width=800,height=680,font_path='msyh.ttc').generate(txt)
wordcloud.generate(txt)
wordcloud.to_file('华为笔记本评价词云图.png')