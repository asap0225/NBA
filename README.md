#초기 세팅
pip install django matplotlib pandas openai requests 

#LLM API 세팅
views.py 파일 "PUT YOUR KEY"부분에 API키 입력하세요

#웹사이트에 선수 추가하는 방법
(#cmd)
python manage.py shell
from main.models import Player
Player.objects.create(name="Russell Westbrook(#선수 이름)", position="PG(#포지션)", team="Denver Nuggets(#팀이름)", 
image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Russell_Westbrook_%28March_21%2C_2022%29_%28cropped%29.jpg/330px-Russell_Westbrook_%28March_21%2C_2022%29_%28cropped%29.jpg(#이미지)')

#웹사이트 열기
커맨드에 python manage.py runserver 입력하시고
터미널에 뜬 http://127.0.0.1:8000/ 를 ctrl+좌클릭 하시면 됩니다.
