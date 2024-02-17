import streamlit as st
from APICall import GeminiCall as GenAI

st.title("MailPrefect")
st.caption(
    'A web app powered by GenAI designed to form perfect email with the capability to correct grammar and reword the '
    'email content.')

task = "rephrase"
with st.sidebar:
    st.header('Task', divider='rainbow')
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email Formation", "Rewording (Improve)", "Grammar Correction"),
        index=None,
        placeholder="Task Options...",
    )
    if option is not None:
        task = option
    st.write('You selected:', option)

st.header("Enter your Input")
txt = st.text_area(
    "This place belong to the user..."
)
if txt != "" and task is not None:
    st.write(f'You wrote {len(txt)} characters.')
    st.header("Your Mail: ")
    st.write(GenAI(txt, task))
