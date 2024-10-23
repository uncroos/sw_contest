import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# train.csv 파일 읽기
file_path = '/Users/an-yohan/Documents/GitHub/SW/data/train.csv'  # 파일 경로 수정
data = pd.read_csv(file_path)

# 시각화 스타일 설정
plt.figure(figsize=(8, 6))
sns.set(style="whitegrid")

# 'fake', 'real' 카테고리 값의 빈도수 계산
category_counts = data['label'].value_counts()

# 막대 그래프 (Seaborn 사용)
ax = sns.barplot(x=category_counts.index, y=category_counts.values, hue=category_counts.index,
                 palette="coolwarm", dodge=False, legend=False)

# 그래프에 수치 표시
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                textcoords='offset points')

# 제목과 레이블 설정
plt.title('Fake and Real', fontsize=16, weight='bold')
plt.xlabel('Category', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# 그래프 출력
plt.show()
