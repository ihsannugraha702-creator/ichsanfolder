import streamlit as st

st.title("🎈ichsanfolder")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[habil] :green[orang] :blue[garut] :violet[asli]
    :gray[habil] :rainbow[maung] and :blue-background[bandung] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
import streamlit as st


v=12
v%=7
print(v)
