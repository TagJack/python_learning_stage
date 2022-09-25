#! Get info about repos of github.
import json, requests, pygal
from bs4 import BeautifulSoup as bs
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Loading page.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
res = requests.get(url)
res.raise_for_status()

# Getting data.
data = res.json()
repos = data['items']

# Gathering info.
names, plot_dicts = [], []
for item in repos:
    names.append(item['name'])
    dict = {
        'value' : item['stargazers_count'],
        'label' : item['description'],
        'xlink' : item['html_url'],
    }
    plot_dicts.append(dict)

# Building visualization and saving it in the file.
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.show_legends = False
my_config.x_label_rotation = 45
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 16
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

bars = pygal.Bar(my_config, style=my_style)
bars.title = 'The most starred labels in github.'
bars.x_labels = names
bars.add('', plot_dicts)
bars.render_to_file('repos.svg')
