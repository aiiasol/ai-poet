# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요. ')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = llm.predict(content + "에 대한 시를 써줘")
        st.write(result)


# Advertisement JavaScript
advertisement_script = """
<script src="https://ads-partners.coupang.com/g.js"></script>
<script>
    new PartnersCoupang.G({"id":769781,"template":"carousel","trackingCode":"AF7086871","width":"680","height":"140","tsource":""});
</script>
"""

st.write(advertisement_script, unsafe_allow_html=True)
