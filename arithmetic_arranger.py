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
    back_operand_count = 0
    for i in my_list:
        if i[0:i.index('+') + 1][4].isdigit():
            raise Exception('Error: Numbers cannot be more than four digits')
        back_operand = i[i.index('+'):]
        for j in back_operand:
            if j.isdigit():
                back_operand_count += 1
                if back_operand_count > 4:
                    raise ValueError('Error: Numbers cannot be more than four digits')
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

def extract_digits(ls: list, sanity_checker_func):
    if sanity_checker_func(ls):
        print("hello")

def calculate_solution(first_value: int, second_value: int) -> int:
    pass

def display_solutions_with_results():
    pass

def display_solutions_without_results():
    pass

def arithmetic_arranger(my_list: list, result=False) -> None:
    """arithmetic_arranger.

    :param my_list:
    :type my_list: list
    :rtype: None
    """
    for i in my_list:
        print(i)
