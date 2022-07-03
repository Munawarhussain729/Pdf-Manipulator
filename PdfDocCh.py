from PyPDF2 import PdfFileReader

def ExtractInfo(pdfName):
    with open(pdfName,"rb") as pdf:
        read = PdfFileReader(pdf)
        info = read.getDocumentInfo()
        NoOfPages = read.getNumPages()
        text = f"""
        Information About:{pdfName}:
            Author : {info.author}
            Creartor: {info.creator}
            Producer: {info.producer}
            Title: {info.title}
            Number Of Pages : {NoOfPages}
        """
        return text

print(ExtractInfo("Resume.pdf"))