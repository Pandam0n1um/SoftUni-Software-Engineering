from project.appliances.appliance import Appliance
from project.common.validators import Validator
from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name  = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        error_message = "Expenses cannot be negative"
        Validator.raise_if_value_negative(value, error_message)
        self.__expenses = value

    def calculate_expenses(self,*expenses_list):
        total_expenses=0
        for el in expenses_list:
            for expense in el:
                if expense.__class__.__name__=='Child':
                    total_expenses+=expense.cost*30
                else:
                    total_expenses+=expense.get_monthly_expense()
        self.expenses=total_expenses
    # def calculate_expenses(self, *args):
    #     total_expenses = 0
    #     for list_el in args:
    #         for el in list_el:
    #             # TODO implement get_monthly_expense in Child class
    #             if isinstance(el, Appliance):
    #                 total_expenses += el.get_monthly_expense()
    #             elif isinstance(el, Child):
    #                 total_expenses += el.cost * 30
    #     self.expenses = total_expenses