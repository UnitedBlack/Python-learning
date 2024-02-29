import g4f
from g4f.Provider import (
    DeepAi,        # works
    HuggingChat,  # auth LLAMA-2
    OpenAssistant,  # auth
    Theb,       # auth
    Wewordle,   # gpt3
    Yqcloud,    # gpt3
    ChatgptAi

)


# usage:
response = g4f.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user",
               "content": "Расскажи про цепную реакцию как будто пятилетнему ребенку"}],
    stream=True,
    provider=DeepAi)

# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello world"}],
#     stream=True,     b
# )

for message in response:
    print(message, flush=True, end='')
