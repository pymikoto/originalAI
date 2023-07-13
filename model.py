# from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

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


# 新しいデータ
new_data = ["月日は百代の過客にして、行きかふ年も又旅人なり。"]

# データの前処理
new_data_counts = count_vect.transform(new_data)
new_data_tfidf = tfidf_transformer.transform(new_data_counts)

# 予測
predicted = clf.predict_proba(new_data_tfidf)

print(predicted)  # 予測されたラベルを表示

from joblib import dump, load

# モデルを保存
dump(clf, 'naive_bayes_model.joblib')

# モデルをロード
loaded_model = load('naive_bayes_model.joblib')
pred = loaded_model.predict_proba(new_data_tfidf)
print(pred)
if pred[0][0]>0.5:
    print("文系")
elif pred[0][0]==0.5:
    print("キメラ")
else :
    print("理系")