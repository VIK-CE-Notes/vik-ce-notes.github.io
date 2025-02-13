import re
from mkdocs_macros.plugin import MacrosPlugin
from unidecode import unidecode

def define_env(env):
    pass

def _add_quotes(text : str) -> str:
    if not text:
        return ''
    
    # in case the text is already quoted
    text = text.strip().removeprefix('"').removesuffix('"').strip()
    return f'"{text}"'

def compatible_admonition(text : str) -> str:
    '''
    Cause Markdown Preview Enhanced parses the admonition
    titles without the quotes, this function adds them.
    '''

    pattern = r'(!!!|\?\?\?\+?)\s*(note|abstract|info|tip|success|question|warning|faliure|danger|bug|example|quote)[^\S\r\n](.*)?'
    return re.sub(pattern, lambda m: f'{m.group(1)} {m.group(2)} {_add_quotes(m.group(3))}', text, flags=re.IGNORECASE)

def remove_url_accents(text : str) -> str:
    '''
    Cause the headings get the id without the accents
    '''

    pattern = r'\[(.*)\]\((.*)\)'
    return re.sub(pattern, lambda m: f'[{m.group(1)}]({unidecode(m.group(2))})', text)


def on_pre_page_macros(env : MacrosPlugin):
    '''
    This function is called before the page macros are processed.
    '''
    text = compatible_admonition(env.markdown)
    text = remove_url_accents(text)
    
    # * ADD YOUR PREPROCESSING HERE
    # Use https://regexr.com/ to understand the regex patterns

    env.markdown = text
