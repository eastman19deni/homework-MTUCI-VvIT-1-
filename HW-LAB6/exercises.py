class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def manage_project(self):
        return f"Manager {self.name} is managing a project in the {self.department} department."

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Technician {self.name} is performing maintenance in the field of {self.specialization}."

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        
        Employee.__init__(self, name, emp_id)  
        self.department = department  # Атрибут из Manager
        self.specialization = specialization  # Атрибут из Technician
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return "No team members."
        return "\n".join([emp.get_info() for emp in self.team])

# Создаем сотрудников разных типов
emp1 = Employee("Fasale", 1)
manager = Manager("Yan", 2, "Sales")
technician = Technician("Tim", 3, "Electrical")
tech_manager = TechManager("Ewan", 4, "IT", "software dev")

# Демонстрация функциональности каждого класса
print(emp1.get_info())  # Вывод базовой информации о сотруднике
print(manager.get_info())  # Информация о менеджере
print(manager.manage_project())  # Управление проектами

print(technician.get_info())  # Информация о технике
print(technician.perform_maintenance())  # Выполнение обслуживания

# TechManager может управлять проектами и выполнять технические задачи
print(tech_manager.get_info())  # Информация о TechManager
print(tech_manager.manage_project())  # Управление проектами
print(tech_manager.perform_maintenance())  # Выполнение обслуживания

# Добавляем сотрудников в команду TechManager
tech_manager.add_employee(emp1)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

# Получаем информацию о команде
print("Team Info:")
print(tech_manager.get_team_info())

# tsests