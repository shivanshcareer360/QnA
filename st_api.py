from dotenv import load_dotenv
from services.prompt import prompt_response
import streamlit as st

# Load environment variables from .env file
load_dotenv()


def output():
    st.title('Welcome to Careers360 QnA')
    user_question = st.text_input("Type your message...")
    obj=prompt_response()
    if user_question:
        response=obj.ask_question(user_question)
        st.write("Answer:", response['answer'])
        st.write("For more detail you may click on the link below:")
        st.write(response['sources'])

    else:
        pass
if __name__ == '__main__':
    output()