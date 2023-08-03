import zipfile
from lxml import etree

def extract_text_from_content_control(content_control):
    text_elements = content_control.xpath('.//w:t', namespaces=content_control.nsmap)
    text = ''.join(element.text for element in text_elements)
    return text

def get_content_control_type(content_control):
    if content_control.find('.//w:sdtPr/w:text', namespaces=content_control.nsmap) is not None:
        return 'Plain Text Content Control'
    elif content_control.find('.//w:sdtPr/w:richText', namespaces=content_control.nsmap) is not None:
        return 'Rich Text Content Control'
    elif content_control.find('.//w:sdtPr/w:pict', namespaces=content_control.nsmap) is not None:
        return 'Picture Content Control'
    elif content_control.find('.//w:sdtPr/w:comboBox', namespaces=content_control.nsmap) is not None:
        return 'ComboBox Content Control'
    elif content_control.find('.//w:sdtPr/w:dropDownList', namespaces=content_control.nsmap) is not None:
        return 'DropDown Content Control'
    else:
        return 'Unknown Content Control Type'

def iterate_content_controls(docx_file_path):
    with zipfile.ZipFile(docx_file_path) as zip_file:
        with zip_file.open('word/document.xml') as xml_file:
            xml_content = xml_file.read()

    xml_tree = etree.fromstring(xml_content)

    nsmap = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }

    for content_control in xml_tree.findall('.//w:sdt', namespaces=nsmap):
        text = extract_text_from_content_control(content_control)
        # control_type = get_content_control_type(content_control)
        print(f"{text}")

# Replace "your_docx_file.docx" with the actual path to your Word document
docx_file_path = "/Users/bilibala/Study/SLA-TRANS/documents/duizhao.docx"
iterate_content_controls(docx_file_path)
