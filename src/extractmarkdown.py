import re



def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def extract_title(text):
    m = re.search(r"^# (.+)", text)
    return m.group(1).strip() if m else None
