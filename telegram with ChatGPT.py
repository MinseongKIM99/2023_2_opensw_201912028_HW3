from openai import OpenAI
import telegram
import asyncio

# 텔레그램 봇 설정
token = "6736572403:AAFqSX_mS5AyGZ0c5bSHP4bmtBvJ_MLWtrE"
bot = telegram.Bot(token=token)
mychat = '6633530090'
public_chat_name = "@K2019test"

# OpenAI 키
client = OpenAI(
    api_key="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"
    )

# 질문 내용
message="인구수 많은 나라 3개만 알려줘"

# 메시지를 보내는 함수
def job():
    response = chatGPT(message)
    asyncio.run(bot.sendMessage(chat_id=public_chat_name, text=response))
    print(f"Sent message: ", message)

# ChatGPt에 메세지 전달하여 답변얻기
def chatGPT(user_input):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    job()