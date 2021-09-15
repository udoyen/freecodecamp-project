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


def calculate_the_result(front_operand: int, back_operand: int, operator: str) -> int:
    """calculate_the_result.

    :param front_operand:
    :type front_operand: int
    :param back_operand:
    :type back_operand: int
    :param operator:
    :type operator: str
    :rtype: int
    """
    if operator == '+':
        return front_operand + back_operand
    return front_operand - back_operand


def extract_digits_helper(item: str) -> list:
    """extract_digits_helper.

    :param item:
    :type item: str
    :rtype: list
    """
    result = []
    if '+' in item:
        front_operand = item[0:item.index('+') + 1]
        back_operand = item[item.index('+'):]
        for j in front_operand:
            if not j.isdigit():
                result.append(int(front_operand[0:front_operand.index(j)]))
                break
        for k in back_operand:
            if k.isdigit():
                result.append(int(back_operand[back_operand.index(k):]))
                break
        # get the final value and
        # create a tuple from the result list
        result.append(calculate_the_result(result[0], result[1], '+'))
        # add the operator to the result list
        result.append('+')

    else:
        front_operand = item[0:item.index('-') + 1]
        back_operand = item[item.index('-'):]
        for j in front_operand:
            if not j.isdigit():
                result.append(int(front_operand[0:front_operand.index(j)]))
                break
        for k in back_operand:
            if k.isdigit():
                result.append(int(back_operand[back_operand.index(k):]))
                break
        # get the final value and
        # create a tuple from the result list
        result.append(calculate_the_result(result[0], result[1], '-'))
        # add the operator to the result list
        result.append('-')
    return result


def extract_digits(my_ls: list):
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


def set_front_operand(result: dict, master_key: int, child_key: int) -> any:
    """set_front_operand.

    :param result:
    :type result: dict
    :param master_key:
    :type master_key: int
    :param child_key:
    :type child_key: int
    :rtype: any
    """
    if result.get(master_key):
        return result[master_key][child_key]
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
        return result[master_key][child_key]
    return ' '


def set_operator_line(result: dict, master_key: int, front_operand_key, back_operand_key: int, operator_key: int) -> str:
    """set_operator_line.

    :param result:
    :type result: dict
    :param master_key:
    :type master_key: int
    :param front_operand_key:
    :param back_operand_key:
    :type back_operand_key: int
    :param operator_key:
    :type operator_key: int
    :rtype: str
    """
    space_multiplier_numbers = {0: 1, 1: 2, 2: 3, 3: 4}
    if result.get(master_key):
        f_key = len(str(result[master_key][front_operand_key]))
        b_key = len(str(result[master_key][back_operand_key]))
        if f_key > b_key:
            multiplier = f_key - b_key
            return str(result[master_key][operator_key]) + ' '*space_multiplier_numbers[multiplier] + str(result[master_key][back_operand_key])
        return str(result[master_key][operator_key]) + ' ' + str(result[master_key][back_operand_key])
    return ' '


def display_solutions_with_results(solutions: list) -> None:
    """display_solutions_with_results.

    :param solutions:
    :type solutions: list
    :rtype: None
    """
    results = {}
    for i, value in enumerate(solutions):
        results[i] = {1: value[0], 2: value[1], 3: value[2], 4: value[3]}

    statements = [
        f"{set_front_operand(results, 0, 1):>5}", f"{set_front_operand(results, 1, 1):>6}", f"{set_front_operand(results, 2, 1):>6}", f"{set_front_operand(results, 3, 1):>6}", f"{set_front_operand(results, 4, 1):>6}",
        f"{set_operator_line(results, 0, 1, 2, 4):>5}", f"{set_operator_line(results, 1, 1, 2, 4):>6}", f"{set_operator_line(results, 2, 1, 2, 4):>6}", f"{set_operator_line(results, 3, 1, 2, 4):>6}", f"{set_operator_line(results, 4, 1, 2, 4):>6}",
        f"{calculate_line(results, 0, 1, 2):>5}", f"{calculate_line(results, 1, 1, 2):>6}", f"{calculate_line(results, 2, 1, 2):>6}", f"{calculate_line(results, 3, 1, 2):>6}", f"{calculate_line(results, 4, 1, 2):>6}",
        f"{set_result(results, 0, 3):>5}", f"{set_result(results, 1, 3):>6}", f"{set_result(results, 2, 3):>6}", f"{set_result(results, 3, 3):>6}", f"{set_result(results, 4, 3):>6}",
                ]
    _assist = {
        0: [ 0, 5],
        1: [ 5, 10],
        2: [ 10, 15],
        3: [ 15, 20]

    }

    send = ""

    for i in range(0, 4):
        send +=  "    ".join(statements[_assist[i][0]:_assist[i][1]]) + "\n" if i != 3 else ''
    return send


def display_solutions_without_results(solutions: list) -> None:
    """display_solutions_without_results.

    :param solutions:
    :type solutions: list
    :rtype: None
    """
    results = {}
    for i, value in enumerate(solutions):
        results[i] = {1: value[0], 2: value[1], 3: value[2], 4: value[3]}

    statements = [
        f"{set_front_operand(results, 0, 1):>6}", f"{set_front_operand(results, 1, 1):>6}", f"{set_front_operand(results, 2, 1):>6}", f"{set_front_operand(results, 3, 1):>6}", f"{set_front_operand(results, 4, 1):>6}",
        f"{set_operator_line(results, 0, 1, 2, 4):>6}".strip(), f"{set_operator_line(results, 1, 1, 2, 4):>6}", f"{set_operator_line(results, 2, 1, 2, 4):>6}", f"{set_operator_line(results, 3, 1, 2, 4):>6}", f"{set_operator_line(results, 4, 1, 2, 4):>6}",
        f"{calculate_line(results, 0, 1, 2):>6}".strip(), f"{calculate_line(results, 1, 1, 2):>6}", f"{calculate_line(results, 2, 1, 2):>6}", f"{calculate_line(results, 3, 1, 2):>6}", f"{calculate_line(results, 4, 1, 2):>6}",
                ]
    _assist = {
        0: [ 0, 5],
        1: [ 5, 10],
        2: [ 10, 15],

    }

    send = ""

    for i in range(0, 3):
        send +=  "    ".join(statements[_assist[i][0]:_assist[i][1]]) + "\n" if i != 3 else ''
    return send



def arithmetic_arranger(my_list: list, result: bool = False) -> any:
    """arithmetic_arranger.

    :param my_list:
    :type my_list: list
    :rtype: any
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
