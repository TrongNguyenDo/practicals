import wikipedia


def main():
    valid = True
    """ write a try except to catch Disambiguation Error if the user enter Python"""
    while valid:
        try:
            search_term = input("Enter a page title or search phrase: ")
            if search_term == "Python":
                print("The Python search term could give Disambiguation Error")
                search_term = input("Enter a page title or search phrase: ")
                wikipedia.page(search_term)
                print(wikipedia.summary(search_term))
            elif search_term != "Python":
                wikipedia.search(search_term)
                wikipedia.page(search_term)
                print(wikipedia.summary(search_term))
            elif search_term == "":
                break
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)


main()
