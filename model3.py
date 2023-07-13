# from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from joblib import dump, load


def judge_percent(input_text):
    # csvファイルからリストを生成する。
    df = pd.read_csv('text.csv',header=0)
    txt_lst = df['text'].values.tolist()
    label_lst = df['label'].values.tolist()
    # textの出現回数をベクトル化
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(txt_lst)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    clf = MultinomialNB().fit(X_train_tfidf, label_lst)
    # データの前処理
    input_text=[input_text]
    new_data_counts = count_vect.transform(input_text)
    new_data_tfidf = tfidf_transformer.transform(new_data_counts)

    predicted = clf.predict_proba(new_data_tfidf)
    # モデルを保存
    dump(clf, 'naive_bayes_model.joblib')
    # モデルをロード
    loaded_model = load('naive_bayes_model.joblib')
    result = loaded_model.predict_proba(new_data_tfidf)
    # if result[0][0]>=result[0][1]:
    #     result= (result[0][0])*100
    # else :
    #     result= (result[0][1])*100
    return result   