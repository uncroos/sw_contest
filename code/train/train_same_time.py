from pydub import AudioSegment
import os

# 작업할 폴더 경로 설정 (train 폴더)
train_folder = '/Users/an-yohan/Documents/GitHub/SW/data/train'  # train 폴더 경로를 설정합니다.
output_folder = '/Users/an-yohan/Documents/GitHub/SW/sw_contest/code/train/new_train_ogg'  # 5초로 정규화된 오디오를 저장할 폴더 경로입니다.

# 오디오 길이 (5초) 설정 - 5000밀리초는 5초를 나타냄
target_duration = 5000  # 밀리초 단위로 5초 길이를 설정

# 출력 폴더가 없다면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 모든 ogg 파일에 대해 반복 처리
for filename in os.listdir(train_folder):
    if filename.endswith('.ogg'):
        # 오디오 파일 불러오기
        filepath = os.path.join(train_folder, filename)
        audio = AudioSegment.from_file(filepath, format="ogg")
        
        # 오디오 길이가 5초보다 긴 경우 자르기
        if len(audio) > target_duration:
            # 오디오의 앞쪽 5초 부분만 잘라내기
            audio = audio[:target_duration]
        
        # 오디오 길이가 5초보다 짧은 경우 패딩
        elif len(audio) < target_duration:
            # 오디오 끝에 0으로 채우기 - Zero Padding
            padding = AudioSegment.silent(duration=target_duration - len(audio))
            audio = audio + padding  # 기존 오디오에 패딩 추가
            
        # 정규화된 오디오를 출력 폴더에 저장
        output_path = os.path.join(output_folder, filename)
        audio.export(output_path, format="ogg")
        print(f"{filename} 파일이 5초로 정규화되었습니다.")
