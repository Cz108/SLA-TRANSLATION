import os
import sys
from tools import snippets as tool
from docparser.excel_table_parser import load_workbook, get_cell_dict_in_selected_column, if_color_match_the_cell, get_cell_text
from docparser.excel_table_parser import check_table_colors, edit_cell_content

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/bilibala/Study/SLA-TRANS/cre/sla.json"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    target_language_code = 'bg'
    excel_path = '/Users/bilibala/Study/SLA-TRANS/documents/excel_test.xlsx'
    wb = load_workbook(excel_path)
    sheet = wb.active

    print("\nINFO: check_table_colors(wb)")
    table_colors = check_table_colors(sheet)

    for source_cell_dict, target_cell_dict in zip(get_cell_dict_in_selected_column(sheet, 0), get_cell_dict_in_selected_column(sheet, 2)):
        if if_color_match_the_cell(source_cell_dict['object'], "FFFFFF"):

            source_text = get_cell_text(source_cell_dict['object'])
            if source_text:
                translated_text = tool.translate_text(target_language_code, source_text)
                translated_text_value = translated_text['translatedText']
                print('-'*50)
                print(source_text)
                print(translated_text_value)
            else:
                translated_text_value = ""
                print('-' * 50)
                print("")
                print("")
            tmpv = target_cell_dict['index']
            print(tmpv)
            if edit_cell_content(sheet, target_cell_dict['index'], translated_text_value):
                print("Cell content modified successfully.")
            else:
                print("Failed to modify cell content.")

    wb.save('/Users/bilibala/Study/SLA-TRANS/documents/translated_excel_test.xlsx')


