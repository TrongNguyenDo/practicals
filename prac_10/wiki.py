import wikipedia


def main():
    while True:
        search_term = input("Enter a page title or search phrase: ")
        if search_term == "":
            break
        else:
            wikipedia.search(search_term)
            print(wikipedia.summary(search_term))
        # write a try except to catch Disambiguation Error if the user enter Python\
        while True:
            try:
                search_term == "Python"
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)


main()
