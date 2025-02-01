from PyPDF2 import PdfReader
from googletrans import Translator

with open("2202071 lab report-2.pdf", 'rb') as file:
    reader = PdfReader(file)

    # Get total number of pages
    num_pages = len(reader.pages)

    translator = Translator()  # Initialize translator

    translated_texts = []  # Store translated text

    for p in range(num_pages):
        page = reader.pages[p]  # Correct way to access a page
        text = page.extract_text()  # Correct function to extract text

        if text:  # Translate only if text is present
            translated = translator.translate(text, src="en", dest="bn")  # No need for await
            translated_texts.append(translated.text)

# Print the translated text
for i, translated_text in enumerate(translated_texts, 1):
    print(f"\n--- Page {i} ---\n")
    print(translated_text)

with open("translated_text.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(translated_texts))



