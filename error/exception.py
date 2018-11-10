class SalaryGivingError(Exception):
    pass
class NotEmployeeException(Exception):
    pass
class WrongEmployeeRoleError(Exception):
    pass

class Department(object):
    def __init__(self, manager = None):
        self.teams = []
        self.manager = manager
        self.add_team()

    def add_team(self):
        if self.manager:
            self.teams.append(self.manager)

    def add_team_members(self, man, array):
        man.add_to_team(array)
        self.teams.append(man)

    def get_salary(self):
        for man in self.teams:
            try:
                if len(man.team) == 0:
                    raise SalaryGivingError(str(man.first_name)+" "+str(man.second_name)+" does't have team")    
            except SalaryGivingError as e:
                print(e)    
            else:
                print(man.first_name,man.second_name,"#salary: ",man.get_salary())
                for empl in man.team:
                    print("    ",empl.first_name,empl.second_name,", manager is - ",man.first_name,man.second_name,"#salary: ",empl.salary)

class CreateEmployee(object):
    def __init__(self, first_name, second_name, experience, salary, manager=None):

        def set_salary(sal, exp):
            newsal = 0
            if exp >= 2 and exp < 5: newsal = sal + 200
            elif exp >= 5: newsal = sal + 500 * 1.5
            return newsal
        
        self.first_name = first_name
        self.second_name = second_name
        self.manager = manager
        self.experience = experience
        self.salary = set_salary(salary,experience)

class Managers(CreateEmployee):
    def __init__(self, first_name, second_name, experience, salary, manager=None):
        CreateEmployee.__init__(self, first_name, second_name, experience, salary, manager)
        #Department.teams.append(self)
        self.team = []

    def add_to_team(self,subordinates):
        try:
            if len(subordinates) == 0:
                raise NotEmployeeException("There are no employee to add")
            for empl in subordinates:
                if isinstance(empl,Managers) == True:
                    raise WrongEmployeeRoleError("Employee "+str(empl.first_name)+" "+str(empl.second_name)+" has unexpected role!")
        except (NotEmployeeException,WrongEmployeeRoleError) as e:
            print(e)
        else:
            self.team = subordinates
    
    def get_salary(self):
        qty_subordinates = len(self.team)
        qty_of_dev = 0
        for subordinates in self.team:
            if isinstance(dev,Developers):
                qty_of_dev +=1
        if qty_subordinates > 5 and qty_subordinates < 10 and qty_of_dev > qty_subordinates / 2: self.salary = self.salary + 200 * 1.1
        elif qty_subordinates > 10 and qty_of_dev > qty_subordinates / 2: self.salary = self.salary + 300 * 1.1
        elif qty_of_dev > qty_subordinates / 2: self.salary = self.salary * 1.1
        return self.salary

class Developers(CreateEmployee):
    def __init__(self, first_name, second_name, experience, salary, manager=None):
        super(Developers, self).__init__(first_name, second_name, experience, salary, manager)
        self.manager = manager 

        
class Designers(CreateEmployee):
    def __init__(self, first_name, second_name, experience, salary, manager=None, cof=None):
        CreateEmployee.__init__(self, first_name, second_name, experience, salary, manager)
        self.cof = cof
        self.manager = manager
        self.set_salary()

    def set_salary(self):
        self.salary = self.salary * self.cof


man = Managers("Marina","Ivanova", 2, 3500)
man2 = Managers("Kirril","Petrov", 10, 4500)
man3 = Managers("Svyatoslav","Antipov", 10, 4500)
dev = Developers("Vasya","Pupkin", 10, 2000, man)
dev2 = Developers("Petya","Petrov",7, 2500, man)
des = Designers("Mark","Markov", 2, 1500, man, 0.6)
dev1 = Developers("Stepan","Kazanin", 2, 1500, man)
dev2 = Developers("Evgen","Ostapenko", 2, 1500, man)
dev3 = Developers("Ivan","Grozniy", 2, 1500, man2)
des1 = Designers("Steve","Jobs", 2, 1500, man2, 0.6)
dev4 = Developers("Mark","Zuckerberg", 10, 5500, man2)
dev5 = Developers("Bill","Gates", 6, 2700, man2)

man3.add_to_team([dev5])

dept = Department()
dept.add_team_members(man,[dev,dev2,des])
dept.add_team_members(man2,[dev3,dev4,des1])

dept.get_salary()
