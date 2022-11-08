from project import Project

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
    # Open the file for reading
    in_file = open(file_name, 'r')
    # File format is like: Language,Typing,Reflection,Year
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()

    # All other lines are project data
    for line in in_file:
        # print(repr(line))  # debugging

        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split('\t')
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        # estimate should be double
        # completion should be int
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))

        # Add the language we've just constructed to the list
        projects.append(project)

    # Close the file as soon as we've finished reading it
    in_file.close()
    return projects


def main():
    projects = load_project(FILE_NAME)
    for project in projects:
        print(project)


if __name__ == '__main__':
    main()

"""def main():
    get_new_file = read_file()
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'L':
            read_file()
        elif choice == 'D':
            display(get_new_file)


def read_file():
    projects = []
    try:
        get_file = open(FILE_NAME, 'r')
        for name in get_file:
            project = name.strip().split(',')
            projects.append(project)
        get_file.close()
    except IOError as error:
        print(f'I/O error: {error}')
    return projects


def display(projects):
    print("Incomplete projects: ")
    incomplete_projects = [project for project in projects if projects.is_not_complete]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Complete projects: ")
    incomplete_projects = [project for project in projects if projects.is_complete]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)


main()"""
