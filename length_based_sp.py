from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader("Agentic_AI_On_AWS.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separator=""
)

result = splitter.split_documents(docs)

print(result[0].page_content)