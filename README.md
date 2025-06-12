#초기 세팅
pip install django matplotlib pandas openai requests 

#선수 추가
(#cmd)
python manage.py shell
from main.models import Player
Player.objects.create(name="Russell Westbrook(#선수 이름)", position="PG(#포지션)", team="Denver Nuggets(#팀이름)", 
image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Russell_Westbrook_%28March_21%2C_2022%29_%28cropped%29.jpg/330px-Russell_Westbrook_%28March_21%2C_2022%29_%28cropped%29.jpg(#이미지)')
