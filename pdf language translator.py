

from PyPDF2 import PdfReader #install the PyPDF2
from googletrans import Translator #install googletrans

# Open the PDF file in binary mode
with open("Bangladesh.pdf", 'rb') as file: #pdf path
    reader = PdfReader(file)

    # Get total number of pages
    num_pages = len(reader.pages)  # ✅ Use len(reader.pages) instead of numpages

    translator = Translator()  # Initialize translator

    translated_texts = []  # Store translated text

    for p in range(num_pages):
        page = reader.pages[p]  # ✅ Use reader.pages[p] instead of getPage(p)
        text = page.extract_text()  # ✅ Use extract_text() instead of extractText()

        if text:  # Only translate if text is present
            translated_text = translator.translate(text, src="en", dest="ar").text #pdf language and pdf converted language
            translated_texts.append(translated_text)

# Print the translated text
for i, translated_text in enumerate(translated_texts, 1):
    print(f"\n--- Page {i} ---\n")
    print(translated_text)

# (Optional) Save the translated text to a file
with open("translated_text.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(translated_texts))

