from openai import OpenAI
import telegram
import asyncio

# 텔레그램 봇 설정
token = "Your_token"
bot = telegram.Bot(token=token)
mychat = 'Your_bot_id'
public_chat_name = "Your_chat_id"

# OpenAI 키
client = OpenAI(
    api_key="Your_apikey"
    )

# 질문 내용
message="질문 내용"

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
