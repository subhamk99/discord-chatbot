import re


def extract_query(text):
    # Define a regular expression pattern to match "$command rest-text" patterns
    pattern = r'\$(\w+)\s(.*)'

    # Use re.match to find the pattern in the text
    match = re.match(pattern, text)

    rest_text = text

    if match:
        rest_text = match.group(2)


    return rest_text
