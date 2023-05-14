import pandas as pd
import re, unicodedata
import MeCab


class CleaningData:
    def __init__(self, df, target_column):
        self.df = df
        self.target_column = target_column

    def cleaning(self):
        self.df[self.target_column] = self.df[self.target_column].map(self.remove_extra_spaces)
        self.df[self.target_column] = self.df[self.target_column].map(self.normalize_neologd)

        # クリーニングの過程でtextが空になった行を削除
        self.df = self.df[self.df[self.target_column] != '']
        self.df = self.df[self.df[self.target_column] != '']
        self.df = self.df.reset_index()
        return self.df

    def unicode_normalize(self, cls, s):
        pt = re.compile('([{}]+)'.format(cls))

        def norm(c):
            return unicodedata.normalize('NFKC', c) if pt.match(c) else c

        s = ''.join(norm(x) for x in re.split(pt, s))
        s = re.sub('－', '-', s)
        return s

    def remove_extra_spaces(self, s):
        s = re.sub('[ 　]+', ' ', s)
        blocks = ''.join(('\u4E00-\u9FFF',  # CJK UNIFIED IDEOGRAPHS
                          '\u3040-\u309F',  # HIRAGANA
                          '\u30A0-\u30FF',  # KATAKANA
                          '\u3000-\u303F',  # CJK SYMBOLS AND PUNCTUATION
                          '\uFF00-\uFFEF'   # HALFWIDTH AND FULLWIDTH FORMS
                          ))
        basic_latin = '\u0000-\u007F'

        def remove_space_between(cls1, cls2, s):
            p = re.compile('([{}]) ([{}])'.format(cls1, cls2))
            while p.search(s):
                s = p.sub(r'\1\2', s)
            return s

        s = remove_space_between(blocks, blocks, s)
        s = remove_space_between(blocks, basic_latin, s)
        s = remove_space_between(basic_latin, blocks, s)
        return s

    def normalize_neologd(self, s):
        s = s.strip()
        s = self.unicode_normalize('０-９Ａ-Ｚａ-ｚ｡-ﾟ', s)

        def maketrans(f, t):
            return {ord(x): ord(y) for x, y in zip(f, t)}

        s = re.sub('[˗֊‐‑‒–⁃⁻₋−]+', '-', s)  # normalize hyphens
        s = re.sub('[﹣－ｰ—―─━ー]+', 'ー', s)  # normalize choonpus
        s = re.sub('[~∼∾〜〰～]', '', s)  # remove tildes
        s = s.translate(
            maketrans('!"#$%&\'()*+,-./:;<=>?@[¥]^_`{|}~｡､･｢｣',
                  '！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」'))

        s = self.remove_extra_spaces(s)
        s = self.unicode_normalize('！”＃＄％＆’（）＊＋，－．／：；＜＞？＠［￥］＾＿｀｛｜｝〜', s)  # keep ＝,・,「,」
        s = re.sub('[’]', '\'', s)
        s = re.sub('[”]', '"', s)
        return s

    def remove_symbols(self, text):
        text = re.sub(r'[◎, 〇, △, ▲, ×, ◇, □]', '', text)
        return text

def wakati_m_2(text):
    #tagger = MeCab.Tagger('')
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -u /mydic/foo.dic')
    tagger.parse('')
    node = tagger.parseToNode(text)
    stopword = ["これ", "ちょ","さん"]
    word_list = []
    while node:
        pos = node.feature.split(",")[0]
        stop = node.feature.split(",")[6]
        #if pos in ["動詞", "形容詞","感動詞"]:
        if (pos in ["名詞"]) & (stop not in stopword):
            word = node.surface
            word_list.append(word)
        node = node.next
    return " ".join(word_list)

def wakati_all(text):
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -u /mydic/foo.dic')
    tagger.parse('')
    node = tagger.parseToNode(text)
    stopword = ["これ", "ちょ","さん"]
    word_list = []
    while node:
        pos = node.feature.split(",")[0]
        stop = node.feature.split(",")[6]
        if pos in ["動詞", "形容詞","感動詞","名詞", "副詞", "助詞", "接続詞", "助動詞", "連体詞", "感動詞","フィラー"]:
            word = node.surface
            word_list.append(word)
        node = node.next
    return " ".join(word_list)

def wakati_pred_v2(text):
    #tagger = MeCab.Tagger('')
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -u /mydic/foo.dic')
    tagger.parse('')
    node = tagger.parseToNode(text)
    stopword = ["これ", "ちょ","さん"]
    through = ["好き", "格好","すき","嫌","かわい","かわえー","だいすきだー","大好き","イケメン","IKEMEN","大好きだー","きもい","きっも"]
    word_list = []
    meishi = 0
    other = 0
    while node:
        pos = node.feature.split(",")[0]
        stop = node.feature.split(",")[6]
        #print(pos,stop)
        if (pos in ["名詞","動詞", "形容詞","感動詞","助動詞","助詞","副詞","フィラー"]):
            word = node.surface
            word_list.append(word)
            if(pos == "名詞" and (stop not in through)):
                meishi += 1
            else:
                other += 1
        node = node.next
    #print(meishi, other)
    if meishi == 1 and other == 0:
        word_list = []
    return " ".join(word_list)

#文字列 s に、同じ文字が n+1 個以上連続している部分文字列を見つけ n に丸める
def round_chars(s, n):
    assert n > 0
    reg = re.compile("(.)\\1{%d,}" % (n))
    while True:
        m = reg.search(s)
        if not m:
            break
        else:
            s = s.replace(m.group(0), m.group(0)[:n])
    return s

def preprocessor(text):
    #デコード
    #text = decode(text)
    #削除する記号の設定
    code_regex = re.compile('["×･#$%&\'\\\\()*+,-./:;<=>@[\\]^＾_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、｀＋￥％!！ ゚ дω?]')
    #スペース,!,?意外の記号を削除
    text = code_regex.sub("", text)
    #半角を全角に
    #text = text.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
    #英語は全て小文字
    text = text.lower()
    #8以外の数字を0に変換
    del_num = re.compile("[０１２３４５６７９012345679]")
    #text = del_num.sub("０", text)
    text = del_num.sub("", text) #数字は削除
    #連続する文字をを3文字に丸める
    text = round_chars(text, 2)
    return text

def sep_comments(dataframe, over=False, step=0, col="content"):
    maxtime = dataframe["vpos"].max()
    sumtime = 0
    if step==0:
        step = maxtime / 20  #20分割
    cols = [col]
    df = pd.DataFrame(index=[], columns=cols)
    count = 0
    comment = ""

    while maxtime > sumtime:
        if over == False:
            times = list(dataframe.query('vpos > (@step * @count) & vpos < @step * (@count + 1)').index)
        elif over == True:
            times = list(dataframe.query('vpos > (@step * @count) & vpos < (@step * (@count + 1)) + (@step / 2)').index)
        for x in times:
            comment = comment + " " + dataframe.iloc[x][col]
        df.loc[count]= comment
        count += 1
        sumtime += step
        comment = ""
    return df