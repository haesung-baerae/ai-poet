import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from dotenv import load_dotenv
#load_dotenv()

llm = init_chat_model('gpt-4o-mini', model_provider= 'openai')
# init_chat_model : 벤더 추상화
# 이렇게 변경 가능
# llm = init_chat_model("claude-3-sonnet", model_provider="anthropic") 

prompt = ChatPromptTemplate.from_messages([
    #('system', 'You are a helpful assistant'),
    ('system', "너는 한국어로 은유를 잘 쓰는 시인이다."),
    ('user', '{input}')
])
# from_template : 단일 텍스트, system prompt 사용 제한적, 대화 확장 불편 -> 텍스트 프롬프트로서 간단한 체인/비채팅 모델용
# from_message : role 기반(system/user/assistant), system prompt 자연스로움, 대화 확장 좋음
#   -> 의도 전달 정확도가 높고, system/user/assistant 분리가 되어 제어력이 높음



parser = StrOutputParser()

chain = prompt|llm|parser

st.title("인공지능 시인")

content = st.text_input("시의 주제를 제시해주세요.")
st.write("시의 주제는 ",content)
if st.button("시 작성 요청하기"):
    with st.spinner('Wait for it...'):
        result = chain.invoke({'input':content+'에 대한 시를 써줘'})
        st.write(result)