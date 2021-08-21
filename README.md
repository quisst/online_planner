# online_planner
태블릿 없는 분들을 위한 파이썬으로 만든 플래너입니다!

## 필요 라이브러리
- cv2
- pillow
- os

## 파일 소개
- main.py : 제일 초기 버전이며 시간 표시 기능은 없습니다.
- main_v2.py : main.py에서 시간 표시 기능이 추가되었습니다.
- main_v2(missed).py : main_v2에서 날짜를 조작할 수 있는 기능이 있는 파일입니다.
- minu-minu planner A5-1.jpg : 플래너 파일로, 이 파일 위에 글자와 도형을 그릴겁니다.

## 작동 순서
- task 개수 받기 (n개)
- 1번째 task의 이름, 내용(, 시간) 받기
- 2번째 task의 이름, 내용(, 시간) 받기
- ...
- n번째 task의 이름, 내용(, 시간) 받기
- task의 이름, 내용이 저장되어 있는 aaa.jpg 저장
- aaa.jpg에 시간을 표시한 bbb.jpg 저장
