import pyttsx3
import PyPDF2

# Anytning File Open to open method
book = open("python_programming_mark_lutz.pdf", "rb")

# PdfFileReader book init
pdfFileReader = PyPDF2.PdfFileReader(book)

# Count of Total pdf page
number_of_page = pdfFileReader.numPages

print(number_of_page)
# Initialize python text to speech
My_Friend = pyttsx3.init()

for num in range(number_of_page):
    # page ta dhoro get page Method call kore
    page = pdfFileReader.getPage(26)

    # Akhon page theke text dorte hobe
    text = page.extractText()

    # Tomar Friend Kichu Bolte Chai
    My_Friend.say(text)

    # Let's Go
    My_Friend.runAndWait()
