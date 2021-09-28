class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        category_name = self.category
        current_ledger = self.ledger
        border_line_multiplier = int((30 - len(category_name)) / 2)
        intro_line = '*' * border_line_multiplier + category_name + '*' * border_line_multiplier

        ledger_list_items = '' + intro_line + "\n"
        for i in current_ledger:
            line = "{:<24}{:>.2f}".format(i["description"][0:23], i["amount"])
            ledger_list_items += line
            ledger_list_items += "\n"
        ledger_list_items += "Total: {:>.2f}".format(self.get_balance())
        return ledger_list_items

    def deposit(self, amount: int, description: str = ""):
        """
        method that accepts an amount and description.
        If no description is given, it should default
        to an empty string. The method should append
        an object to the ledger list in the form of
        `{"amount": amount, "description": description}`.

        :param amount:
        :param description:
        :return:
        :rtype: None
        """
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount: int, description: str = '') -> bool:
        """
        method that is similar to the `deposit` method,
        but the amount passed in should be stored in the
        ledger as a negative number. If there are not enough funds,
        nothing should be added to the ledger.
        This method should return `True` if the withdrawal took place,
        and `False` otherwise.

        :param amount:
        :param description:
        :return: False or True
        :rtype: bool
        """
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False

    def get_balance(self) -> int:
        """
        Method that returns the current
        balance of the budget category based
        on the deposits and withdrawals that
        have occurred.

        :return: Current balance
        :rtype: int
        """
        total = 0
        for i in self.ledger:
            total += i["amount"]
        return abs(total)

    def transfer(self, amount: int, budget_category: callable) -> bool:
        """
        method that accepts an amount and another budget category as arguments.
         The method should add a withdrawal with the amount and the description "Transfer to
         [Destination Budget Category]". The method should then add a deposit to the other budget
         category with the amount and the description "Transfer from [Source Budget Category]".
         If there are not enough funds, nothing should be added to either ledgers. This method should return `True`
         if the transfer took place, and `False` otherwise.

        :param amount:
        :param budget_category:
        :return: True or False
        :rtype: bool
        """

        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.ledger.append({"amount": amount, "description": f"Transfer from {self.category}"})
            return True
        return False

    def check_funds(self, amount: int) -> bool:
        """
        method that accepts an amount as an argument.
        It returns `False` if the amount is greater than
        the balance of the budget category and returns `True` otherwise.
         This method should be used by both the `withdraw`
         method and `transfer` method.
        :param amount:
        :return: True or False
        :rtype: bool
        """
        if amount > self.get_balance():
            return False
        return True


def split(word):
    """
    Helper function to
    split catergory words
    :param word:
    :type: str
    :return:
    :rtype: list
    """
    return [char for char in word]


def create_spend_chart(categories: list) -> str:
    """
    Function to create chart
    :param categories:
    :type: list
    :return:
    :rtype: str
    """
    cat_items = []
    total_percentage_spend = 0
    for i in categories:  # list of categories
        init_balance = 0
        balance = i.get_balance()
        for j in i.ledger:  # list of dicts
            if init_balance != 0:
                break
            for key in j:
                if init_balance != 0:
                    break
                if key == 'description':
                    init_balance = j['amount']
                    calculate_percentage = int(((init_balance - balance) * 100) / init_balance)
                    total_percentage_spend += calculate_percentage
                    cat_items.append({i.category: calculate_percentage})
                    break
    # Calculate the display percentage
    for k in cat_items:
        for key, value in k.items():
            k[key] = int(((value * 100) / total_percentage_spend)) - (
                        int(((value * 100) / total_percentage_spend)) % 10)
    # print(f"Items: {cat_items}")
    header = "Percentage spent by category" + "\n"
    display = ''
    display += header
    for i in range(100, -1, -10):
        display += f"{i:>3}| "
        for index, value in enumerate(cat_items):
            if index == 0:
                for j in value.values():
                    if j >= i:
                        display += f"o  "
                    else:
                        display += "   "
            else:
                for j in value.values():
                    if j >= i:
                        display += f"o  "
                    else:
                        display += f"   "

        display += "\n"
    display += "    " + "-" * 10 + "\n"
    # display += "     "
    total_letter_count = 0
    combined_keys_list = []
    for item in cat_items:
        for k in item.keys():
            total_letter_count += len(k)
            combined_keys_list.append(split(k))
    # print(total_letter_count, combined_keys_list)
    for c in range(0, total_letter_count):
        for index, m in enumerate(combined_keys_list):
            if index == 0:
                if len(m) != 0:
                    display += "     " + m.pop(0) + "  "
                else:
                    display += "        "
            else:
                if len(m) != 0:
                    display += m.pop(0) + "  "
                else:
                    display += "   "
        display += "\n"
    return display.rstrip() + "  "
