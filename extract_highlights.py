import sys
import fitz


def extract_highlights(pdf_path):
    doc = fitz.open(pdf_path)
    highlight_texts = []
    for page in doc:
        annots = page.annots()
        if annots is None:
            continue
        for annot in annots:
            if annot.type[0] == fitz.PDF_ANNOT_HIGHLIGHT:
                text = page.get_textbox(annot.rect).strip()
                if text:
                    highlight_texts.append(text)
    return highlight_texts


def write_highlights_to_pdf(texts, output_path):
    doc = fitz.open()
    for text in texts:
        page = doc.new_page()
        page.insert_text((72, 72), text)
    doc.save(output_path)


def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_highlights.py input.pdf output.pdf")
        return
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    highlights = extract_highlights(input_pdf)
    for text in highlights:
        print(text)
    write_highlights_to_pdf(highlights, output_pdf)


if __name__ == "__main__":
    main()
