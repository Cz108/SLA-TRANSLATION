# Test only
import os
import sys
from tools import snippets as tool
from docparser.docs_table_parser import load_document, get_cell_dict_in_selected_column, if_color_match_the_cell, get_cell_text
from docparser.docs_table_parser import check_table_colors, edit_cell_content

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/bilibala/Study/SLA-TRANS/cre/sla.json"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    target_language_code = 'bs'
    doc_path = '/Users/bilibala/Study/SLA-TRANS/documents/test1.docx'
    doc = load_document(doc_path)

    print("\nINFO: check_table_colors(doc)")
    table_colors = check_table_colors(doc)

    for source_cell_dict, target_cell_dict in zip(get_cell_dict_in_selected_column(doc, 2), get_cell_dict_in_selected_column(doc, 3)):
        if if_color_match_the_cell(source_cell_dict['object'], "FFFFFF") or if_color_match_the_cell(source_cell_dict['object'], "F5DEB3"):
            translated_text = tool.translate_text(target_language_code, get_cell_text(source_cell_dict['object']))
            print('-'*50)
            print(get_cell_text(source_cell_dict['object']))
            print(translated_text['translatedText'])

            if edit_cell_content(doc, target_cell_dict['index'], translated_text['translatedText']):
                print("Cell content modified successfully.")
            else:
                print("Failed to modify cell content.")

    doc.save(doc_path)


