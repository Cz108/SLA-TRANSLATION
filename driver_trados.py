import os
import sys
from tools import snippets as tool
from tools.folder_tree import open_docx_files_in_directory
from tools.chatgpt import repeat_sentece, calculate_per_k_cost
from docparser.docs_table_parser import load_document, get_cell_dict_in_selected_column, if_color_match_the_cell, get_cell_text
from docparser.docs_table_parser import check_table_colors, edit_cell_content

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/bilibala/Study/SLA-TRANS/cre/sla.json"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    target_language_code = 'bs'
    root_directory = "/Users/bilibala/Documents/Tmp/bg&hr&el&sr"
    file_path_list, file_name_list = open_docx_files_in_directory(root_directory)
    total_price = float(0)

    for doc_path, doc_name in zip(file_path_list, file_name_list):
        # doc_path = '/Users/bilibala/Study/SLA-TRANS/documents/test1.docx'

        doc = load_document(doc_path)

        print(f"""\nINFO: {doc_path}""")
        target_language_code = input("Please enter the target_language_code: ")

        print("\nINFO: check_table_colors(doc)")
        table_colors = check_table_colors(doc)

        for source_cell_dict, target_cell_dict in zip(get_cell_dict_in_selected_column(doc, 2), get_cell_dict_in_selected_column(doc, 3)):
            if if_color_match_the_cell(source_cell_dict['object'], "FFFFFF") or if_color_match_the_cell(source_cell_dict['object'], "F5DEB3"):

                gcp_translated_text = tool.translate_text(target_language_code, get_cell_text(source_cell_dict['object']))['translatedText']

                # print('-'*50)
                # print(get_cell_text(source_cell_dict['object']))
                # print(gcp_translated_text)

                chatgpt_result = repeat_sentece(gcp_translated_text)
                chatgpt_repeated_text = chatgpt_result['result']

                sub_price = float(calculate_per_k_cost(gcp_translated_text, chatgpt_result['price']))

                total_price += sub_price

                if edit_cell_content(doc, target_cell_dict['index'], chatgpt_repeated_text):
                    # print("Cell content modified successfully.")
                    pass
                else:
                    print("ERROR: Failed to modify cell content.")

        doc.save(doc_path)
        print(f"""INFO: Translation finished with {doc_path}""")

    print(f"""INFO: total price in USD: {total_price}""")



