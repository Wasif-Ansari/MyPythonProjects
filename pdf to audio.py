import PyPDF2,pyttsx3

path = open("path to pdf",'rb') #open in binary form

pdfReader = PyPDF2.PdfFileReader(path)

speak = pyttsx3.init()

for pages in range(pdfReader.numPages):
    text = pdfReader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()

speak.stop()