def validate_parenthesis(string):
    result = False
    string_list = list(string)

    n_brackets1 = 0  # {}
    n_brackets2 = 0  # []
    n_brackets3 = 0  # ()

    stack_length = len(string_list)

    if stack_length > 0:
        first_element = string_list[0]

        if first_element == '}' or first_element == ')' or first_element == ']':
            result = False

        else:
            while stack_length > 0:
                element = string_list.pop(0)

                if stack_length == 1:
                    next_element = element
                else:
                    next_element = string_list[0]

                if element == '{':
                    n_brackets1 += 1
                    if stack_length != 1:
                        if next_element == ')' or next_element == ']':
                            result = False
                            break
                elif element == '}':
                    n_brackets1 -= 1

                if element == '[':
                    n_brackets2 += 1
                    if stack_length != 1:
                        if next_element == ')' or next_element == '}':
                            result = False
                            break
                elif element == ']':
                    n_brackets2 -= 1

                if element == '(':
                    n_brackets3 += 1
                    if stack_length != 1:
                        if next_element == '}' or next_element == ']':
                            result = False
                            break
                elif element == ')':
                    n_brackets3 -= 1

                stack_length -= 1

            if 0 == n_brackets1 == n_brackets2 == n_brackets3:
                result = True
    else:
        result = 'Empty'

    print(result)


string = '{(ab)[a]}'
string2 = '{{[[(())]]}}'
string_error = '])}['
string_error2 = '{](ab)[a]}'
string_error3 = '{[(])}'

validate_parenthesis(string)
validate_parenthesis(string2)
validate_parenthesis(string_error)
validate_parenthesis(string_error2)
validate_parenthesis(string_error3)
