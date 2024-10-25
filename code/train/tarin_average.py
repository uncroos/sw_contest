import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# train_time.csv 읽기
df_time = pd.read_csv('/Users/an-yohan/Documents/GitHub/SW/sw_contest/code/train/new_data/train_time.csv')

# 각 label의 평균 시간 계산
mean_times = df_time.groupby('label')['time'].mean()

# Figure 1: 평균 시간 막대 그래프
plt.figure(figsize=(8, 5))
plt.bar(mean_times.index, mean_times.values, color=['skyblue', 'salmon'], alpha=0.7)
plt.title('Average Duration of Real and Fake Audio Files')
plt.xlabel('Label')
plt.ylabel('Average Time (seconds)')
plt.xticks(rotation=0)
plt.grid(axis='y')

# 막대 위에 평균 시간 텍스트 표시
for i, value in enumerate(mean_times.values):
    plt.text(i, value, f'{value:.3f}', ha='center', va='bottom')

# 그래프 저장 및 표시
plt.savefig('average_duration_bar.png')
plt.show()

# Figure 2: Real과 Fake 데이터의 오디오 길이 밀도 함수 비교
plt.figure(figsize=(10, 6))
sns.kdeplot(df_time[df_time['label'] == 'real']['time'], label='Real', color='blue', shade=True)
sns.kdeplot(df_time[df_time['label'] == 'fake']['time'], label='Fake', color='orange', shade=True)
plt.title('Length of Audio by Label')
plt.xlabel('Audio Length (seconds)')
plt.ylabel('Density')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 그래프 하단에 설명 추가
plt.figtext(0.5, -0.1, 'Figure 1. Real Data와 Fake Data의 길이 별 분포', ha='center', fontsize=10)

# 그래프 저장 및 표시
plt.savefig('audio_length_density.png', bbox_inches='tight')
plt.show()
