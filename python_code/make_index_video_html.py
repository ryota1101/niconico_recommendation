#index2.html自動作成
import pandas as pd
import os

def write_page( file1, str1 ): 
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0 


df = pd.read_csv('../csv_file/reccomend_df.csv', index_col=0)

head_sorce = """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>索引</title>
         </head>
         <body>
             <h1>ニコニコ動画推薦システム(アンケート)</h1>
             <p>視聴したいタイトルに移動してください</p>
"""

tail_sorce = """
      </body>
    </html>
"""


for num in range(len(df)):
    movie_title = df["title"].iloc[num]
    orgmovieid = df["ID"].iloc[num]
    
    
    link_sorce = """
        <p>
            <a href="movie/{id}.html">{title}</a>
        </p>
        <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id}/script?w=320&h=180"></script>
         
    """.format(title=movie_title, id=orgmovieid,)
    
    head_sorce += link_sorce

head_sorce += tail_sorce
filename = "../HTML/index-video.html" 
write_page(filename, head_sorce)