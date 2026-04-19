from langchain_openai import ChatOpenAI
llama3 = ChatOpenAI (api_key = groq_api_key,
                     base_url = "https://api.groq.com/openAI/v1",
                     model = "llama3-8b-8192",
                    )
llama3
ai_msg = llama3.invoke ("Hi, how are you?")
print (ai_msg.content)
