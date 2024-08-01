# JHU-BSPH - Data Science Assessment 2024

## Q1 - Graph for 'Deadliest natural disasters by year excluding epidemics and famines (1900-2024)'
### Sourced from: https://en.wikipedia.org/wiki/List_of_natural_disasters_by_death_toll
### Date: 7.31.2024

Code for Q1 scrapes Wikipedia webpage for article 'List of natural disasters by death toll' and loads up data for two seperate tables in section 'Deadliest natural disasters by year excluding epidemics and famines.' Table 1 is list of deadliest disasters in 20th century, with each entry in the table detailing the year of incident, death toll of incident, formal event name, imapcted countries, natural disaster type, and date of incident. Table 2 is nearly identical, but for disasters from 2001-2024. Tables were merged together after scraping and data sanitization, then plotted via plotly as both *.png image file and interactive HTML.

![Bar plot visually shows data derived from scraped tables](/jhu-ds-assessment/Q1/results/data-sci-q1-graph.png)

Height of each bar plot demonstrates extent of death toll for the deadliest disaster for a given year. Each bar is colored by disaster type (see key to right of figure).