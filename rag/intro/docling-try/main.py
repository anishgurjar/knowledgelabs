from langchain_docling import DoclingLoader

FILE_PATH = "./docs/fannie_selling_guide.pdf"

loader = DoclingLoader(file_path=FILE_PATH)

docs = loader.load()

print("1", docs[0])
print("2", docs[1])
print("3", docs[2])
print("4", docs[3])
print("5", docs[4])
print("6", docs[5])
print("7", docs[6])
print("8", docs[7])
print("9", docs[8])
print("10", docs[9])