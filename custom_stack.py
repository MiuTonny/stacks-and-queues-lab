def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        #if opening bracket, push to stack
        if char in pairs.values():
            stack.append(char)

        #if closing bracket, check stack
        elif char in pairs:
            if not stack:
                return False
            
            top = stack.pop()
            if top != pairs[char]:
                return False
            
    return not stack
