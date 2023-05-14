# niconico_recommendation
## 概要
- ニコニコ動画の動画500件のコメントデータから動画を推薦するシステムの作成
- 各動画のコメントデータから特徴語と感性を抽出し、それぞれの距離を計算することで類似動画を推薦
  - 各動画の特徴語20語を文書としてWMDで距離計算
  - byt5(文字ベースの自然言語処理モデル)で感情分類、カウントベースで動画の感性ベクトル作成、ユークリッド距離計算
  - HTML、CSS、JavaScriptのみで動画サイトの作成(アンケート機能付き)
<!--   - 特徴語
    - mecab-ipadic-neologdで名詞のみを抽出、BoW+TF-IDFで特徴語抽出
  - 感性
    - byt5(文字ベースの自然言語処理モデル)で楽しい、かわいい、格好いい、悲しいの4感情に分類 -->
## HTML
- index.html
  - 元動画リンク集
  - index2.htmlは動画のサムネ付
- movie
  - 各動画のページ([id].html)
## csv_file
公開可能なデータファイルを一部
- emotion_df.csv
  - 各動画の感性ベクトル
- movie3_df_list.csv
  - 各動画の特徴語リスト
- rank3_df_list
  - wmdによる距離計算結果上位3件のリスト
- recommend_df.csv
  - 動画id、タイトル、推薦動画9件など
## mydic
mecabのユーザー辞書
## notebook
- processing_movie_comment.inpyb
  - 対象動画のコメントを前処理
  - 各動画の特徴後を20語抽出して保存
  - 使用データ : moviedata2(非公開)
- evalution.inpyb
  - WMDおよびコサイン類似度によって推薦した動画の類似判定、類似動画割合計算
  - 類似動画判定のためのタグ調整
  - 使用データ : rank3_df.csv, meta_df3.csv(非公開), movie3_df_list.csv
  - word2vecモデル : jawaki.all_vectors.300d.txt(https://github.com/singletongue/WikiEntVec/releases)
- make_recommend_df.inpyb
  - 特徴語、印象、両方の組み合わせにより動画を推薦
  - 各動画のタイトルやタグ、特徴語と推薦動画をまとめてデータフレームを作成し保存する
  - 使用データ : rank3_df.csv, meta3_df.csv(非公開), emotion_df.csv, movie3_df_list.csv
  - word2vecモデル : jawaki.all_vectors.300d.txt(https://github.com/singletongue/WikiEntVec/releases)
- ML_emotion_nico.inpyb
  - コメント感情分類モデル作成(BoW+SVM, Word2Vec+SVMなど)
  - 使用データ : nico_20000_train.tsv, nico_20000_test.tsv, nico_20000_dev.tsv(非公開)
  - word2vecモデル : jawaki.all_vectors.300d.txt(https://github.com/singletongue/WikiEntVec/releases)
- byt5.inpyb
  - 感情分類モデル作成、転移学習用コード
  - 空ディレクトリ「byt5_model」「data」を作成し、「data」下に使用データを置く
  - 使用データ : nico_20000_train.tsv, nico_20000_test.tsv, nico_20000_dev.tsv(非公開)
- T5.inpyb
  - 感情分類モデル作成(t5)
  - 空ディレクトリ「t5_model」「data」を作成し、「data」下に使用データを置く
  - 使用データ : nico_20000_train.tsv, nico_20000_test.tsv, nico_20000_dev.tsv(非公開)
## python_code
recommend_df.csv(推薦結果)から動画表示用HTMLページの自動生成
