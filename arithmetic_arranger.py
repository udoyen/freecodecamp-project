def problems_number_limit_check(my_list: list) -> bool:
    """problems_number_limit_check.

    :param my_list:
    :type my_list: list
    :rtype: bool
    """
    if len(my_list) > 5:
        raise Exception('Error: Too many problems')
    return True


def operator_check(my_list: list) -> bool:
    """operator_check.

    :param my_list:
    :type my_list: list
    :rtype: bool
    """
    for i in my_list:
        if '*' in i:
            raise Exception("Error: Operator must be '+' or '-'")
        if '/' in i:
            raise Exception("Error: Operator must be '+' or '-'")
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
                            raise Exception(
                                'Error: Numbers cannot be more than four digits')
                back_operand = i[i.index('+'):]
                for j in back_operand:
                    if j.isdigit():
                        back_operand_count += 1
                        if back_operand_count > 4:
                            raise ValueError(
                                'Error: Numbers cannot be more than four digits')
            except ValueError as e:
                print(f"Error: 3 Empty list found {e}")
        else:
            try:
                front_operand = i[0:i.index('-') + 1]
                for k in front_operand:
                    if k.isdigit():
                        front_operand_count += 1
                        if front_operand_count > 4:
                            raise Exception(
                                'Error: Numbers cannot be more than four digits')
                back_operand = i[i.index('-'):]
                back_operand = i[i.index('-'):]
                for j in back_operand:
                    if j.isdigit():
                        back_operand_count += 1
                        if back_operand_count > 4:
                            raise ValueError(
                                'Error: Numbers cannot be more than four digits')
            except ValueError as e:
                print(f"Error: 2 Empty list found {e}")
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
                raise TypeError('Error: Numbers must only contain digits')
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
    else:
        return front_operand - back_operand


def extract_digits_helper(item: str) -> list:
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


def extract_digits(ls: list, sanity_checker_func: callable) -> list:
    """extract_digits.

    :param ls:
    :type ls: list
    :param sanity_checker_func:
    :type sanity_checker_func: callable
    :rtype: list
    """
    problem_solutions = []
    if sanity_checker_func(ls):
        for i in ls:
            try:
                problem_solutions.append(tuple(extract_digits_helper(i)))
            except ValueError as e:
                print(f"Error: 1 Empty list found {e}")
    return problem_solutions


def calculate_line(result: dict, master_key: int, front_operand_key: int, back_operand_key: int) -> str:
    """calculate_line.

    :param result:
    :type result: dict
    :param master_key:
    :type master_key: int
    :param front_operand_key:
    :type front_operand_key: int
    :param back_operand_key:
    :type back_operand_key: int
    :rtype: str
    """
    if result.get(master_key):
        try:
            if len(str(result[master_key][front_operand_key])) > len(str(result[master_key][back_operand_key])):
                multiplier = len(
                    str(result[master_key][front_operand_key])) + 2
                return "-"*multiplier
            else:
                multiplier = len(str(result[master_key][back_operand_key])) + 2
                return "-"*multiplier
        except TypeError as e:
            print(f"Error: calculate line error {e}")
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
    else:
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
    else:
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
        else:
            return str(result[master_key][operator_key]) + ' ' + str(result[master_key][back_operand_key])
    else:
        return ' '


def display_solutions_with_results(solutions: list) -> None:
    """display_solutions_with_results.

    :param solutions:
    :type solutions: list
    :rtype: None
    """
    results = {}
    checker = len(solutions)
    for i, value in enumerate(solutions):
        results[i] = {1: value[0], 2: value[1], 3: value[2], 4: value[3]}

    print("{:>6}    {:>6}    {:>6}    {:>6}    {:>6}".format(f'{set_front_operand(results, 0, 1)}', f'{set_front_operand(results, 1, 1)}',
                                                             f'{set_front_operand(results, 2, 1)}', f'{set_front_operand(results, 3, 1)}', f'{set_front_operand(results, 4, 1)}'))
    print("{:>6}    {:>6}    {:>6}    {:>6}    {:>6}".format(f"{set_operator_line(results, 0, 1, 2, 4)}", f"{set_operator_line(results, 1, 1, 2, 4)}",
                                                    f"{set_operator_line(results, 2, 1, 2, 4)}", f"{set_operator_line(results, 3, 1, 2, 4)}",
                                                    f"{set_operator_line(results, 4, 1, 2, 4)}"))
    print("{:>6}    {:>6}    {:>6}    {:>6}    {:>6}".format(f"{calculate_line(results, 0, 1, 2)}", f"{calculate_line(results, 1, 1, 2)}",
                                                            f"{calculate_line(results, 2, 1, 2)}", f"{calculate_line(results, 3, 1, 2)}", f"{calculate_line(results, 4, 1, 2)}"))
    print("{:>6}    {:>6}    {:>6}    {:>6}    {:>6}".format(f'{set_result(results, 0, 3)}', f'{set_result(results, 1, 3)}',
                                                             f'{set_result(results, 2, 3)}', f'{set_result(results, 3, 3)}', f'{set_result(results, 4, 3)}'))


def display_solutions_without_results(solutions: list) -> None:
    """display_solutions_without_results.

    :param solutions:
    :type solutions: list
    :rtype: None
    """
    results = {}
    for i, value in enumerate(solutions):
        results[i] = {1: value[0], 2: value[1], 3: value[2], 4: value[3]}
    print("{:>6}    {:>6}    {:>6}    {:>6}    {:>6}".format(f'{set_front_operand(results, 0, 1)}', f'{set_front_operand(results, 1, 1)}',
                                                             f'{set_front_operand(results, 2, 1)}', f'{set_front_operand(results, 3, 1)}', f'{set_front_operand(results, 4, 1)}'))
    print("{:>6}    {:>6}    {:>6}    {:>6}    {:>6}".format(f"{set_operator_line(results, 0, 1, 2, 4)}", f"{set_operator_line(results, 1, 1, 2, 4)}",
                                                    f"{set_operator_line(results, 2, 1, 2, 4)}", f"{set_operator_line(results, 3, 1, 2, 4)}",
                                                    f"{set_operator_line(results, 4, 1, 2, 4)}"))
    print("{:>6}    {:>6}    {:>6}    {:>6}    {:>6}".format(f"{calculate_line(results, 0, 1, 2)}", f"{calculate_line(results, 1, 1, 2)}",
                                                            f"{calculate_line(results, 2, 1, 2)}", f"{calculate_line(results, 3, 1, 2)}", f"{calculate_line(results, 4, 1, 2)}"))

def arithmetic_arranger(my_list: list, result: bool = False) -> None:
    """arithmetic_arranger.

    :param my_list:
    :type my_list: list
    :rtype: None
    """
    results = extract_digits(my_list, sanity_check)
    try:
        if result:
            display_solutions_with_results(results)
        else:
            display_solutions_without_results(results)
    except TypeError as e:
        print(f"Error: arithmetic arranger error {e}")
