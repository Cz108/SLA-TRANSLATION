# Test only
import os
from tools import snippets as tool

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/bilibala/Study/SLA-TRANS/cre/sla.json"



print(tool.detect_language("你好吗？"))
print(tool.detect_language("Dzien dobry？"))
print(tool.detect_language("это за день на това?"))