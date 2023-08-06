def extract_between(init_str: str, left: str, right: str, left_adjust: int=0, right_adjust: int=0) -> str:
    left_pos = init_str.find(left) if left is not None else 0
    right_pos = init_str.find(right) if right is not None else len(init_str)
    return init_str[left_pos + left_adjust : right_pos + right_adjust]

def word_count(text: str) -> int:
    return len(text.split(" "))

def line_count(text: str) -> int:
    return len(text.split("\n"))