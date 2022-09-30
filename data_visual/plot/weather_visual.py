#! work whith .csv file to get weather info.
import csv, pathlib, re
from matplotlib import pyplot as plt
from datetime import datetime

# home = pathlib.Path.home()
# file_name = 'sitka_weather_2014.csv'
# file = pathlib.Path(home, 'PycharmProjects', 'data_visual', 'main', 'chapter_16', file_name)
#
# date, maxes, mins = [], [], []
# with open(file, 'r') as f:
#     reader = csv.reader(f)
#     # header = next(reader)
#
#     for row in reader:
#         try:
#             time_posted = datetime.strptime(row[0], '%Y-%m-%d')
#             max = row[10]
#             min = row[12]
#
#         except ValueError:
#             print(date, 'missing data.')
#
#         else:
#             date.append(time_posted)
#             maxes.append(float(max))
#             mins.append(float(min))
#
#
# fig = plt.figure(dpi=128, figsize=(10,6))
# plt.plot(date, maxes, c='red', alpha=0.5)
# plt.plot(date, mins, c='blue', alpha=0.5)
# plt.fill_between(date, maxes, mins, facecolor='orange', alpha=0.2)
# #
# plt.title('Sea level pressure.', fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel('Sea level', fontsize=16)
# fig.autofmt_xdate()
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.show()

class Weather_compare():
    # Takes csv file returns date, max, min temperature
    def __init__(self, file):
        self.file = file
        self.date, self.maxes, self.mins = [], [], []

        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)

            for row in reader:
                try:
                    time_posted = datetime.strptime(row[0], '%Y-%m-%d')
                    max = (int(row[1]) - 32) // 1.8
                    min = (int(row[3]) - 32) // 1.8
                except ValueError:
                    print(self.date, 'missing date.')
                else:
                    self.date.append(time_posted)
                    self.maxes.append(max)
                    self.mins.append(min)

    def get_date_list(self):
        return self.date

    def get_maxes_list(self):
        return self.maxes

    def get_mins_list(self):
        return self.mins


def compare_weather(place1, place2):
    # file1 = input('File: ')
    # file2 = input('File: ')
    # name1 = re.findall(r'(?<=:).*(?=\d)', file1.replace('_', ' '))
    # name2 = re.findall(r'(?<=:).*(?=\d)', file2.replace('_', ' '))

    city1 = Weather_compare(place1)
    city2 = Weather_compare(place2)
    # Experimenting with fill_between()
    maxes_of_city1 = city1.get_maxes_list()
    maxes_of_city2 = city2.get_maxes_list()
    date = city1.get_maxes_list()
    #
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(date, maxes_of_city1, c='red', alpha=0.8)
    plt.plot(date, maxes_of_city2, c = 'purple', alpha=0.8)
    plt.fill_between(date, maxes_of_city1, maxes_of_city2, c='orange', alpha=0.3)
    #
    plt.title('Compare max temps of two cityes.', fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperatures in C.', fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


home = pathlib.Path.home()
city1 = pathlib.Path(home, 'PycharmProjects', 'data_visual', 'main', 'chapter_16', 'death_valley_2014.csv')
city2 = pathlib.Path(home, 'PycharmProjects', 'data_visual', 'main', 'chapter_16', 'sitka_weather_2014.csv')
compare_weather(city1, city2)



