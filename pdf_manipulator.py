from asyncore import read, write
from csv import reader
from doctest import OutputChecker
from fileinput import filename
import quopri
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfWriter
import os

from bs4 import PageElement

def ExtractInfo():
    fileName = input("Enter Name of File: ")
    if(os.path.exists(fileName)):
        with open(fileName,'rb') as file:
            pdf = PdfFileReader(file)
            information  = pdf.getDocumentInfo()
            TotalPages = pdf.getNumPages()
            txt = f"""
            Information about {fileName}:
            Author : {information.author}
            Creator: {information.creator}
            Prodcuer: {information.producer}
            Subject: {information.subject}
            Title: {information.title}
            Number of Pages: {TotalPages}"""

            print(txt)

def ClockWiseRotation(fileName, PageNumbers, outFileName):
    writer = PdfFileWriter()
    with open(fileName,'rb') as file:
        reader = PdfFileReader(file)
        for x in range(reader.getNumPages()):
            if x in PageNumbers:
                writer.addPage(reader.getPage(int(x)).rotateClockwise(90))
            else:
                writer.addPage(reader.getPage(int(x)))
    
        with open(outFileName,'wb') as output:
            writer.write(output)

def AntiClockwise(fileName, PageNumber, outFileName):
    writer = PdfFileWriter()
    with open(fileName,'rb') as file:
        reader = PdfFileReader(file)
        for x in range(reader.getNumPages()):
            if x in PageNumber:
                writer.addPage(reader.getPage(int(x)).rotateCounterClockwise(90))
            else:
                writer.addPage(reader.getPage(int(x))) 
        with open(outFileName,'wb') as file:
            writer.write(file)


def Merge(NoOfFiles):
    FileNames = []
    for x in range(NoOfFiles):
        fileName = input("Enter the Name of File ")
        if(os.path.exists(fileName)):
            FileNames.append(fileName)
        else:
            NoOfFiles = NoOfFiles+1
    
    outPut = input("Enter the Name of Out Put File ")
    writer = PdfFileWriter()
    for file in FileNames:
        reader = PdfFileReader(file)
        for x in range(reader.getNumPages()):
            writer.addPage(reader.getPage(int(x)))
    
    with open(outPut, 'wb') as file:
        writer.write(file)  

def Splitter( ):
    fileName = input("Enter the Name of File you want to split: ")
    if(os.path.exists(fileName)):
        PageToSplit = int(input("Enter the Number of Page you want to Split: "))
        outPutFile = input("Enter the Name of OutPut File: ")
        writer1 = PdfFileWriter()
        writer2 = PdfFileWriter()

        reader = PdfFileReader(fileName)
        for x in range(PageToSplit):
            writer1.addPage(reader.getPage(int(x)))
        for x in range(PageToSplit, reader.getNumPages()):
            writer2.addPage(reader.getPage(x))
        
        with open(fileName,'wb') as file:
            writer1.write(file)

        with open(outPutFile,'wb') as file:
            writer2.write(file)
    else:
        print("File Does not Exists ")


def Encrypter():
   fileName = input(" Enter the Name of File ")
   if(os.path.exists(fileName)):
        password = input("Enter Password For File: ")
        writer = PdfFileWriter()
        reader = PdfFileReader(fileName)
        for page in range(reader.getNumPages()):
            writer.addPage(reader.getPage(page))
        
        writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
        with open(fileName, 'wb') as file:
            writer.write(file)


def FileRotator():
    fileName = input(" Enter the Name of File ")
    if(os.path.exists(fileName)):
       
        NoOfPages = input("Enter the Number of Pages You want to Rotate: ")
        outPutFile = input("Enter the Name of OutPut File: ")
        choice = input("Enter C to rotate Clockwise and A to rotate AntiClockWise: ")
        pageNumbers = []
        for x in range(int(NoOfPages)):
            num = input("Enter the Page Number to Rotate: ")
            if(num.isnumeric()):
                pageNumbers.append(int(num))
            else:
                NoOfPages = NoOfPages+1

        
        if(choice.lower() == "c"):
            ClockWiseRotation(fileName, pageNumbers, outPutFile)
        elif(choice.lower() == "a"):
            AntiClockwise(fileName, pageNumbers, outPutFile)
        else:
            print("Sorry! Invalid Choice ")
    else:
        print("Sorry! File Does Not Exists ")



def __main__():
    print("|--------------------------------------------------|")
    print("|---- Welcome to Pdf Manipulator " + "\N{grinning face}" + " ---------------|")
    print("|-Enter (Rotate) to Rotate some Pages of pdf File -|")
    print("|-Enter (Merge) to merge Multiple pdf Files -------|")
    print("|-Enter (Split) to Split a pdf File into 2 Files --|")
    print("|-Enter (Encrypt) to encrypt a pdf File -----------|")
    print("|-Enter (info) to Extract info Related to Pdf File |")
    print("|--------------------------------------------------|")
    choice = input(" Enter your Choice ")

    if (choice.lower() == "rotate"):
        FileRotator()
    elif (choice.lower() == "merge"):
        NoOfFile = int(input("Enter the Number of Files You want to Merge: "))
        Merge(NoOfFile)
    elif (choice.lower() == "split"):
        Splitter()
    elif (choice.lower() == "encrypt"):
        Encrypter() 
    elif (choice.lower() == "info"):
        ExtractInfo()
    else:
        print("Wrong Choice")


if __name__ == __main__():
    __main__()