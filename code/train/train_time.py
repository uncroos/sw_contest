import pandas as pd
import librosa
import os
import time  # 시간 측정용 모듈

# 시작 시간 기록
start_time = time.time()

# train_sorted.csv 읽기
df_sorted = pd.read_csv('/Users/an-yohan/Documents/GitHub/SW/sw_contest/code/train/new_data/train_sorted.csv')

# 결과를 저장할 리스트
results = []

# train 폴더 안의 ogg 파일을 순회
for index, row in df_sorted.iterrows():
    audio_id = row['id']
    audio_path = os.path.join('/Users/an-yohan/Documents/GitHub/SW/data/train', f'{audio_id}.ogg')
    label = row['label']  # label 가져오기

    # ogg 파일 읽기 및 시간 측정
    try:
        y, sr = librosa.load(audio_path, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)

        # 결과 저장
        results.append({
            'id': audio_id,
            'path': audio_path,
            'time': round(duration, 3),  # 소수점 3자리까지 반올림
            'label': label  # label 추가
        })
    except Exception as e:
        print(f"Error processing {audio_path}: {e}")

# 결과 DataFrame 생성
df_results = pd.DataFrame(results)

# train_time.csv로 저장
df_results.to_csv('train_time.csv', index=False)

# 종료 시간 기록
end_time = time.time()

# 실행 시간 계산
execution_time = end_time - start_time
print(f"train_time.csv 파일이 생성되었습니다. 실행 시간: {execution_time:.2f}초")
