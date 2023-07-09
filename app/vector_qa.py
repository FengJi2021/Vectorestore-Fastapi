from langchain.chat_models import ChatVertexAI
from langchain.vectorstores import DeepLake
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.chat_models import ChatVertexAI

class VectorQA:
    def __init__(
            self,
            model: ChatVertexAI=ChatVertexAI(),
            dataset_path: str="local_vector_db/langchain",
        ):
        self.dataset_path = dataset_path
        db_qa = DeepLake(dataset_path=dataset_path, read_only=True)
        retriever = db_qa.as_retriever()
        retriever.search_kwargs['distance_metric'] = 'cos'
        retriever.search_kwargs['k'] = 20

        model = ChatVertexAI()
        self.qa = RetrievalQA.from_llm(model, retriever=retriever)

    def process(self, msg: str) -> str:
        return self.qa.run(msg)
