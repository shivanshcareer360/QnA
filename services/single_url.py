from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import pickle as pkl 
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
import os
 

basepath=os.getcwd()
print(basepath)


class IITD:
    def __init__(self):
        self.url_path=['https://www.careers360.com/university/indian-institute-of-technology-delhi',
                       'https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india']


    def load_url(self):
        try:
            loaders = UnstructuredURLLoader(urls=self.url_path)
            data = loaders.load()
            return data
        except Exception as e:
            print(f'Error message of load_url method: {e}')


    def splitting(self, data):
        try:
            text_splitter = CharacterTextSplitter(separator='\n',
                                                chunk_size=800,
                                                chunk_overlap=50)


            docs = text_splitter.split_documents(data)
            return docs

        except Exception as e:
            print(f"Error message in splitting methiod: {e}")    


    def embeddings(self, docs):
        try:
            embeddings = OpenAIEmbeddings()
            knowledge_base = FAISS.from_documents(docs, embeddings)
            knowledge_base.save_local("./faissDB")
        except Exception as e:
            print(f"Error message in embedding method: {e}")    
    

    def runall(self):
        try:
            data=self.load_url()
            docs=self.splitting(data)
            self.embeddings(docs)
        except Exception as e:
            print(f"Error message in run all method: {e}")