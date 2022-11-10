from project import Project
from datetime import datetime
from operator import attrgetter

MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""
FILE_NAME = "project.txt"


def load_project(file_name):
    """Read file of programming language details, save as objects, display a list of projects"""
    projects = []
    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)

    in_file.close()
    return projects


def display(projects):
    print("Incomplete projects: ")
    incomplete_projects = [project for project in projects if project.complete_percentage < 100]
    incomplete_projects.sort(key=attrgetter('priority'))
    for project1 in incomplete_projects:
        print(" ", project1)
    print("Complete projects: ")
    complete_projects = [project for project in projects if project.complete_percentage == 100]
    complete_projects.sort(key=attrgetter('priority'))
    for project2 in complete_projects:
        print(" ", project2)


def add_project(projects):
    print('Lets add a new project')
    name = input('Name: ')
    start_date = input('Start date (dd/mm/yy): ')
    priority = int(input('Priority: '))
    cost = float(input('Cost estimate: $'))
    complete_percentage = int(input('Percent complete: '))
    projects.append(Project(name, start_date, priority, cost, complete_percentage))
    return projects


def string_to_date(projects):
    """Still could not finish this function of comparing dates"""
    projects_datetime = [datetime.strptime(x, "%d/%m/%Y") for x in projects]
    date_string = input("Show projects that start after date (dd/mm/yy): ")  # e.g., "30/9/2022"
    format_date = datetime.strptime(date_string, "%d/%m/%Y")
    for date in projects:
        if projects_datetime > format_date:
            print(date)


def save_file(file_name, projects):
    try:
        outfile = open(file_name, 'w')
        for project in projects:
            print(project.name + ', start: ' + str(project.start_date) + ',' + str(
                project.priority) + ', estimate: $' + str(
                project.cost) + ',completion: ' + str(project.complete_percentage) + "%", file=file_name)
        print(f'{len(projects)} guitars saved to {file_name}')
        outfile.close()
    except IOError:
        print('Error: can not open file')


def update_file(projects):
    for project in projects:
        print(
            project.name + ', start: ' + str(project.start_date) + ',' + str(project.priority) + ', estimate: $' + str(
                project.cost) + ',completion: ' + str(project.complete_percentage) + "%")


def main():
    projects = load_project(FILE_NAME)
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'D':
            display(projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'F':
            string_to_date(projects)
        elif choice == 'S':
            save_file(FILE_NAME, projects)
        elif choice == 'U':
            update_file(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>>").upper()
    print("Thank you for using custom-built project management software.")


if __name__ == '__main__':
    main()
