from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle as pkl 
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
import os


load_dotenv()

basepath=os.getcwd()


class IITD:
    def __init__(self):
        self.url_path='./urls/iitd_urls.pkl'

    def load_url(self):
        try:
            with open(self.url_path,'rb') as r:
                urls=pkl.load(r)
                loaders = UnstructuredURLLoader(urls=urls)
                data = loaders.load()
            return data
        except Exception as e:
            print(f'Error message of load_url method: {e}')


    def splitting(self, data):
        try:
            text_splitter = CharacterTextSplitter(separator='\n',
                                                chunk_size=1000,
                                                chunk_overlap=200)


            docs = text_splitter.split_documents(data)
            return docs

        except Exception as e:
            print(f"Error message in splitting methiod: {e}")    


    def embeddings(self, docs):
        try:
            embeddings = OpenAIEmbeddings()
            knowledge_base = FAISS.from_documents(docs, embeddings)
            knowledge_base.save_local("./faissDB")
            # return knowledge_base
        except Exception as e:
            print(f"Error message in embedding method: {e}")    
    

    def runall(self):
        try:
            data=self.load_url()
            docs=self.splitting(data)
            self.embeddings(docs)
        except Exception as e:
            print(f"Error message in run all method: {e}")