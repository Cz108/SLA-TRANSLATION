# Test only
import os
from tools import snippets as tool

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/bilibala/Study/SLA-TRANS/cre/sla.json"


"""
Language detect code snippet
"""
# print(tool.detect_language("你好吗？"))
# print(tool.detect_language("Dzien dobry？"))
# print(tool.detect_language("это за день на това?"))

"""
Language code printout
"""
# print(tool.list_languages())

# tool.list_languages()
value = tool.translate_text('bs','Get Advertisement Linkage Records')
print(value['translatedText'])
