import pandas as pd
import matplotlib.pyplot as plt

# train_time.csv 읽기
df_time = pd.read_csv('/Users/an-yohan/Documents/GitHub/SW/sw_contest/code/train/new_data/train_time.csv')

# 'label' 열이 'real'과 'fake'인 경우로 필터링하여 평균 시간 계산
mean_times = df_time.groupby('label')['time'].mean()

# 그래프 그리기
plt.figure(figsize=(8, 5))
bars = plt.bar(mean_times.index, mean_times.values, color=['skyblue', 'salmon'])
plt.title('Average Duration of Real and Fake Audio Files')
plt.xlabel('Label')
plt.ylabel('Average Time (seconds)')
plt.xticks(rotation=0)
plt.grid(axis='y')

# 평균 시간을 바 위에 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.3f}', ha='center', va='bottom')

# 그래프 저장
plt.savefig('average_duration.png')

# 그래프 표시
plt.show()
