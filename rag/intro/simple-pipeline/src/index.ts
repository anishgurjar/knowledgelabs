import { PDFLoader } from "@langchain/community/document_loaders/fs/pdf"

const PdfPath = "./src/docs/Selling-Guide_09-03-25_highlighting (1).pdf";

const loader = new PDFLoader(PdfPath)

const docs = await loader.load()

console.log(docs[0])

