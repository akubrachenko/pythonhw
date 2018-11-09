class Department(object):
    teams = []

class CreateEmployee(object):
    def __init__(self, first_name, second_name, experience, salary, manager=None):

        def set_salary(sal, exp):
            newsal = 0
            if exp >= 2 and exp < 5: newsal = sal + 200
            elif exp >= 5: newsal = sal + 500 * 1.5 # was sal*1.5+500
            return newsal
        
        self.first_name = first_name
        self.second_name = second_name
        self.manager = manager
        self.experience = experience
        self.salary = set_salary(salary,experience)
        self.subordinates = []
        
        self.add_to_subordinates()

    def add_to_subordinates(self):
        if self.manager:
            self.manager.subordinates.append(self)

class Managers(CreateEmployee):
    def __init__(self, first_name, second_name, experience, salary, manager=None):
        CreateEmployee.__init__(self, first_name, second_name, experience, salary, manager)
        Department.teams.append(self)

    def get_salary(self):
        qty_subordinates = len(self.subordinates)
        qty_of_dev = 0
        for team in self.subordinates:
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
dev = Developers("Vasya","Pupkin", 10, 2000, man)
dev2 = Developers("Petya","Petrov",7, 2500, man)
des = Designers("Mark","Markov", 2, 1500, man, 0.6)
dev1 = Developers("Stepan","Kazanin", 2, 1500, man)
dev2 = Developers("Evgen","Ostapenko", 2, 1500, man)
dev3 = Developers("Ivan","Grozniy", 2, 1500, man2)
des1 = Designers("Steve","Jobs", 2, 1500, man2, 0.6)
dev4 = Developers("Mark","Zuckerberg", 10, 5500, man2)
dev5 = Developers("Bill","Gates", 6, 2700, man2)

team = Department()
for man in team.teams:
    print(man.first_name,man.second_name,"has sallary -",man.get_salary())
    for empl in man.subordinates:
        print("    ",empl.first_name,empl.second_name,"has sallary -",empl.salary)