Local vector database
=====================

# Description
This directory contains the local vector database. The database is generated from deeplake 

# How to use
```python
from langchain.vectorstores import DeepLake

db = DeepLake( data_path='local_vector_db/your_target_db', read_only=True )
query = 'your query'

db.similarity_search(query)
```

