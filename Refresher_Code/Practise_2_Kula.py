data = {
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


# Parse the dictionary
employees_data = data['employees']

# 1. Calculate the average age of all employees
def calculate_average_age(employees):
    total_age = 0 # Initialize
    for employee in employees:
        total_age += employee["age"]
        average_age = total_age / len(employees_data)
    return average_age

average_age = calculate_average_age(employees_data)
print ("Average age is ", average_age)


# 2. Find the employee with the highest salary
def high_salary_identifier(employees):
    high_Salary = [] # initilaze
    for employee in employees:
      if employee['salary'] > high_Salary:
        high_Salary = employee
    return high_Salary

highest_salary = high_salary_identifier(employees_data)
print ("highest salary is: ",high_salary_identifier(highest_salary))

# 3. Count the number of employees in each department

# 4. Get employees in 'Engineering' department sorted by age in descending order

# 5. Example of how to use the function for any department

def get_employees_by_department(employees, department):
  filtered_employees = []
  for employee in employees:
    if employee['department'] == department:
      filtered_employees.append(employee)
  sorted_employees = sorted(filtered_employees, key=lambda x: x['age'], reverse=True)
  return sorted_employees


# Get employees in 'Engineering' department sorted by age in descending order
engineering_employees = get_employees_by_department(employees_data, 'Engineering')
print(engineering_employees)

# Example of how to use the function for any department
sales_employees = get_employees_by_department(employees_data, 'Sales')
print(sales_employees)