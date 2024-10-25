import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('/Users/an-yohan/Documents/GitHub/SW/data/train.csv')

# 'id' 열을 알파벳 순서로 정렬
df_sorted = df.sort_values(by='id').reset_index(drop=True)

# 정렬된 DataFrame을 새로운 CSV 파일로 저장
df_sorted.to_csv('train_sorted.csv', index=False)

print("ID값 정렬 완료")
