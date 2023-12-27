from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.llms import OpenAI


class prompt_response:
    pass

    def ask_question(self, user_question):
        embeddings = OpenAIEmbeddings()
        loadvec=FAISS.load_local("./faissDB", embeddings)
        if user_question==None:
            pass    

        else:
            try:
                llm=OpenAI(temperature=0)
                chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, 
                                                             retriever=loadvec.as_retriever())
                response=chain({"question": user_question}, 
                               return_only_outputs=True)

                return response
            except Exception as e:
                return f"Error message: {e}"