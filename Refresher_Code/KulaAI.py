import json

# Sample JSON data
data = '''
{
  "employees": [
    {
      "name": "John Doe",
      "age": 32,
      "department": "Engineering",
      "salary": 80000
    },
    {
      "name": "Jane Smith",
      "age": 27,
      "department": "Marketing",
      "salary": 65000
    },
    {
      "name": "Michael Johnson",
      "age": 45,
      "department": "Sales",
      "salary": 90000
    },
    {
      "name": "Emily Davis",
      "age": 29,
      "department": "Engineering",
      "salary": 75000
    },
    {
      "name": "David Wilson",
      "age": 38,
      "department": "Marketing",
      "salary": 72000
    },
    {
      "name": "Sarah Thompson",
      "age": 31,
      "department": "Sales",
      "salary": 85000
    }
  ]
}
'''

# Parse the JSON data
employees_data = json.loads(data)['employees']

# Calculate the average age of all employees
def calculate_average_age(employees):
    total_age = sum(employee['age'] for employee in employees)
    average_age = total_age / len(employees)
    return average_age

# Find the employee with the highest salary
def find_highest_salary_employee(employees):
    highest_salary_employee = max(employees, key=lambda x: x['salary'])
    return highest_salary_employee

# Count the number of employees in each department
def count_employees_per_department(employees):
    department_count = {}
    for employee in employees:
        department = employee['department']
        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1
    return department_count

# List employees in a department sorted by age in descending order
def employees_in_department_sorted_by_age(employees, department_name):
    department_employees = [employee for employee in employees if employee['department'] == department_name]
    sorted_employees = sorted(department_employees, key=lambda x: x['age'], reverse=True)
    return sorted_employees

# Calculate the average age
average_age = calculate_average_age(employees_data)
print(f"Average age of all employees: {average_age}")

# Find the employee with the highest salary
highest_salary_employee = find_highest_salary_employee(employees_data)
print(f"Employee with the highest salary: {highest_salary_employee['name']} with salary {highest_salary_employee['salary']}")

# Count the number of employees in each department
department_count = count_employees_per_department(employees_data)
print("Number of employees in each department:", department_count)

# Get employees in 'Engineering' department sorted by age in descending order
engineering_employees_sorted_by_age = employees_in_department_sorted_by_age(employees_data, 'Engineering')
print("Employees in Engineering department sorted by age:", engineering_employees_sorted_by_age)

# Example of how to use the function for any department
marketing_employees_sorted_by_age = employees_in_department_sorted_by_age(employees_data, 'Marketing')
print("Employees in Marketing department sorted by age:", marketing_employees_sorted_by_age)
