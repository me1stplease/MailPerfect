import numpy as np
import pandas as pd
import streamlit as st
from APICall import GeminiCall as GenAI
from APICall import senAnalyze as analysis
from EnDe import keyGen,encrypt,decrypt
from GetPii import getPii
from EnCrypthPii import encpi

def ui():
    st.set_page_config(page_title = "MailPrefect")

    st.title("MailPrefect")
    st.caption(
        'A web app powered by GenAI designed to form perfect email with the capability to ' +
        'correct grammar and reword the email content.')

    global task
    with st.sidebar:
        st.header('Task', divider='rainbow')
        option = st.radio(
            "What task you want to perform?",
            ("Email Formation", "Rewording (Improve)", "Grammar Correction"),
            index=0,
        )
        if option is not None:
            task = option
        st.write('You selected:', option)

    st.header("Enter your Input")
    txt = st.text_area(
        "This place belong to the user..."
    )


    style = st.multiselect(
        'Select the writing styles :',
        ['Clear and concise', 'use facts', 'use evidence and logic', 'Polite',
         'structured', 'avoid colloquial language', 'relaxed language', 'Conversational',
         'Emphasize creativity', 'Formal', 'follow the inverted pyramid structure'])

    # st.write(style)

    if st.button("Create", type="primary"):

        if txt != "" and task is not None:
            #get Piis
            pii = getPii(txt)

            #Encryption and decryption key Generation
            alpha = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_@')
            EnDekey = keyGen(alpha)

            # Encrytion of pii
            encrypted = []
            for p in pii:
                encrypted.append(encrypt(alpha, EnDekey, p))
            # print('---')
            # print(alpha)
            # print(EnDekey)
            # print(encrypted)

            # Decryption of pii
            decrypted = []
            for e in encrypted:
                decrypted.append(decrypt(alpha, EnDekey, e))
            # print('---')
            # print(alpha)
            # print(EnDekey)
            # print(decrypted)
        
            st.write(f'You wrote {len(txt)} characters.')

            st.divider()

            st.subheader("Your email is being generated...")

            encText = encpi(txt,pii,encrypted)
            print('EncText : ',encText)

            genRes = GenAI(style, txt, encText)

            decText = encpi(genRes,encrypted,decrypted)

            generatedMail = decText

            with st.container(border=True):
                st.markdown(generatedMail)

            st.divider()

            if generatedMail !='There is some error getting the result or input may contain some abusive or harmful content. Please try again.':

                df = analysis(style, generatedMail)

                if df is not None:
                    # if st.button("Click for Writing Style Analysis", type="secondary", use_container_width=True):
                    st.subheader(':blue[Analysis] :bookmark_tabs:')
                    # print(df)
                    df.iloc[:, 2].str.strip()
                    df.iloc[:, 2] = df.iloc[:, 2].str.replace(r'\W', '', regex=True)
                    df.iloc[:, 2] = df.iloc[:, 2].map(int)
                    chart_data = pd.DataFrame(
                        {
                            "Criteria": df.iloc[:, 1].tolist(),
                            "Score(%)": df.iloc[:, 2].tolist(),
                        }
                    )
                    st.bar_chart(chart_data, x="Criteria", y="Score(%)")

                    with st.expander("Detailed explanation"):
                        reason = df.iloc[:, 3].tolist()
                        criteria = df.iloc[:, 1].tolist()
                        for i in range(len(criteria)):
                            st.write(criteria[i]+" : ")
                            st.caption(reason[i])

                # st.write("")

        else:
            st.write("Please provide the input and select the task")


if __name__ == '__main__':
    ui()
