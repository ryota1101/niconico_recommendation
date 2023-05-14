#各動画ページの自動生成
import pandas as pd
import os

def write_page( file1, str1 ): 
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0 


df = pd.read_csv('../csv_file/reccomend_df.csv', index_col=0)

for num in range(len(df)):
    movie_title = df["title"].iloc[num]
    orgmovieid = df["ID"].iloc[num]
    ID = df["ID"].iloc[num]
    words = df["content"].iloc[num]
    word = words.split(",")
    fwordorg = ", ".join(word)
    id1 = df["sim_rec1"][df["ID"]==ID].iloc[0]
    words = df["content"][df["ID"]==id1].iloc[0]
    word = words.split(",")
    word1 = ", ".join(word)
    id2 = df["sim_rec2"][df["ID"]==ID].iloc[0]
    words = df["content"][df["ID"]==id2].iloc[0]
    word = words.split(",")
    word2 = ", ".join(word)
    id3 = df["sim_rec3"][df["ID"]==ID].iloc[0]
    words = df["content"][df["ID"]==id3].iloc[0]
    word = words.split(",")
    word3 = ", ".join(word)
    id4 = df["emo_rec1"][df["ID"]==ID].iloc[0]
    words = df["content"][df["ID"]==id4].iloc[0]
    word = words.split(",")
    word4 = ", ".join(word)
    id5 = df["emo_rec2"][df["ID"]==ID].iloc[0]
    words = df["content"][df["ID"]==id5].iloc[0]
    word = words.split(",")
    word5 = ", ".join(word)
    id6 = df["emo_rec3"][df["ID"]==ID].iloc[0]
    words = df["content"][df["ID"]==id6].iloc[0]
    word = words.split(",")
    word6 = ", ".join(word)
    id7 = df["comb_rec1"][df["ID"]==ID].iloc[0]
    words = df["content"][df["ID"]==id7].iloc[0]
    word = words.split(",")
    word7 = ", ".join(word)
    id8 = df["comb_rec2"][df["ID"]==ID].iloc[0]
    words = df["content"][df["ID"]==id8].iloc[0]
    word = words.split(",")
    word8 = ", ".join(word)
    id9 = df["comb_rec3"][df["ID"]==ID].iloc[0]
    words = df["content"][df["ID"]==id9].iloc[0]
    word = words.split(",")
    word9 = ", ".join(word)
    #df["check"].iloc[num] = 1
    #df.to_csv('reccomend_df.csv')
    #print(df["tags"].iloc[num])

    html_sorce = """
    <!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="moviepage.css"></title>
    <!-- 0 -->
    <title>{orgmovieid}</title>
  </head>

  <body>
    <!-- 1 -->
    <h1>{movie_title}</h1>
    <p>
      <a href="../index.html">最初に戻る</a>
    </p>

    <h2>推薦元動画</h2>
    <!-- 2 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{orgmovieid}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{orgmovieid}">推薦元動画リンク</a></noscript>
    <h3>特徴語</h3>
    <!-- 3 -->
    <h4>{fwordorg}</h4>
    <h3>印象</h3>
    <p>左から順に[楽しい，面白い][かわいい，感動，好き][かっこいい,驚き][怖い，怒り，悲しい]</p>
    <!-- 4 -->
    <div class="container">
      <div class="item item0_{orgmovieid}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{orgmovieid}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{orgmovieid}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{orgmovieid}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h2>特徴語による推薦動画1</h2>
    <!-- 5 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id1}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{id1}">特徴語推薦1動画リンク</a></noscript>
    <h3>特徴語</h3>
    <!-- 5.5 -->
    <h4>{word1}</h4>
    <!-- 6 -->
    <h3>印象</h3>
    <div class="container">
      <div class="item item0_{id1}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{id1}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{id1}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{id1}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h3>アンケート</h3>
    <form id="target">
      <div>
        <label>
    	     <input name="hoge" type="radio" value="0" checked> 推薦された動画は適切である/嗜好にあっている
         </label>
      </div>
      <div>
        <label>
    	     <input name="hoge" type="radio" value="1"> 推薦された動画は適切でない/嗜好にあっていない
         </label>
      </div>
    </form>
    <h2>特徴語推薦2</h2>
    <!-- 7 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id2}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{id2}">特徴語推薦2動画リンク</a></noscript>
    <h3>特徴語</h3>
    <!-- 8 -->
    <h4>{word2}</h4>
    <h3>印象</h3>
    <!-- 9 -->
    <div class="container">
      <div class="item item0_{id2}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{id2}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{id2}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{id2}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h3>アンケート</h3>
    <form id="target2">
      <div>
        <label>
    	     <input name="hoge" type="radio" value="0" checked> 推薦された動画は適切である/嗜好にあっている
         </label>
      </div>
      <div>
        <label>
    	     <input name="hoge" type="radio" value="1"> 推薦された動画は適切でない/嗜好にあっていない
         </label>
      </div>
    </form>
    <h2>特徴語推薦3</h2>
    <!-- 10 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id3}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{id3}">特徴語推薦3動画リンク</a></noscript>
    <h3>特徴語</h3>
    <!-- 11 -->
    <h4>{word3}</h4>
    <h3>印象</h3>
    <!-- 12 -->
    <div class="container">
      <div class="item item0_{id3}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{id3}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{id3}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{id3}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h3>アンケート</h3>
    <form id="target3">
      <div>
        <label>
    	     <input name="hoge" type="radio" value="0" checked> 推薦された動画は適切である/嗜好にあっている
         </label>
      </div>
      <div>
        <label>
    	     <input name="hoge" type="radio" value="1"> 推薦された動画は適切でない/嗜好にあっていない
         </label>
      </div>
    </form>
    <h2>印象による推薦動画1</h2>
    <!-- 13 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id4}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{id4}">印象推薦1動画リンク</a></noscript>
    <h3>特徴語</h3>
    <!-- 14 -->
    <h4>{word4}</h4>
    <h3>印象</h3>
    <!-- 15 -->
    <div class="container">
      <div class="item item0_{id4}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{id4}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{id4}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{id4}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h3>アンケート</h3>
    <form id="target4">
      <div>
        <label>
    	     <input name="hoge" type="radio" value="0" checked> 推薦された動画は適切である/嗜好にあっている
         </label>
      </div>
      <div>
        <label>
    	     <input name="hoge" type="radio" value="1"> 推薦された動画は適切でない/嗜好にあっていない
         </label>
      </div>
    </form>
    <h2>印象推薦2</h2>
    <!-- 16 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id5}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{id5}">印象推薦2動画リンク</a></noscript>
    <h3>特徴語</h3>
    <!-- 17 -->
    <h4>{word5}</h4>
    <h3>印象</h3>
    <!-- 18 -->
    <div class="container">
      <div class="item item0_{id5}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{id5}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{id5}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{id5}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h3>アンケート</h3>
    <form id="target5">
      <div>
        <label>
    	     <input name="hoge" type="radio" value="0" checked> 推薦された動画は適切である/嗜好にあっている
         </label>
      </div>
      <div>
        <label>
    	     <input name="hoge" type="radio" value="1"> 推薦された動画は適切でない/嗜好にあっていない
         </label>
      </div>
    </form>
    <h2>印象推薦3</h2>
    <!-- 19 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id6}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{id6}">印象推薦3動画リンク</a></noscript>
    <h3>特徴語</h3>
    <!-- 20 -->
    <h4>{word6}</h4>
    <h3>印象</h3>
    <!-- 20.5 -->
    <div class="container">
      <div class="item item0_{id6}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{id6}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{id6}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{id6}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h3>アンケート</h3>
    <form id="target6">
      <div>
        <label>
    	     <input name="hoge" type="radio" value="0" checked> 推薦された動画は適切である/嗜好にあっている
         </label>
      </div>
      <div>
        <label>
    	     <input name="hoge" type="radio" value="1"> 推薦された動画は適切でない/嗜好にあっていない
         </label>
      </div>
    </form>
    <h2>特徴語と印象の両方による推薦動画1</h2>
    <!-- 21 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id7}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{id7}">組み合わせ推薦1動画リンク</a></noscript>
    <h3>特徴語</h3>
    <!-- 22 -->
    <h4>{word7}</h4>
    <h3>印象</h3>
    <!-- 23 -->
    <div class="container">
      <div class="item item0_{id7}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{id7}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{id7}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{id7}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h3>アンケート</h3>
    <form id="target7">
      <div>
        <label>
    	     <input name="hoge" type="radio" value="0" checked> 推薦された動画は適切である/嗜好にあっている
         </label>
      </div>
      <div>
        <label>
    	     <input name="hoge" type="radio" value="1"> 推薦された動画は適切でない/嗜好にあっていない
         </label>
      </div>
    </form>
    <h2>組み合わせ推薦2</h2>
    <!-- 24 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id8}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{id8}">組み合わせ推薦2動画リンク</a></noscript>
    <h3>特徴語</h3>
    <!-- 25 -->
    <h4>{word8}</h4>
    <h3>印象</h3>
    <!-- 26 -->
    <div class="container">
      <div class="item item0_{id8}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{id8}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{id8}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{id8}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h3>アンケート</h3>
    <form id="target8">
      <div>
        <label>
    	     <input name="hoge" type="radio" value="0" checked> 推薦された動画は適切である/嗜好にあっている
         </label>
      </div>
      <div>
        <label>
    	     <input name="hoge" type="radio" value="1"> 推薦された動画は適切でない/嗜好にあっていない
         </label>
      </div>
    </form>
    <h2>組み合わせ推薦3</h2>
    <!-- 27 -->
    <script type="application/javascript" src="https://embed.nicovideo.jp/watch/{id9}/script?w=640&h=360"></script>
    <noscript><a href="https://www.nicovideo.jp/watch/{id9}">組み合わせ推薦3動画リンク</a></noscript>

    <h3>特徴語</h3>
    <!-- 28 -->
    <h4>{word9}</h4>
    <h3>印象</h3>
    <!-- 29 -->
    <div class="container">
      <div class="item item0_{id9}">
        <span class="item_label">面白い，楽しい</span>
      </div>
      <div class="item item1_{id9}">
        <span class="item_label">かわいい，感動</span>
      </div>
      <div class="item item2_{id9}">
        <span class="item_label">かっこいい，驚き</span>
      </div>
      <div class="item item3_{id9}">
        <span class="item_label">怖い，怒り</span>
      </div>
    </div>
    <h3>アンケート</h3>
    <form id="target9">
      <div>
        <label>
    	     <input name="hoge" type="radio" value="0" checked> 推薦された動画は適切である/嗜好にあっている
         </label>
      </div>
      <div>
        <label>
    	     <input name="hoge" type="radio" value="1"> 推薦された動画は適切でない/嗜好にあっていない
         </label>
      </div>
    </form>
    <p>　</p>
    <button id="download" type="button">アンケート回答結果をダウンロード</button>
    <p>　</p>
    <p>アンケート協力ありがとうございました</p>
    <p>
      <a href="../index.html">索引に戻る</a>
    </p>
    <script>
      function downloadCSV() {{

        let q = "";
        const ques = document.getElementById("target");
          for (let i = 0; i < ques.length; i++) {{
            if (ques[i].checked) {{
              q = ques[i].value;
              break;
            }}
          }}

        let q2 = "";
        const ques2 = document.getElementById("target2");
          for (let i = 0; i < ques2.length; i++) {{
            if (ques2[i].checked) {{
              q2 = ques2[i].value;
              break;
            }}
          }}

        let q3 = "";
        const ques3 = document.getElementById("target3");
          for (let i = 0; i < ques3.length; i++) {{
            if (ques3[i].checked) {{
              q3 = ques3[i].value;
              break;
            }}
          }}

        let q4 = "";
        const ques4 = document.getElementById("target4");
          for (let i = 0; i < ques4.length; i++) {{
            if (ques4[i].checked) {{
              q4 = ques4[i].value;
              break;
            }}
          }}

        let q5 = "";
        const ques5 = document.getElementById("target5");
          for (let i = 0; i < ques5.length; i++) {{
            if (ques5[i].checked) {{
              q5 = ques5[i].value;
              break;
            }}
          }}

        let q6 = "";
        const ques6 = document.getElementById("target6");
          for (let i = 0; i < ques6.length; i++) {{
            if (ques6[i].checked) {{
              q6 = ques6[i].value;
              break;
            }}
          }}

        let q7 = "";
        const ques7 = document.getElementById("target7");
          for (let i = 0; i < ques7.length; i++) {{
            if (ques7[i].checked) {{
              q7 = ques7[i].value;
              break;
            }}
          }}

        let q8 = "";
        const ques8 = document.getElementById("target8");
          for (let i = 0; i < ques8.length; i++) {{
            if (ques8[i].checked) {{
              q8 = ques8[i].value;
              break;
            }}
          }}

        let q9 = "";
        const ques9 = document.getElementById("target9");
          for (let i = 0; i < ques9.length; i++) {{
            if (ques9[i].checked) {{
              q9 = ques9[i].value;
              break;
            }}
          }}

          /* #######################  filename と　ID　を変更 ############################# */
          const filename = "{orgmovieid}.csv";
          const head = ",ID,特徴1,特徴2,特徴3,印象1,印象2,印象3,両方1,両方2,両方3\\n";
          const input = "0,{orgmovieid}," + q +","+ q2+","+ q3+","+ q4+","+ q5+","+ q6+","+ q7+","+ q8+","+ q9;
          //CSVデータ
          const data = head + input;
          //BOMを付与する（Excelでの文字化け対策）
          const bom = new Uint8Array([0xef, 0xbb, 0xbf]);
          //Blobでデータを作成する
          const blob = new Blob([bom, data], {{ type: "text/csv" }});

          //IE10/11用(download属性が機能しないためmsSaveBlobを使用）
          if (window.navigator.msSaveBlob) {{
              window.navigator.msSaveBlob(blob, filename);

          //その他ブラウザ
          }} else {{
              //BlobからオブジェクトURLを作成する
              const url = (window.URL || window.webkitURL).createObjectURL(blob);
              //ダウンロード用にリンクを作成する
              const download = document.createElement("a");
              //リンク先に上記で生成したURLを指定する
              download.href = url;
              //download属性にファイル名を指定する
              download.download = filename;
              //作成したリンクをクリックしてダウンロードを実行する
              download.click();
              //createObjectURLで作成したオブジェクトURLを開放する
              (window.URL || window.webkitURL).revokeObjectURL(url);
          }}
      }}


      //ボタンを取得する
      const download = document.getElementById("download");
      //ボタンがクリックされたら「downloadCSV」を実行する
      download.addEventListener("click", downloadCSV, false);
    </script>
  </body>
</html>
    """.format( movie_title=movie_title, orgmovieid=orgmovieid, fwordorg=fwordorg,
           id1=id1,  word1=word1, id2=id2, word2=word2, id3=id3, word3=word3,
           id4=id4, word4=word4, id5=id5, word5=word5, id6=id6, word6=word6,
           id7=id7, word7=word7, id8=id8, word8=word8, id9=id9, word9=word9)


    filename = "../HTML/movie/"+ID+".html" 
    write_page(filename, html_sorce)