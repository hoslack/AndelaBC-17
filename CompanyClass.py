class Company(object):
    def __init__(self, name, company_type=0, number_of_staff=0, annual_income=0):
        self.name = name
        self.company_type = company_type
        self.number_of_staff = number_of_staff
        self._annual_income = annual_income

    def layoff_staff(self, number_to_sack):
        pass

    def hire_staff(self, number_to_hire):
        pass

    def change_income(self, change):
        pass


class PrivateCompany(Company):
    def __init__(self, *args, **kwargs):
        super(PrivateCompany, self).__init__(*args, **kwargs)

    def layoff_staff(self, number_to_sack):
        if self.number_of_staff <= 0:
            return "You don't have people to fire"
        else:
            number_of_staff = self.number_of_staff - number_to_sack
            return number_of_staff

    def hire_staff(self, number_to_hire):
        number_of_staff = self.number_of_staff + number_to_hire
        return number_of_staff

    def change_income(self, change):
        annual_income = self._annual_income + change
        return annual_income


class PublicCompany(Company):
    def __init__(self, *args, **kwargs):
        super(PublicCompany, self).__init__(*args, **kwargs)

    def layoff_staff(self, number_to_sack):
        court_consent = input("What does the court say? 1=yes")
        if self.number_of_staff <= 0:
            return "You don't have people to fire"
        elif court_consent == 1:
            number_of_staff = self.number_of_staff - number_to_sack
            return number_of_staff
        else:
            return "You are not allowed to sack"

    def hire_staff(self, number_to_hire):
        number_of_staff = self.number_of_staff + number_to_hire
        return number_of_staff

    def change_income(self, change):
        annual_income = self._annual_income + change
        return annual_income
