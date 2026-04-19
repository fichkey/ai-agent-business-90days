!pip install langchain_openai
from langchain_openai import ChatOpenAI
llama3 = ChatOpenAI (api_key = groq_api_key,
                     base_url = "https://api.groq.com/openai/v1",
                     model = "llama-3.3-70b-versatile",
                    )
llama3
ai_msg = llama3.invoke ("Hi, how are you?")
print (ai_msg.content)
