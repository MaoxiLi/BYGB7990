#Maoxi Li Project(individual)
import pandas as pd
def main():
    df = pd.read_csv('student.txt', sep='\t', header=0) #read the txt file in to a dataframe
    choice = get_menu_choice()
    while choice != 6:
        if choice == 1:
            choice = All_student(df)
        elif choice == 2:
            choice = Last_name_student(df)
        elif choice == 3:
            choice = Certain_year(df)
        elif choice == 4:
            choice = Report_number(df)
        elif choice == 5:
            choice = Classmates(df)

#define a menu function to choose what to do next
def get_menu_choice():
    print('1. Display all student records')
    print('2. Display students whose last name begins with a certain string')
    print('3. Display all records for students whose graduating year is a certain year')
    print('4. Display a summary report of number and percent of students in each program, for students graduating on/after a certain year')
    print('5. Find your classmates')
    print('6. Quit')
    choice = input('Enter your choice (ues number): ')
    try:
        choice = int(choice)
        while choice < 1 or choice > 6:
            print('Please enter a valid choice! ')
            return get_menu_choice()
    except:
        print('Please enter a number! ')
        return get_menu_choice()
    return choice

#define a function to show all student records
def All_student(x):
    pd.set_option('display.max_rows',None) #change the option to show all the rows
    print(x)
    return get_menu_choice()

#define a function to display students whose last name begins with a certain string(case insensitive)
def Last_name_student(x):
    str = input('Enter a string (case insensitive): ')
    name = x.loc[x['Last'].str.contains(f'^{str}', case= False)]
    print(name)
    return get_menu_choice()

#define a function to display all records for students whose graduating year is a certain year
def Certain_year(x):
    try:
        string = int(input('Enter a certain graduate year: '))
        year = x[x['GradYear'] == string]
        print(year)
        return get_menu_choice()
    except:
        print('Please enter a number! ')
        return 3

#define a function to display a summary report of number and percent of students in each program, for students graduating on/after a certain year
def Report_number(x):
    try:
        string = int(input('Enter a year that student graduate on or after: '))
        year = x[x['GradYear'] >= string]
        group = year.groupby(['DegreeProgram']).size().reset_index(name='Counts') #calculate how many students in each program
        total = int(group['Counts'].sum()) #calculate the amount number of students
        for index, row in group.iterrows(): # a for loop to calculate the percent for each program
            percent = row['Counts']/total
            percent = format(percent,'.2%')
            row['Percent'] = percent
            print(f'There are {row["Counts"]} students in {row["DegreeProgram"]} on/after {string} and the percent is {row["Percent"]}')
        return get_menu_choice()
    except:
        print('Please enter a year!')
        return 4

#define a function to display all your classmates
def Classmates(df):
    try:
        string = int(input('Please enter your ID number: ')) #match your classmates by your ID
        match1 = df[df['ID'] == string]
        try:
            classmate = df[(df['GradYear'].values == match1['GradYear'].values) & (df['GradTerm'].values == match1['GradTerm'].values) & (df['DegreeProgram'].values == match1['DegreeProgram'].values)]
            print(classmate)
            return get_menu_choice()
        except:
            print('Please enter a valid ID number! ')
            return 5
    except:
        print('Please enter a number!')
        return 5

main()