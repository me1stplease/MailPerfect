from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")


def GeminiCall(user, task, llmIn=llm):
    if task == "Email Formation":
        prompt = "You are tool for email formation of \"" + user + "\" with proper salutation, signature and subject."
    elif task == "Rewording (Improve)":
        prompt1 = "You are tool for rephrasing the content of \"" + user + "\" and please give only one answer."
        temp = llmIn.invoke(prompt1)
        prompt = "Don't alter the content just add salutation, signature and subject if not present of " + temp.content + "."
    elif task == "Grammar Correction":
        prompt1 = "You are Grammar Correction tool for the content of \"" + user + "\"."
        temp = llmIn.invoke(prompt1)
        prompt = "Don't alter the content just add salutation, signature and subject if not present of " + temp.content + "."
    else:
        prompt1 = "You are tool for rephrasing the content of \"" + user + "\" and please give only one answer."
        temp = llmIn.invoke(prompt1)
        prompt = "Don't alter the content just add salutation, signature and subject if not present of " + temp.content + "."

    # prompt = "'{user}' rephrase the content".format( user="Hi I got this idea in mind, but I haven't really thought
    # deeply about how to make it happen. It would be good to hear ideas from other teammates so that we can
    # collectively decide on the most practical automation idea. Thanks and Regards, Mahtab Alam")

    result = llm.invoke(prompt)
    print(result.content)
    return result.content
