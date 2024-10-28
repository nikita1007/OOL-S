# Вариант 5
# Задача 1
# Создайте класс компания Company, содержащей сотрудников и реализующей методы:
# • найм одного сотрудника — hire(),
# • найм списка сотрудников – hireAll(),
# • увольнение сотрудника – fire(),
# • получение значения дохода компании – getIncome().
# Аргументы и возвращаемое значение методов выберите на основании логики работы вашего приложения.
# 
# Задание 2
# Создайте два метода, возвращающие список указанной длины (count). Они должны содержать сотрудников, отсортированных по убыванию и возрастанию заработной платы:
# •	List<Employee> getTopSalaryStaff(int count),
# •	List<Employee> getLowestSalaryStaff(int count).


from typing import Optional, Any


class Employee:
    def __init__(self, name: str = '', profit: int = 0) -> None:
        self.__name: str = self.__checkAttr(key="name", value=name)
        self.__profit: int = self.__checkAttr(key="profit", value=profit)

    def __checkAttr(self, key: str, value) -> Any:
        match key:
            case "name":
                if not isinstance(value, str):
                    raise TypeError("Атрибут `name` должен иметь тип str")
            case "profit":
                if not isinstance(value, int):
                    raise TypeError("Атрибут `profit` должен иметь тип int")
        
        return value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        # Проверка на тип передаваемого атрибута
        self.__checkAttr(key="name", value=value)

        self.__name = value

    @property
    def profit(self):
        return self.__profit

    @profit.setter
    def profit(self, value: int) -> None:
        # Проверка на тип передаваемого атрибута
        self.__checkAttr(key="profit", value=value)

        self.__profit = value
    
    def __repr__(self):
        return "{" + f"name: {self.__name}, profit: {self.__profit}" + "}"

class Company:
    def __init__(self) -> None:
        self.__employees: dict[int, Employee] = {}
        self.__profit: Optional[int] = None

    def __generateId(self) -> int:
        return max(self.__employees.keys()) + 1 if len(self.__employees) else 1

    def hire(self, name: str, profit: int) -> None:
        '''
        Метод для найма одного сотрудника
        :param name: Имя сотрудника
        :param profit: Прибыль, которую приносит сотрудник компании
        '''

        new_employee_id = self.__generateId()

        new_employee = Employee()
        new_employee.name = name
        new_employee.profit = profit

        self.__employees[new_employee_id] = new_employee

    def hireAll(self, employees: list[Employee]) -> None:
        ''' Метод для найма нескольких сотрудников
        :param employees: Список объектов новых сотрудников
        '''

        # Проверка на то, является ли атрибут `employees` типа list
        if not isinstance(employees, list):
            raise TypeError("Атрибут `employees` должен иметь тип list")

        for new_employee in employees:
            # Проверка каждого объекта списка принадлежности к классу Employee
            if not isinstance(new_employee, Employee):
                raise TypeError("Каждый объекта атрибута `employees` должен иметь тип Employee")

            new_employee_id = self.__generateId()

            self.__employees[new_employee_id] = new_employee

    def fire(self, id: int) -> None:
        ''' Метод по для сотрудника по его идентификатору
        :param id: Идентификатор сотрудника
        '''

        # Проверка на типа атрибута `id`
        if not isinstance(id, int):
            raise TypeError("Атрибут `id` должен иметь тип int")

        # Проверка на нахождения сотрудника с определенным `id` в компании
        if not id in self.__employees.keys():
            raise Exception(f"Работника с {id=} не найдено!")

        del self.__employees[id]

    def getIncome(self) -> int:
        return sum([employee.profit for employee in self.__employees.values()])

    @property
    def profit(self):
        return self.__profit

    @profit.getter
    def profit(self) -> int:
        return self.getIncome()

    def getTopSalaryStaff(self, count: int) -> list[tuple[int, Employee]]:
        ''' Возвращает список сотрудников с наивысшей зарплатой
        :param count: Количество сотрудников для возврата
        '''
        # Сортировка по возрастанию и возврат последних count
        sorted_employees = sorted(self.__employees.items(), key=lambda x: x[1].profit, reverse=True)
        return sorted_employees[:count]

    def getLowestSalaryStaff(self, count: int) -> list[tuple[int, Employee]]:
        ''' Возвращает список сотрудников с наименьшей зарплатой
        :param count: Количество сотрудников для возврата
        '''
        # Сортировка по возрастанию и возврат первых count
        sorted_employees = sorted(self.__employees.items(), key=lambda x: x[1].profit)
        return sorted_employees[:count]
    
    def __repr__(self):
        class_name = self.__class__.__name__
        employees = '\n'.join('id %s: %s' % (k, v) for k, v in self.__employees.items())
        return f"{class_name}\nСотрудники: \n{employees}\nПрибыль компании: {self.profit}"


# Задание 1

company = Company()

company.hireAll(employees=[Employee(name="Nikita", profit=100000), Employee(name="Vadim", profit=2000)])

company.hire(name='NoName', profit=0)
company.hire(name='Andrey', profit=20000)

print(company, '\n')

company.fire(id=3)
company.hire(name='Dima', profit=50000)

company.hireAll(employees=[Employee(name="Oleg", profit=1000)])

print(company)

# Задание 2

# Получение списка сотрудников с самой высокой зарплатой
print("Сотрудники с самой высокой зарплатой:", company.getTopSalaryStaff(2))

# Получение списка сотрудников с самой низкой зарплатой
print("Сотрудники с самой низкой зарплатой:", company.getLowestSalaryStaff(2))