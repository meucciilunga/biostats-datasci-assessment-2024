import pandas as pd
import re
import statistics
import plotly.express as px
import plotly.io as pio

# Load webpage and parse via pandas
url = "https://en.wikipedia.org/wiki/List_of_natural_disasters_by_death_toll"
tables = pd.read_html(url)

# Collect appropriate tables from webpage (20th and 21st century mortality)
century_1900 = tables[2]
century_2001 = tables[3]

# Given raw input taken from target webpage mortality table, sanitize table values
def clean_death_toll_num(raw_toll_num_str):

    # Constant values
    dash_chars = ['–', '-']
    ref_pattern = r'\[[0-9][0-9]\]'

    # Remove wikipedia reference [*] pollution
    matches = re.finditer(ref_pattern, raw_toll_num_str)
    for match in matches:
        replacement_target = raw_toll_num_str[match.start():match.end()]
        raw_toll_num_str = raw_toll_num_str.replace(replacement_target, '')
    
    # Split range-estimates into list
    if dash_chars[0] in raw_toll_num_str:
        raw_toll_num_str = raw_toll_num_str.split(dash_chars[0])
    elif dash_chars[1] in raw_toll_num_str:
        raw_toll_num_str = raw_toll_num_str.split(dash_chars[1])
    else:
        raw_toll_num_str = [raw_toll_num_str]

    # Remove commas and Over-range markers '+'
    raw_toll_num_str = [num.replace(',', '').replace('+', '') for num in raw_toll_num_str]

    # Take midpoint of ranges; convert everything to ints
    if len(raw_toll_num_str) == 2:
        raw_toll_num_str = [float(x) for x in raw_toll_num_str]
        raw_toll_num_str = int(statistics.mean(raw_toll_num_str))
    elif len(raw_toll_num_str) == 1:
        raw_toll_num_str = int(raw_toll_num_str[0])

    return(raw_toll_num_str)

# Unify Tables Together
century_1900_2024 = pd.concat([century_1900, century_2001], ignore_index=True)

# Clean death tolls for each position in the chart
cleaned_death_toll = [clean_death_toll_num(x) for x in century_1900_2024['Death toll']]
century_1900_2024['Death toll'] = cleaned_death_toll

# Create a bar chart via plotly
plot_title = 'Deadliest natural disasters by year (1900-2024) excluding epidemics and famines -- Wikipedia'
fig = px.bar(century_1900_2024, x='Year', y='Death toll', color='Type', title=plot_title)
fig.show()

# OPTIONAL - save results to files
# Data table
output_csv_path = '/home/katavga/coding/jhu-ds-assessment/Q1/results/data-sci-q1-table-results.csv'
century_1900_2024.to_csv(output_csv_path, header=True, sep=',', date_format='%Y-%m-%d',encoding='utf-8')

# Plot
output_html = '/home/katavga/coding/jhu-ds-assessment/Q1/results/data-sci-q1-graph.html'
output_png = '/home/katavga/coding/jhu-ds-assessment/Q1/results/data-sci-q1-graph.png'
pio.write_image(fig, output_png, width=2000, height=1000)
pio.write_html(fig, output_html)