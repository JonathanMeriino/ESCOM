import pandas as pd
import sklearn

"""
INput (x) -> comentarios(review)
output (y) -> sentimientos
"""

df_review= pd.read_csv('IMDB Dataset.csv')

# print(df_review)

df_positivo = df_review[df_review['sentiment']=='positive'][:9000]
df_negativo = df_review[df_review['sentiment']=='negative'][:1000]

df_review_des= pd.concat([df_positivo,df_negativo])


print(df_review_des)
total=df_review_des.value_counts('sentiment')
print(total)