from docx import Document
import sys

def load_document(file_path):
    return Document(file_path)

"""
Select column in the docx 
Replace with the column_index of the column you want (0-based index)
    for cell_text in selected_column:
        print("cell:")
        print(cell_text)
"""
def select_column(doc, column_index):
    selected_column = []

    for table in doc.tables:
        for row in table.rows:
            if len(row.cells) > column_index:
                cell = row.cells[column_index]
                selected_column.append(cell.text)

    return selected_column

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    doc = load_document('/Users/bilibala/Study/SLA-TRANS/documents/test1.docx')
    column_index_to_select = 2  # Replace with the index of the column you want (0-based index)

    selected_column = select_column(doc, column_index_to_select)

    for cell_text in selected_column:
        print("cell:")
        print(cell_text)
