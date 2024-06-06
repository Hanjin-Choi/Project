from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI
from django.conf import settings
from finances.models import Finance, Option
# Create your views here.

txt_file_path = './combined_finance_data.txt'

# 파일 전체 내용을 한 줄의 문자열로 읽기
with open(txt_file_path, 'r', encoding='utf-8') as txtfile:
    content = txtfile.read()

OPEN_API=settings.OPEN_API

@api_view(['POST'])
def chatbot(request):
    user_input = request.data.get('message')
    client = OpenAI(api_key=OPEN_API,)
    # OpenAI API 호출
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
        {"role": "system", "content": "You are a finance product recommend assistant."},
        {"role": "user", "content": f"만약 특정은행에 대한 상품을 물어볼 때, {content} 데이터를 참고해서 대답해줘. 예시로 Q.경남은행의 상품을 추천해 주세요. A. 경남은행은 BNK더 조은정기예금, BNK주거래우대정기예금, BNK MY 원픽 정기예금, The 든든 예금이 있습니다. Q. BNK MY 원픽 정기예금에 대해 설명 해줘 A. BNK MY 원픽 정기예금은 단리 상품이며 3,6,12개월 상품이 있습니다. 최대 우대 금리는 12개월 상품인 3.55%입니다. Q. 대구은행 적금상품 추천해줘 A. 대구은행 적금상품은 4가지가 있으며 그 중 영플러스적금이 우대금리가 4.21로 제일 높습니다. 대답은 마크다운 형식이 아니라 string형식으로 문장마다 줄바꿈 문자인 <br>으로 대답해줘"},
        {"role": "user", "content": f'{user_input}, 대답은 마크다운 형식이 아니라 string형식으로 문장마다 줄바꿈 문자인 <br>으로 대답해줘'},
  ])


    bot_response = completion.choices[0].message.content

    return Response({'message':bot_response})