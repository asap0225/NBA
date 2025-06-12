from django.shortcuts import render, get_object_or_404
from .models import Player
import requests
import json

LLAMA_API_URL = "https://openrouter.ai/api/v1/chat/completions"
LLAMA_API_KEY = "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"  # 보안상 생략했지만 실제론 전체 키 입력

def llama_analysis(prompt):
    try:
        resp = requests.post(
            LLAMA_API_URL,
            json={
                "model": "meta-llama/llama-3.3-8b-instruct:free",  # 더 높은 품질 모델 사용
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
            },
            headers={"Authorization": f"Bearer {LLAMA_API_KEY}"}
        )

        print("응답 상태 코드:", resp.status_code)
        print("응답 본문:", resp.text)

        data = resp.json()
        if 'choices' in data and len(data['choices']) > 0:
            return data['choices'][0]['message']['content']
        else:
            return "[오류] 분석 결과가 없습니다. 응답 형식을 확인하세요."
    except Exception as e:
        return f"[API 호출 실패] {str(e)}"

def home(request):
    players = Player.objects.all()
    return render(request, 'main/home.html', {'players': players})

def player_analysis(request, player_id):
    player = get_object_or_404(Player, pk=player_id)

    prompt = (
        f"{player.name}의 2025 시즌 주요 NBA 스탯을 기반으로 다음 JSON 형식으로 분석해줘.\n"
        f"- 'stats'는 영어 키(key)를 사용하고, value는 float 또는 int 형식\n"
        f"- 'analysis'는 최소 5문장 이상, 문법 오류 없이 한국어로 작성\n"
        f"- 분석 내용은 디테일하고 논리적으로 정리해줘. 과장 표현 없이 정확하게.\n"
        f"- 오타, 줄임말, 잘못된 띄어쓰기 없이 자연스럽고 매끄럽게 작성해줘.\n\n"
        f"예시 형식:\n"
        f"""{{
  "stats": {{
    "points": 27.7,
    "rebounds": 11.5,
    "assists": 6.3,
    "steals": 1.9,
    "blocks": 1.2
  }},
  "analysis": "LeBron James는 2025 시즌에도 여전히 전방위적인 활약을 보여주고 있습니다. 특히 리바운드와 득점에서 팀의 핵심 역할을 하며, 경기 전체의 흐름을 조율하는 능력이 뛰어납니다. 그의 어시스트 수치는 플레이메이킹 능력을 반영하고 있으며, 수비에서도 적극적인 개입을 통해 팀에 안정감을 줍니다. 기술적인 완성도와 경기 운영 능력을 바탕으로 그는 여전히 리그 최고의 선수 중 한 명으로 평가받고 있습니다. 전반적으로 팀에서 중심적인 존재로 활약하고 있습니다."
}}"""
    )

    analysis = llama_analysis(prompt)

    try:
        parsed = json.loads(analysis)
        stats = parsed.get("stats", {})
        analysis_text = parsed.get("analysis", "")
    except Exception as e:
        stats = {}
        analysis_text = f"[분석 오류] JSON 형식이 아닙니다. 원본 출력:\n\n{analysis}"

    return render(request, 'main/player_analysis.html', {
        'player': player,
        'stats': stats,
        'analysis_text': analysis_text
    })



