import re

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

def katex_block_linebreaks(text : str) -> str:
    '''
    This function adds a line break before and after every KaTeX block.
    '''

    before_pattern = r'(?!\n)(\$\$.*?\$\$)'
    after_pattern = r'(\$\$.*?\$\$)(?!\n)'
    return re.sub(before_pattern, r'\n\1\n', re.sub(after_pattern, r'\n\1\n', text))


def on_pre_page_macros(env):
    '''
    This function is called before the page macros are processed.
    '''
    text = compatible_admonition(env.markdown)
    
    text = katex_block_linebreaks(text)

    # * ADD YOUR PREPROCESSING HERE
    # Use https://regexr.com/ to understand the regex patterns

    env.markdown = text
