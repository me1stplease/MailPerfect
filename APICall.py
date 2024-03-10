from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from io import StringIO
import pandas as pd

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")


def GeminiCall(wStyle, user, task, llmIn=llm):
    err ='There is some error getting the result or input may contain some abusive or harmful content. Please try again.'
    try:
        if len(wStyle) == 0 or wStyle is None:
            if task == "Email Formation":
                prompt = "You are tool for email formation of \"" + user + "\" with proper salutation, signature and " \
                                                                        "subject."
            elif task == "Rewording (Improve)":
                prompt1 = "You are tool for rephrasing the content of \"" + user + "\" and don't provide options."
                temp = llmIn.invoke(prompt1)
                prompt = "\"" + temp.content + "\" Don't alter the content just add salutation, signature and subject if " \
                                            "not " \
                                            "present."
            elif task == "Grammar Correction":
                prompt1 = "You are Grammar Correction tool for the content of \"" + user + "\" and don't provide options."
                temp = llmIn.invoke(prompt1)
                prompt = "\"" + temp.content + "\" Don't alter the content just add salutation, signature and subject if " \
                                            "not " \
                                            "present."
            else:
                prompt1 = "You are tool for rephrasing the content of \"" + user + "\" and don't provide options."
                temp = llmIn.invoke(prompt1)
                prompt = "\"" + temp.content + "\" Don't alter the content just add salutation, signature and subject if " \
                                            "not " \
                                            "present."
        else:
            ws = str(wStyle)
            if task == "Email Formation":
                prompt = "You are tool for email formation of \"" + user + "\" with proper salutation, signature and " \
                                                                        "subject in the listed writing style used in a " \
                                                                        "single mail: " + ws
            elif task == "Rewording (Improve)":
                prompt1 = "You are tool for rephrasing the content of \"" + user + "\" " + " in the listed writing style: " + ws + " and don't provide options."
                temp = llmIn.invoke(prompt1)
                prompt = "\"" + temp.content + "\" Don't alter the content just add salutation, signature and subject if " \
                                            "not " \
                                            "present."
            elif task == "Grammar Correction":
                prompt1 = "You are Grammar Correction tool for the content of \"" + user + "\" " + " and" \
                                                                                                                    " don't provide options."
                temp = llmIn.invoke(prompt1)
                prompt = "\"" + temp.content + "\" Don't alter the content just add salutation, signature and subject if " \
                                            "not " \
                                            "present."
            else:
                prompt1 = "You are tool for rephrasing the content of \"" + user + "\" " + " in the listed writing style: " + ws + " and don't provide options."
                temp = llmIn.invoke(prompt1)
                prompt = "\"" + temp.content + "\" Don't alter the content just add salutation, signature and subject if " \
                                            "not " \
                                            "present."

        # prompt = "'{user}' rephrase the content".format( user="Hi I got this idea in mind, but I haven't really thought
        # deeply about how to make it happen. It would be good to hear ideas from other teammates so that we can
        # collectively decide on the most practical automation idea. Thanks and Regards, Mahtab Alam")

        result = llmIn.invoke(prompt)
        print(result.content)
        return result.content
    except Exception as e:
        print(e.args[0])
        # return e.args[0]
    return err


def senAnalyze(wStyle, genMail, llmIn=llm):
    output = None
    if len(wStyle) == 0 or wStyle is None:
        pass
    else:
        ws = str(wStyle)
        prompt = "Give score to the following email based on the listed writing style " + ws + " in the table format with 3 columns 1.criteria, 2.score %, 3.reason. '" + genMail + "'"
        result = llmIn.invoke(prompt)
        output = StringIO(result.content)
        df = pd.read_table(output, delimiter="|")
        df = df.drop(0, axis='index')
        output = df

    return output
