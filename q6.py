# Create a class name, Teacher. Teacher have some properties name, designation, 
# month salary, and department. In every year he will get 20% increment. 
# After five year how much salary he will get at the end of the year. 
# Expected Output: ahter_five years 298598.4 if he gets 10000 tk per month

class Teacher():

    def __init__(self, teacher_name, teacher_designation, monthly_salary, department):

        self.monthly_salary = monthly_salary

        print(f"""Hi I'm {teacher_name}. My designation is {teacher_designation} and {department} is my department.
        I get {monthly_salary} tk salary at a month. """)

    def getIncrement(self, increment):

        return increment

    def getSalaryEndOfTheYear(self, how_much_year, increments):

        TOTAL_MONTH_IN_A_YEAR = 12

        total_salary_after_the_end_of_a_yr = (
            TOTAL_MONTH_IN_A_YEAR*self.monthly_salary)

        total_salary_after_the_end_ofa_yr_wth_icrement = (
            total_salary_after_the_end_of_a_yr * increments/100) + total_salary_after_the_end_of_a_yr
        print(total_salary_after_the_end_ofa_yr_wth_icrement)
        yr = range(how_much_year)
        for y in yr:
            total_salary_after_the_end_ofa_yr_wth_icrement = (
                total_salary_after_the_end_ofa_yr_wth_icrement*increments/100)+total_salary_after_the_end_ofa_yr_wth_icrement

        print('after_five years', total_salary_after_the_end_ofa_yr_wth_icrement)


# Creating objects
teachers_name = input('Teacher name: ')
teacher_designation = input('Designation: ')
monthly_salary = int(input('Monthly salary: '))
department = input('Ddepartment: ')

teacher = Teacher(teachers_name, teacher_designation,
                  monthly_salary, department)


how_much_increment_get_after_a_yr = int(
    input('How much increments he will get after the end of the year, Ex: 20%: '))
increment_persentage = teacher.getIncrement(how_much_increment_get_after_a_yr)


how_much_year = int(input('Years: '))
teacher.getSalaryEndOfTheYear(how_much_year, increment_persentage)