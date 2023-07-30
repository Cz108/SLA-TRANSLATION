def find_key_containing_val(key_list, keyword):
    for key in key_list:
        if keyword in key:
            return key
    return None

def word_count(text):
    words = text.split()
    return len(words)