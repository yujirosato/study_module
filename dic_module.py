#読み込んだ極性値のCSVファイルを辞書型に格納
import csv
import MeCab

#辞書＝{名詞名：極性値}の辞書をCSVから読み取る関数
#東工大の高村教授が公開されている「単語感情極性対応表」
def make_dic():

    dic = {}

    with open('pn_ja_dic.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダーを読み飛ばしたい時

        for row in reader:
            #要素三つ目に極性値 要素0個目に名詞名
            dic[row[0]] = row[3]

    return dic

def i(line_2, sub_dic):

    point = 0

    # 形態素解析器の変数（オブジェクト）を作成 neologd
    t = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    #レビューの形態素解析
    line_2 = t.parse(line_2)
    #形態素解析データを分割してリストに
    ward = [ward.replace('\t',',').split(',') for ward in line_2.split('\n')[:-2]]


    for x in ward:
        if x[7] in sub_dic:
            #印象の合計の計算
            point = point + float(sub_dic[x[7]])

    return point


if __name__ == "__main__":

    #辞書を作成
    main_dic = make_dic()

    line = input("文章を入力:")
    #印象計算
    point = i(line, main_dic)

    print(line + " : " + str(point))

    #print(str(main_dic["いい"]))
