import openai
# OpenAI chatGPT API 입니다.
# API 키를 입력하면 바로 사용 가능합니다.
def GPT_ask(Prompt, Max_token):
    openai.api_key = "Your API Key"
    stream = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        # model="text-davinci-003"
        temperature=0.3,
        max_tokens=int(Max_token),
        messages=[{"role": "user", "content": str(Prompt)}],
        stream=True,
    )
    answer = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            # print(chunk.choices[0].delta.content, end="")
            answer = answer + (chunk.choices[0].delta.content)
    return answer