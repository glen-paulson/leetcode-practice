class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_stack = []
        for character in s:
            if character == '[' or character == '{' or character == '(':
                my_stack.append(character)
            elif character == ']' or character == '}' or character == ')':
                if not my_stack:
                    return False
                top_character = my_stack[-1]
                if (character == ']' and top_character != '[') or (character == '}' and top_character != '{') or (character == ')' and top_character != '('):
                    return False
                my_stack.pop()

        return not my_stack
