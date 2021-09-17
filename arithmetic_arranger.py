def problems_number_limit_check(my_list: list) -> bool:
    """problems_number_limit_check.

    :param my_list:
    :type my_list: list
    :rtype: bool
    """
    if len(my_list) > 5:
        return False
    return True


def operator_check(my_list: list) -> bool:
    """operator_check.

    :param my_list:
    :type my_list: list
    :rtype: bool
    """
    for i in my_list:
        if '*' in i:
            return False
        if '/' in i:
            return False
    return True


def four_digits_check(my_list: list) -> bool:
    """four_digits_check.

    :param my_list:
    :type my_list: list
    :rtype: bool
    """
    for i in my_list:
        back_operand_count = 0
        front_operand_count = 0
        if '+' in i:
            try:
                front_operand = i[0:i.index('+') + 1]
                for k in front_operand:
                    if k.isdigit():
                        front_operand_count += 1
                        if front_operand_count > 4:
                            return False
                back_operand = i[i.index('+'):]
                for j in back_operand:
                    if j.isdigit():
                        back_operand_count += 1
                        if back_operand_count > 4:
                            return False
            except ValueError as e_err:
                print(f"Error: 3 Empty list found {e_err}")
        else:
            try:
                front_operand = i[0:i.index('-') + 1]
                for k in front_operand:
                    if k.isdigit():
                        front_operand_count += 1
                        if front_operand_count > 4:
                            return False
                back_operand = i[i.index('-'):]
                back_operand = i[i.index('-'):]
                for j in back_operand:
                    if j.isdigit():
                        back_operand_count += 1
                        if back_operand_count > 4:
                            return False
            except ValueError as e_err:
                print(f"Error: 2 Empty list found {e_err}")
    return True


def digits_check(my_list: list) -> bool:
    """digits_check.

    :param my_list:
    :type my_list: list
    :rtype: bool
    """
    for i in my_list:
        for j in i:
            if j.isalpha():
                return False
    return True


def sanity_check(my_list: list) -> bool:
    """sanity_check.

    :param my_list:
    :type my_list: list
    :rtype: bool
    """
    if problems_number_limit_check(my_list):
        if operator_check(my_list):
            if four_digits_check(my_list):
                if digits_check(my_list):
                    return True
    return False


def calculate_the_result(front_operand: int, back_operand: int, operator: str) -> str:
    """calculate_the_result.

    :param front_operand:
    :type front_operand: int
    :param back_operand:
    :type back_operand: int
    :param operator:
    :type operator: str
    :rtype: str
    """
    if operator == '+':
        return str(front_operand + back_operand)
    return str(front_operand - back_operand)


def extract_digits_helper(item: str) -> list:
    """extract_digits_helper.

    :param item:
    :type item: str
    :rtype: list
    """
    result = []
    if '+' in item:
        front_operand = item.split()[0]
        result.append(front_operand)

        back_operand = item.split()[2]
        result.append(back_operand)

        operator = item.split()[1]

        # create a tuple from the result list
        result.append(calculate_the_result(int(front_operand), int(back_operand), operator))
        # add the operator to the result list
        result.append(operator)

    else:
        front_operand = item.split()[0]
        result.append(front_operand)

        back_operand = item.split()[2]
        result.append(back_operand)

        operator = item.split()[1]

        # create a tuple from the result list
        result.append(calculate_the_result(int(front_operand), int(back_operand), operator))
        # add the operator to the result list
        result.append(operator)
    return result


def extract_digits(my_ls: list) -> list:
    """
    Used to extract the problem digits
    and create a list of tuples
    :param my_ls:
    :return: list
    """
    problem_solutions = []

    for i in my_ls:
        try:
            problem_solutions.append(tuple(extract_digits_helper(i)))
        except ValueError as e_err:
            print(f"Error: 1 Empty list found {e_err}")
    return problem_solutions


def calculate_line(result: dict, master_key: int, front_operand_key: int, back_operand_key: int) -> any:
    """calculate_line.

    :param result:
    :type result: dict
    :param master_key:
    :type master_key: int
    :param front_operand_key:
    :type front_operand_key: int
    :param back_operand_key:
    :type back_operand_key: int
    :rtype: any
    """
    if result.get(master_key):
        try:
            if len(str(result[master_key][front_operand_key])) > len(str(result[master_key][back_operand_key])):
                multiplier = len(
                    str(result[master_key][front_operand_key])) + 2
                return "-"*multiplier
            multiplier = len(str(result[master_key][back_operand_key])) + 2
            return "-"*multiplier
        except TypeError as e_err:
            print(f"Error: calculate line error {e_err}")
    else:
        return " "


def set_front_operand_helper(result: dict, master_key: int) -> str:
    """
    Returns the left operand value with
    the right space padding added
    :param result:
    :type result: dict
    :param master_key:
    :type master_key: int
    :return: str
    """
    right_to_left_operand_mapping = {
        4: {4: 2, 3: 3, 2: 4, 1: 5},
        3: {3: 1, 2: 3, 1: 4},
        2: {1: 3, 2: 1},
        1: {1: 2}
    }
    # check which is the bigger of the two operands
    # print(f"Master key 1: {len(str(result[master_key][1]))}")
    if len(str(result[master_key][1])) >= len(str(result[master_key][2])):
        # return the space padded string
        return '''{0:>{1}}'''.format(result[master_key][1], len(str(result[master_key][1])) + 2)
    else:
        padding = right_to_left_operand_mapping[len(str(result[master_key][2]))][len(str(result[master_key][1]))]
        return '''{0:>{1}}'''.format(result[master_key][1], padding + len(str(result[master_key][1])))


def set_front_operand(result: dict, master_key: int) -> any:
    """set_front_operand.

    :param result:
    :type result: dict
    :param master_key:
    :type master_key: int
    :rtype: any
    """
    if result.get(master_key):
        return set_front_operand_helper(result, master_key)
    return ' '


def set_result(result: dict, master_key: int, child_key: int) -> any:
    """set_result.

    :param result:
    :type result: dict
    :param master_key:
    :type master_key: int
    :param child_key:
    :type child_key: int
    :rtype: any
    """
    if result.get(master_key):
        padding = max(len(str(result[master_key][1])), len(str(result[master_key][2])))
        return '''{0:>{1}}'''.format(result[master_key][child_key], padding + 2)
    return ' '


def set_back_operand_helper(result: dict, master_key: int) -> str:
    """
    Helper function to set_back_operand function
    :param result:
    :type result: dict
    :param master_key:
    :type master_key: int
    :return: str
    """
    left_to_right_operand_mapping = {
        4: {4: 1, 3: 2, 2: 3, 1: 4},
        3: {3: 1, 2: 2, 1: 3},
        2: {2: 1, 1: 2},
        1: {1: 1}
    }

    # check which is the bigger of the two operands
    print(f"Master key 1: {len(str(result[master_key][2]))}")
    if len(str(result[master_key][2])) >= len(str(result[master_key][1])):
        # return the space padded string
        return '''{0:>{1}}'''.format(result[master_key][2], len(str(result[master_key][2])) + 1)
    else:
        padding = left_to_right_operand_mapping[len(str(result[master_key][1]))][len(str(result[master_key][2]))]
        # print(f"Padding: {padding}")
        return '''{0:>{1}}'''.format(result[master_key][2], padding + len(str(result[master_key][2])))


def set_operator_line(result: dict, master_key: int) -> str:
    """set_operator_line.

    :param result:
    :type result: dict
    :param master_key:
    :type master_key: int
    :rtype: str
    """
    if result.get(master_key):
        r_operand = set_back_operand_helper(result, master_key)
        operator = result[master_key][4]
        return str(operator) + str(r_operand)
    return ' '


def display_solutions_with_results(solutions: list) -> str:
    """display_solutions_with_results.

    :param solutions:
    :type solutions: list
    :rtype: str
    """
    results = {}
    for i, value in enumerate(solutions):
        results[i] = {1: value[0], 2: value[1], 3: value[2], 4: value[3]}
    statements = [
        f"{set_front_operand(results, 0)}", f"{set_front_operand(results, 1)}", f"{set_front_operand(results, 2)}", f"{set_front_operand(results, 3)}", f"{set_front_operand(results, 4)}",
        f"{set_operator_line(results, 0)}", f"{set_operator_line(results, 1)}", f"{set_operator_line(results, 2)}", f"{set_operator_line(results, 3)}", f"{set_operator_line(results, 4)}",
        f"{calculate_line(results, 0, 1, 2):>}", f"{calculate_line(results, 1, 1, 2):>}", f"{calculate_line(results, 2, 1, 2):>}", f"{calculate_line(results, 3, 1, 2):>}", f"{calculate_line(results, 4, 1, 2):>}",
        f"{set_result(results, 0, 3):>}", f"{set_result(results, 1, 3):>}", f"{set_result(results, 2, 3):>}", f"{set_result(results, 3, 3):>}", f"{set_result(results, 4, 3):>}",
                ]

    _assist = {
        0: [0,  len(solutions)],
        1: [5,  5 + len(solutions)],
        2: [10, 10 + len(solutions)],
        3: [15, 15 + len(solutions)]

    }

    send = ""

    for k in _assist:
        # print("In assist")
        statements_slice = statements[_assist[k][0]:_assist[k][1]]
        # print(f"Statements: {statements_slice}")
        if [*_assist.keys()][-1] != k:
            send += "    ".join(statements_slice)
            send += "\n"
        else:
            send += "    ".join(statements_slice)

    return send


def display_solutions_without_results(solutions: list) -> str:
    """display_solutions_without_results.

    :param solutions:
    :type solutions: list
    :rtype: str
    """
    results = {}
    for i, value in enumerate(solutions):
        results[i] = {1: value[0], 2: value[1], 3: value[2], 4: value[3]}
    statements = [
        f"{set_front_operand(results, 0)}", f"{set_front_operand(results, 1)}", f"{set_front_operand(results, 2)}", f"{set_front_operand(results, 3)}", f"{set_front_operand(results, 4)}",
        f"{set_operator_line(results, 0)}", f"{set_operator_line(results, 1)}", f"{set_operator_line(results, 2)}", f"{set_operator_line(results, 3)}", f"{set_operator_line(results, 4)}",
        f"{calculate_line(results, 0, 1, 2):>}", f"{calculate_line(results, 1, 1, 2):>}", f"{calculate_line(results, 2, 1, 2):>}", f"{calculate_line(results, 3, 1, 2):>}", f"{calculate_line(results, 4, 1, 2):>}",
                ]
    # print(f"Statements: {statements}")
    _assist = {
        0: [0, len(solutions)],
        1: [5, 5 + len(solutions)],
        2: [10, 10 + len(solutions)],

    }

    send = ""

    for k in _assist:
        statements_slice = statements[_assist[k][0]:_assist[k][1]]
        # print(f"Statements: {statements_slice}")
        if [*_assist.keys()][-1] != k: # only add newline character if not last key
            send += "    ".join(statements_slice)
            send += "\n"
        else:
            send += "    ".join(statements_slice)
    return send


def arithmetic_arranger(my_list: list, result: bool = False) -> any:
    """
    Main entry point for app
    :param my_list:
    :type my_list: list
    :param result:
    :type result: bool
    :return:
    """
    problem_count = problems_number_limit_check(my_list)
    operator_checker = operator_check(my_list)
    digit_checker = digits_check(my_list)
    digits_count_checker = four_digits_check(my_list)

    if problem_count:
        if operator_checker:
            if digit_checker:
                if digits_count_checker:
                    results = extract_digits(my_list)
                    try:
                        if result:
                            return display_solutions_with_results(results)
                        return display_solutions_without_results(results)
                    except TypeError as e_err:
                        print(f"Error: arithmetic arranger error {e_err}")
                else:
                    return 'Error: Numbers cannot be more than four digits.'
            else:
                return 'Error: Numbers must only contain digits.'
        else:
            return "Error: Operator must be '+' or '-'."
    else:
        return 'Error: Too many problems.'
