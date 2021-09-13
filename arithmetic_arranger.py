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
        if '+' in i:
            if i[0:i.index('+') + 1][4].isdigit():
                raise Exception('Error: Numbers cannot be more than four digits')
            back_operand = i[i.index('+'):]
            for j in back_operand:
                if j.isdigit():
                    back_operand_count += 1
                    if back_operand_count > 4:
                        raise ValueError('Error: Numbers cannot be more than four digits')
        else:
            if i[0:i.index('-') + 1][4].isdigit():
                raise Exception('Error: Numbers cannot be more than four digits')
            back_operand = i[i.index('-'):]
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
        if back_operand > front_operand:
            raise Exception('Error: First value must be greater then second value')
        return front_operand + back_operand
    else:
        if back_operand > front_operand:
            raise Exception("Error: First value must be greater than second value")
        return front_operand - back_operand

def extract_digits(ls: list, sanity_checker_func: callable):
    problem_solutions = []
    if sanity_checker_func(ls):
        for i in ls:
            result = []
            if '+' in i:
                front_operand = i[0:i.index('+') + 1]
                back_operand =  i[i.index('+'):]
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
                problem_solutions.append(tuple(result))
            else:
                front_operand = i[0:i.index('-') + 1]
                back_operand =  i[i.index('-'):]
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
                problem_solutions.append(tuple(result))
        print(problem_solutions)

def display_solutions_with_results():
    pass

def display_solutions_without_results():
    pass

def arithmetic_arranger(my_list: list, result: bool = False) -> None:
    """arithmetic_arranger.

    :param my_list:
    :type my_list: list
    :rtype: None
    """
    for i in my_list:
        print(i)
