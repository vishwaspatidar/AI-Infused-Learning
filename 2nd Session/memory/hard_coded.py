from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly tutor."),     # ① personality, like Class 1
    MessagesPlaceholder("history"),              # ② past turns park here
    ("human", "{question}"),                     # ③ the new question
])
model  = ChatGroq(model="openai/gpt-oss-120b", temperature=0.3)

chain = prompt | model

history = [HumanMessage("My name is vishwas."), AIMessage("Hi vishwas!")]
print(chain.invoke({"history": history, "question": "What's my name and age?"}).content)
# → "Your name is Aarav."  ✅ it "remembered" — because WE re-sent the history