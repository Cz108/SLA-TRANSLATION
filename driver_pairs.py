import os
import sys
from tools import snippets as tool
from docparser.docs_general_parser import load_document, skip_empty_paragraph
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/bilibala/Study/SLA-TRANS/cre/sla.json"


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    doc = load_document('/documents/duizhao_xml.docx')

    target_language_code = 'sr'

    for para in doc.paragraphs:
        if skip_empty_paragraph(para):  # Ignore empty paragraphs
            translated_text = tool.translate_text(target_language_code, para.text)
            print('-' * 50)
            print(para.text)
            para.text = f"{para.text} \n{translated_text['translatedText']}"
            print(translated_text['translatedText'])

    # Save the modified content back to the DOCX file
    doc.save('/Users/bilibala/Study/SLA-TRANS/documents/duizhao_xml_modified.docx')

