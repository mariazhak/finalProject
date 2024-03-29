import csv
import random


def year_reader(csv_reader):
    year_period = {'1950': [], '1970': [], '2000': [], '2024': [], 'DM': []}
    for row in csv_reader:
        year_period['DM'].append(row[0])
        if int(row[2]) <= 1950:
            year_period['1950'].append(row[0])
        elif int(row[2]) <= 1970:
            year_period['1970'].append(row[0])
        elif int(row[2]) <= 2000:
            year_period['2000'].append(row[0])
        else:
            year_period['2024'].append(row[0])
    return year_period


def genre_reader(csv_reader):
    genres = dict()
    for row in csv_reader:
        if row[3] not in genres.keys():
            genres[row[3]] = []
            genres[row[3]].append(row[0])
        else:
            genres[row[3]].append(row[0])
    return genres


def author_reader(csv_reader):
    authors = dict()
    for row in csv_reader:
        authors[row[0]] = row[1]
    return authors


def age_reader(csv_reader):
    ages = {'Early Elementary':[], 'Middle Grade': [], 'Young Adult': [], 'Adult':[], 'DM':[]}
    for row in csv_reader:
        possible_ages = row[4].split('/')
        ages['DM'].append(row[0])
        for age in possible_ages:
            ages[age].append(row[0])
    return ages


def get_genre():
    print('Please choose a genre from possible options(enter the number): ')
    genre_list = []
    for genre in genres.keys():
        genre_list.append(genre)
    for i in range(len(genre_list)):
        print(f'{i+1}. ', genre_list[i])
    genre_choice = int(input())
    while genre_choice not in range(1, len(genre_list) + 1):
        genre_choice = int(input('Wrong option, please try again: '))
    return genre_list[genre_choice-1]


def get_year():
    print('Please choose a year period from possible options(enter the number): ')
    print('1. Before 1950')
    print('2. 1950-1970')
    print('3. 1970-2000')
    print('4. 2000- now')
    print('5. Does not matter')
    year_choice = int(input())
    while year_choice not in range(1, 6):
        year_choice = int(input('Wrong option, please try again: '))
    if year_choice == 1:
        return '1950'
    elif year_choice == 2:
        return '1970'
    elif year_choice == 3:
        return '2000'
    elif year_choice == 4:
        return '2024'
    else:
        return 'DM'


def get_age():
    print('Please choose an age of the reader from possible options(enter the number): ')
    counter = 1
    age_list = []
    for age in ages:
        if age == 'DM':
            continue
        else:
            print(f'{counter}.', age)
            age_list.append(age)
        counter += 1
    print(f'{counter}. Does not matter')
    age_list.append('DM')
    age_choice = int(input())
    while age_choice not in range(1, counter+1):
        age_choice = int(input('Wrong option, please try again: '))
    return age_list[age_choice - 1]


def choicer(genre, year, age):
    possible_choices = []
    for option in genres[genre]:
        if option in year_periods[year]:
            if option in ages[age]:
                possible_choices.append(option)
    return possible_choices


def choicer2(genre, year, age):
    genre_year = []
    if year != 'DM':
        for option in genres[genre]:
            if option in year_periods[year]:
                genre_year.append(option)
        print(f'For genre {genre} and given time period: ')
        if len(genre_year) == 0:
            print('No options found!')
        else:
            for i in range(len(genre_year)):
                print(f'{i+1}. "', genre_year[i], '" Author: ', author[genre_year[i]])

    genre_age = []
    if age != 'DM':
        for option in genres[genre]:
            if option in ages[age]:
                genre_age.append(option)
        print(f'For genre {genre} and for {age}: ')
        if len(genre_age) == 0:
            print('No options found!')
        else:
            for i in range(len(genre_age)):
                print(f'{i + 1}. "', genre_age[i], '" Author: ', author[genre_age[i]])

    year_age = []
    if age !='DM' and year != 'DM':
        for option in year_periods[year]:
            if option in ages[age]:
                year_age.append(option)
        print(f'For given time period and for {age}: ')
        if len(year_age) == 0:
            print('No options found!')
        else:
            for i in range(len(year_age)):
                print(f'{i + 1}. "', year_age[i], '" Author: ', author[year_age[i]])


def list_display(l, genre, year, age):
    if len(l) == 0:
        print('Sorry, no options found!')
        print('Do you want to see the books which suits to two of your criteria? Enter yes/no')
        input_choice = input().lower()
        while input_choice not in ['yes', 'no']:
            input_choice = input('Wrong input! Try again please: ').lower()
        if input_choice == 'yes':
            choicer2(genre, year, age)
        else:
            print('Okay!')
    else:
        if len(l) == 1:
            print('The recommended book is ', l[0], ' Author: ', author[l[0]])
        else:
            print('There are more than one option found!')
            print('Do you want to see all options or the random one? Enter all/rand: ')
            input_choice = input().lower()
            while input_choice != 'all' and input_choice != 'rand':
                input_choice = input('Wrong input! Try again please: ').lower()
            if input_choice == 'all':
                print('Here is the list of books which you would like:')
                for i in range(len(l)):
                    print(f'{i+1}. "', l[i], '" Author: ', author[l[i]])
            else:
                rand_choice = random.randint(0, len(l)-1)
                print('The recommended book is: "', l[rand_choice], '" Author: ', author[l[rand_choice]])


with open('data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    genres = genre_reader(csvreader)

with open('data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    year_periods = year_reader(csvreader)

with open('data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    ages = age_reader(csvreader)

with open('data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    author = author_reader(csvreader)

name = input('Welcome to book choicer! Enter your name please:')
print(f'Hi {name}!')
genre = get_genre()
year = get_year()
age = get_age()

possible_choices = choicer(genre, year, age)

list_display(possible_choices, genre, year, age)

print('Thank you for using this book recommender! Goodbye!')