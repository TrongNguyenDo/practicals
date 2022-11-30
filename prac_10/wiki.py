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
                wikipedia.search(search_term)
                print(wikipedia.page(search_term))
                print(wikipedia.page(search_term))
                print(wikipedia.page(search_term).title)
                print(wikipedia.summary(search_term))
                print(wikipedia.page(search_term).url)
            elif search_term != "Python":
                wikipedia.search(search_term)
                print(wikipedia.page(search_term))
                print(wikipedia.page(search_term).title)
                print(wikipedia.summary(search_term))
                print(wikipedia.page(search_term).url)
            elif search_term == "":
                break
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)


main()
