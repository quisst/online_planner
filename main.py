import random
import datetime
from PIL import Image, ImageDraw, ImageFont
import os

img = Image.open('minu-minu planner A5-1.jpg') # 이미지 열기
fontsFolder = 'C:\Windows\Fonts' # 폰트 경로
draw = ImageDraw.Draw(img)

def draw_date():
    time = datetime.datetime.now() # 지금 시간
    date = str(time.date()) # 지금 날짜
    draw_date_font = ImageFont.truetype(os.path.join(fontsFolder, 'H2HDRM.ttf'), 100)
    draw.text((80, 95), date, fill="black", font=draw_date_font)


def draw_Dday():
    today = datetime.date.today()
    exam_date = datetime.date(2022, 11, 17)
    Dday = exam_date - today
    draw_Dday_font = ImageFont.truetype(os.path.join(fontsFolder, 'H2HDRM.ttf'), 100)
    if int(Dday.days) == 0:
        draw.text((780, 95), "D-day", fill="black", font=draw_Dday_font)
    elif int(Dday.days) < 0:
        draw.text((850, 95), "D+{0}".format(str(abs(Dday.days))), fill="black", font=draw_Dday_font)
    else:
        draw.text((780, 95), "D-{0}".format(str(Dday.days)), fill="black", font=draw_Dday_font)

def draw_comment():
    comments=[
"일곱 번 넘어져도, 여덟 번 일어나라. (동양의 사자성어)",
"성공에는 간단한 공식이 있다. 무엇이건 최선을 다해라. 모두들 그것을 좋아할 것이다. (샘 유잉)",
"어려움은 모든 것을 극복하는 것이다. (어니스트 헨리 섀클턴 경)",
"즐거움과 행동만으로도, 시간은 부족하다. (윌리엄 셰익스피어)",
"무엇보다도, 준비가 성공의 열쇠이다. (알렉산더 그레이엄 벨)",
"증기, 전기 및 원자력보다 더 강력한 원동력이 있다: 바로 인간의 의지이다. (알버트 아인슈타인)",
"새로운 아이디어를 가진 사람은, 그 아이디어가 성공할 때까지 강한 원동력을 발휘한다. (마크 트웨인)",
"촬영하지 않은 장면은, 무조건 잃어버리게 된다. (웨인 그레츠키)",
"자기 신뢰는 성공의 첫 번째 비결이다. (랄프 왈도 에머슨)",
"우리가 실패에서 배우면, 실패는 성공이 된다. (말콤 포브스)",
"실패는 단순히 이번에는 더 지능적으로 다시 시작할 수 있는 새로운 기회일 뿐이다. (헨리 포드)",
"실패는 선택지가 아니다. 모두가 성공해야 한다. (아놀드 슈왈제네거)",
"모든 스트라이크는, 나의 다음 홈런을 더욱 가까이 오게 한다. (베이브 루스)",
"주변에 주저앉아서 물건들이 너에게 오기를 기다리지 마라. 당신이 원하는 것을 위해 싸우고, 스스로 책임을 져라. (미셸 타누스)",
"모든 것이 각자의 아름다움을 지니고 있지만, 모든 사람들이 그 아름다움을 보지는 않는다. (공자)",
"인간은 성공을 누릴 필요가 있기 때문에, 그만한 어려움이 필요하다. (A.P.J. 압둘 칼람)",
"실수하지 않는 사람은 열심히 노력하지 않는다. (웨스 로버트)",
"탐험되지 않은 삶은 가치가 없다. (소크라테스)",
"성공의 80%가 서서히 나타나고 있다. (우디 앨런)",
"당신이 할 수 있다고 생각하든, 그렇지 않다고 생각하든 – 당신 말이 맞습니다. (헨리 포드)",
"네가 원하는 것을 위해 싸우지 않았다면, 잃어버린 것 때문에 울지 말아라. (익명)",
"이기는 것은 모든 것이 아니라, 유일한 것이다. (빈스 롬바르디)",
"항상 가장 큰 노력이 필요한 것이, 바로 모든 일의 시작이다. (제임스 캐시 페니)",
"최대한의 삶을 살고, 최대한 긍정적인 것에 집중하자. (매트 카메론)",
"너는 긍정적인 삶과 부정적인 생각을 동시에 가질 수 없다. (조이스 마이어)",
"긍정적인 생각과 결합된 긍정적인 행동은 성공을 불러온다. (시브 카에라)",
"지도자는 자신이 가야할 길을 알고, 그 길을 가고, 그 길을 보여준다. (존 C. 맥스웰)",
"혁신은 리더와 추종자를 구별한다. (스티브 잡스)",
"나는 사실 실용적인 몽상가이다. 꿈은 통풍이 잘 되지 않는다. 꿈을 가능한 한 현실로 바꾸고 싶다. (마하트마 간디)",
"잘못을 찾아라. 구제책을 찾지 마라. (헨리 포드)",
"웃어라, 온 세상이 너와 함께 웃을 것이다. 울어라, 너 혼자 울 것이다. (엘라 휠러 윌콕스)"
    ]  # 명언 모음
    num = random.randint(0, 30) # 명언 갯수
    draw_comment_font = ImageFont.truetype(os.path.join(fontsFolder, 'H2HDRM.ttf'), 20)
    draw.text((80, 285), comments[num], fill="black", font=draw_comment_font)

def is_int(a): # 문자열이 정수형으로 이루어져 있는지 판별 (draw_tasks()에서 사용)
    try:
        int(a)
        return True
    except ValueError:
        return False

def draw_tasks():
    num = input("과목 수를 입력해주세요. : ")
    try: # num에 정수를 입력했는지 판별
        num = int(num)
    except ValueError:
        while True:
            num=input("1부터 13까지의 수 중 하나를 정수형으로 입력해주세요. : ")
            if is_int(num):
                num = int(num)
                break

    task_titles = []
    task_contents = []
    for i in range(num):
        task_title = input("과목명을 입력해주세요. : ")
        task_titles.append(task_title)
        task_content = input("내용을 입력해주세요. : ")
        task_contents.append(task_content)

    draw_tasks_title_font = ImageFont.truetype(os.path.join(fontsFolder, 'H2HDRM.ttf'), 30)
    draw_tasks_content_font = ImageFont.truetype(os.path.join(fontsFolder, 'H2HDRM.ttf'), 25)

    for i in range(num):
        draw.text((95, 450+67*i), task_titles[i], fill="black", font=draw_tasks_title_font)
        draw.text((200, 453+67*i), task_contents[i], fill="black", font=draw_tasks_content_font)

def start():
    draw_date()
    draw_Dday()
    draw_comment()
    draw_tasks()
    img.save("aaa.jpg")

start()