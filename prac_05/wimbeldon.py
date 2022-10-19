COUNTRY_NUMBER = 1
CHAMPION_NUMBER = 2


def main():
    records = []
    with open("wimbeldon.csv", "r", encoding="utf-8-sig") as this_file:
        this_file.readline()
        for i in this_file:
            parts = i.strip().split(",")
            records.append(parts)
    champion_to_count, countries = list_adding(records)
    print("Wimbledon Champions:  ")
    list_result(champion_to_count, countries)


def list_adding(records):
    number_of_champion = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_NUMBER])
        try:
            number_of_champion[record[CHAMPION_NUMBER]] += 1
        except KeyError:
            number_of_champion[record[CHAMPION_NUMBER]] = 1
    return number_of_champion, countries


def list_result(count_champions, countries):
    for name, country in count_champions.items():
        print(name, country)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
