import re

text = "@Привет, как дела?@"
result = re.search(r'@(.+?)@', text)
if result:
    extracted_text = result.group(1)
    print(extracted_text)
