from shutil import get_terminal_size
import textwrap

def important_message(message: str) -> str:
    width = get_terminal_size().columns - 1
    top = '#' + '=' * (width - 2) + '#'
    bottom = top
    empty_space = '#' + ' ' * (width - 2) + '#'
    wrapped_message = textwrap.fill(message, width - 6)  
    message_lines = ['#  ' + line.center(width - 6) + '  #' for line in wrapped_message.splitlines()]
    message = '\n'.join(message_lines)
    
    result = f"{top}\n{empty_space}\n{message}\n{empty_space}\n{bottom}"
    return result
