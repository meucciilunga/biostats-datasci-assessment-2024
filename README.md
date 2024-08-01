# JHU-BSPH - Biostatistics PhD - Data Science Assessment 2024

## Q1 - Graph for 'Deadliest natural disasters by year excluding epidemics and famines (1900-2024)'
### Data sourced from: https://en.wikipedia.org/wiki/List_of_natural_disasters_by_death_toll
### Date: 7.31.2024

Code for Q1 scrapes Wikipedia webpage article for 'List of natural disasters by death toll' and loads up data for two seperate tables in section 'Deadliest natural disasters by year excluding epidemics and famines.' Table 1 is list of deadliest disasters in 20th century, with each entry in the table detailing the year of incident, death toll of incident, formal event name, imapcted countries, natural disaster type, and date of incident. Table 2 is nearly identical, but for disasters from 2001-2024. Tables were merged together after scraping and then the data in 'Death toll' column was sanitized; afterwards, table was plotted via plotly then exported as both *.png image file and interactive HTML. 'Death toll' values were sanitized according to spec. provided in original assessment instructions paper provider by examiners. Resulting table from scraping code is as follows:

| Year   | Death toll   | Event                                                       | Countries affected                                          | Type                    | Date                       |
|:-------|:-------------|:------------------------------------------------------------|:------------------------------------------------------------|:------------------------|:---------------------------|
| 1900   | 9000         | 1900 Galveston hurricane                                    | United States                                               | Tropical cyclone        | September 9                |
| 1901   | 9500         | 1901 eastern United States heat wave                        | United States                                               | Heat wave               | June–July                  |
| 1902   | 29000        | 1902 eruption of Mount Pelée                                | Martinique                                                  | Volcanic eruption       | April–August               |
| 1903   | 3500         | 1903 Manzikert earthquake                                   | Turkey                                                      | Earthquake              | April 28                   |
| 1904   | 400          | 1904 Sichuan earthquake                                     | China                                                       | Earthquake              | August 30                  |
| 1905   | 20000        | 1905 Kangra earthquake                                      | India                                                       | Earthquake              | April 4                    |
| 1906   | 15000        | 1906 Hong Kong typhoon                                      | Hong Kong,China                                             | Tropical cyclone        | September 18               |
| 1907   | 13500        | 1907 Qaratog earthquake                                     | Uzbekistan                                                  | Earthquake              | October 21                 |
| 1908   | 78500        | 1908 Messina earthquake                                     | Italy                                                       | Earthquake              | December 28                |
| 1909   | 7000         | 1909 Borujerd earthquake                                    | Iran                                                        | Earthquake              | January 23                 |
| 1910   | 2450         | 1910 Costa Rica earthquakes                                 | Costa Rica                                                  | Earthquake              | May 4                      |
| 1911   | 41072        | 1911 France heat wave                                       | France                                                      | Heat wave               | June–August                |
| 1912   | 135000       | 1912 China typhoon                                          | China                                                       | Tropical cyclone        | August 29                  |
| 1913   | 1421         | 1913 Eshan earthquake                                       | China                                                       | Earthquake              | December 21                |
| 1914   | 2344         | 1914 Burdur earthquake                                      | Turkey                                                      | Earthquake              | October 4                  |
| 1915   | 31294        | 1915 Avezzano earthquake                                    | Italy                                                       | Earthquake              | January 13                 |
| 1916   | 6000         | White Friday avalanches                                     | Italy                                                       | Avalanche               | December 13                |
| 1917   | 1500         | 1917 Bali earthquake                                        | Indonesia                                                   | Earthquake              | January 21                 |
| 1918   | 1000         | 1918 Shantou earthquake                                     | China                                                       | Earthquake              | February 13                |
| 1919   | 5000         | 1919 Kelud mudflow                                          | Indonesia                                                   | Volcanic eruption       | May 19                     |
| 1920   | 266057       | 1920 Haiyuan earthquake                                     | China, Mongolia                                             | Earthquake              | December 16                |
| 1921   | 215          | September 1921 San Antonio floods                           | United States                                               | Flood                   | September 7 –11            |
| 1922   | 75000        | 1922 Shantou typhoon                                        | Philippines, China                                          | Tropical cyclone        | July 27 –August 3          |
| 1923   | 124092       | 1923 Great Kantō earthquake                                 | Japan                                                       | Earthquake              | September 1                |
| 1924   | 1000         | Great flood of 99                                           | India                                                       | Flood                   | July                       |
| 1925   | 5000         | 1925 Dali earthquake                                        | China                                                       | Earthquake              | March 16                   |
| 1926   | 709          | 1926 Havana–Bermuda hurricane                               | Cuba, United States, Bahamas, Bermuda                       | Tropical cyclone        | October 14 –28             |
| 1927   | 40912        | 1927 Gulang earthquake                                      | China, Tibet                                                | Earthquake              | May 22                     |
| 1928   | 4112         | 1928 Okeechobee hurricane                                   | United States, Puerto Rico, Guadeloupe, Bahamas, Dominica,  | Tropical cyclone        | September 12 –21           |
| 1929   | 3528         | 1929 Kopet Dag earthquake                                   | Iran, Turkmenistan                                          | Earthquake              | May 1                      |
| 1930   | 5000         | 1930 San Zenón hurricane                                    | Dominican Republic                                          | Tropical cyclone        | September 3                |
| 1931   | 2211249      | 1931 China floods                                           | China                                                       | Flood                   | July – November            |
| 1932   | 3103         | 1932 Cuba hurricane                                         | Cayman Islands, Cuba                                        | Tropical cyclone        | November 9                 |
| 1933   | 8082         | 1933 Diexi earthquake                                       | China                                                       | Earthquake              | August 25                  |
| 1934   | 11350        | 1934 Nepal–India earthquake                                 | Nepal, India                                                | Earthquake              | January 15                 |
| 1935   | 145000       | 1935 Yangtze flood                                          | China                                                       | Flood                   | July 6                     |
| 1936   | 5000         | 1936 North American heat wave                               | United States, Canada                                       | Heat wave               | June – September           |
| 1937   | 11021        | 1937 Great Hong Kong typhoon                                | China                                                       | Tropical cyclone        | September 2                |
| 1938   | 715          | 1938 Hanshin flood                                          | Japan                                                       | Flood                   | July                       |
| 1939   | 32834        | 1939 Erzincan earthquake                                    | Turkey                                                      | Earthquake              | December 27                |
| 1940   | 1000         | 1940 Vrancea earthquake                                     | Romania                                                     | Earthquake              | November 10                |
| 1941   | 1200         | 1941 Jabal Razih earthquake                                 | Yemen                                                       | Earthquake              | January 11                 |
| 1942   | 61000        | 1942 West Bengal cyclone                                    | India                                                       | Tropical cyclone        | October 14 – 18            |
| 1943   | 3912         | 1943 Tosya–Ladik earthquake                                 | Turkey                                                      | Earthquake              | November 27                |
| 1944   | 10000        | 1944 San Juan earthquake                                    | Argentina                                                   | Earthquake              | January 15                 |
| 1945   | 4000         | 1945 Balochistan earthquake                                 | Pakistan                                                    | Earthquake              | November 28                |
| 1946   | 2550         | 1946 Dominican Republic earthquake                          | Dominican Republic                                          | Earthquake              | August 4                   |
| 1947   | 1077         | Typhoon Kathleen                                            | Japan                                                       | Tropical cyclone        | September 15               |
| 1948   | 60000        | 1948 Ashgabat earthquake                                    | Soviet Union, Iran                                          | Earthquake              | October 6                  |
| 1949   | 7200         | 1949 Khait earthquake                                       | Tajikistan                                                  | Earthquake              | July 10                    |
| 1950   | 4800         | 1950 Assam-Tibet earthquake                                 | India, China                                                | Earthquake              | August 15                  |
| 1951   | 4800         | 1951 Manchuria flood                                        | China                                                       | Flood                   | September 18               |
| 1952   | 2336         | 1952 Severo-Kurilsk earthquake                              | Russia                                                      | Earthquake              | November 4                 |
| 1953   | 2551         | North Sea flood of 1953                                     | Netherlands, Belgium, England, Scotland                     | Flood                   | January 31–February 1      |
| 1954   | 33000        | 1954 Yangtze floods                                         | China                                                       | Flood                   | June – September           |
| 1955   | 1023         | Hurricane Janet                                             | Lesser Antilles, Mexico                                     | Tropical cyclone        | September 22 – 30          |
| 1956   | 4935         | Typhoon Wanda                                               | China                                                       | Tropical cyclone        | August 1                   |
| 1957   | 1500         | 1957 Sangchal earthquake                                    | Iran                                                        | Earthquake              | July 2                     |
| 1958   | 1269         | Typhoon Ida                                                 | Japan                                                       | Tropical cyclone        | September 26               |
| 1959   | 5098         | Typhoon Vera                                                | Japan                                                       | Tropical cyclone        | September 26               |
| 1960   | 14174        | Severe Cyclonic Storm Ten                                   | East Pakistan (now Bangladesh)                              | Tropical cyclone        | October 31                 |
| 1961   | 11468        | Cyclone Winnie                                              | East Pakistan (now Bangladesh)                              | Tropical cyclone        | May 6 – 9                  |
| 1962   | 50935        | Tropical Storm Harriet                                      | Thailand, East Pakistan (now Bangladesh)                    | Tropical cyclone        | October 19 – 31            |
| 1963   | 22000        | Extremely Severe Cyclonic Storm Two                         | East Pakistan (now Bangladesh)                              | Tropical cyclone        | May 28                     |
| 1964   | 7000         | Tropical Storm Joan                                         | Vietnam                                                     | Tropical cyclone        | November 4 – 11            |
| 1965   | 47000        | 1965 Bengal cyclones                                        | East Pakistan (now Bangladesh)                              | Tropical cyclone        | May 11 – 12 and June 1 – 2 |
| 1966   | 8064         | 1966 Xingtai earthquakes                                    | China                                                       | Earthquake              | March 22                   |
| 1967   | 10000        | 1967 Paradip cyclone[14]                                    | India                                                       | Tropical cyclone        | October 26                 |
| 1968   | 15000        | 1968 Dasht-e Bayaz and Ferdows earthquakes                  | Iran                                                        | Earthquake              | August 31                  |
| 1969   | 3000         | 1969 Yangjiang earthquake                                   | China                                                       | Earthquake              | July 26                    |
| 1970   | 400000       | 1970 Bhola cyclone                                          | India, East Pakistan (now Bangladesh)                       | Tropical cyclone        | November 13                |
| 1971   | 100000       | Hanoi and Red River Delta flood                             | North Vietnam                                               | Flood                   | August 1                   |
| 1972   | 5374         | 1972 Qir earthquake                                         | Iran                                                        | Earthquake              | April 10                   |
| 1973   | 2189         | 1973 Luhuo earthquake                                       | China                                                       | Earthquake              | February 6                 |
| 1974   | 8210         | Hurricane Fifi–Orlene                                       | Honduras, Nicaragua, El Salvador, Guatemala, Belize, Mexico | Tropical cyclone        | September 18 – 20          |
| 1975   | 133000       | 1975 Banqiao Dam Failure disaster triggered by Typhoon Nina | China                                                       | Tropical cyclone        | August 7                   |
| 1976   | 448709       | 1976 Tangshan earthquake                                    | China                                                       | Earthquake              | July 28                    |
| 1977   | 30000        | 1977 Andhra Pradesh cyclone                                 | India                                                       | Tropical cyclone        | November 19                |
| 1978   | 20000        | 1978 Tabas earthquake                                       | Iran                                                        | Earthquake              | September 16               |
| 1979   | 2078         | Hurricane David                                             | Dominican Republic, Dominica                                | Tropical cyclone        | August 15 – September 8    |
| 1980   | 3816         | 1980 El Asnam earthquake                                    | Algeria                                                     | Earthquake              | October 10                 |
| 1981   | 3000         | 1981 Golbaf earthquake                                      | Iran                                                        | Earthquake              | June 11                    |
| 1982   | 2800         | 1982 North Yemen earthquake                                 | Yemen                                                       | Earthquake              | December 13                |
| 1983   | 1342         | 1983 Erzurum earthquake                                     | Turkey                                                      | Earthquake              | October 30                 |
| 1984   | 1474         | Typhoon Ike                                                 | Philippines                                                 | Tropical cyclone        | August 26 – September 6    |
| 1985   | 23000        | Armero tragedy                                              | Colombia                                                    | Volcanic eruption       | November 13                |
| 1986   | 1746         | Lake Nyos disaster                                          | Cameroon                                                    | Limnic eruption         | August 21                  |
| 1987   | 1000         | 1987 Ecuador earthquakes                                    | Ecuador                                                     | Earthquake              | March 6                    |
| 1988   | 37500        | 1988 Armenian earthquake                                    | Armenia                                                     | Earthquake              | December 7                 |
| 1989   | 3814         | 1989 Sichuan flood                                          | China                                                       | Flood                   | July 27                    |
| 1990   | 40000        | 1990 Manjil–Rudbar earthquake                               | Iran                                                        | Earthquake              | June 21                    |
| 1991   | 138866       | 1991 Bangladesh cyclone                                     | Bangladesh                                                  | Tropical cyclone        | April 24 – 30              |
| 1992   | 2500         | 1992 Flores earthquake and tsunami                          | Indonesia                                                   | Earthquake, Tsunami     | December 12                |
| 1993   | 9748         | 1993 Latur earthquake                                       | India                                                       | Earthquake              | September 30               |
| 1994   | 3063         | Typhoon Fred                                                | China, Taiwan                                               | Tropical cyclone        | August 21                  |
| 1995   | 6434         | Great Hanshin earthquake                                    | Japan                                                       | Earthquake              | January 17                 |
| 1996   | 1077         | 1996 Andhra Pradesh cyclone                                 | India                                                       | Tropical cyclone        | November 4 – 7             |
| 1997   | 3123         | Tropical Storm Linda                                        | Vietnam, Thailand                                           | Tropical cyclone, Flood | November 1 – 9             |
| 1998   | 11374        | Hurricane Mitch                                             | Honduras, Nicaragua, El Salvador, Guatemala, Belize, Mexico | Tropical cyclone        | October 22 – November 9    |
| 1999   | 17749        | 1999 İzmit earthquake                                       | Turkey                                                      | Earthquake              | August 17                  |
| 2000   | 750          | 2000 Mozambique flood                                       | Mozambique                                                  | Flood                   | February – March           |
| 2001   | 16914        | 2001 Gujarat earthquake                                     | India                                                       | Earthquake              | January 26                 |
| 2002   | 1200         | 2002 Hindu Kush earthquakes                                 | Afghanistan                                                 | Earthquake              | March 25                   |
| 2003   | 72000        | 2003 European heat wave                                     | Europe                                                      | Heat Wave               | July – August              |
| 2004   | 227898       | 2004 Indian Ocean earthquake and tsunami                    | Indonesia, Sri Lanka, India, Thailand, Maldives, Somalia    | Earthquake, Tsunami     | December 26                |
| 2005   | 86675        | 2005 Kashmir earthquake                                     | India, Pakistan                                             | Earthquake              | October 8                  |
| 2006   | 5763         | 2006 Yogyakarta earthquake                                  | Indonesia                                                   | Earthquake              | May 26                     |
| 2007   | 15000        | Cyclone Sidr                                                | Bangladesh, India                                           | Tropical cyclone        | November 11 – 16           |
| 2008   | 138373       | Cyclone Nargis                                              | Myanmar                                                     | Tropical cyclone        | April 27 – May 3           |
| 2009   | 1115         | 2009 Sumatra earthquakes                                    | Indonesia                                                   | Earthquake              | September 30               |
| 2010   | 208000       | 2010 Haiti earthquake                                       | Haiti                                                       | Earthquake              | January 12                 |
| 2011   | 19749        | 2011 Tōhoku earthquake and tsunami                          | Japan                                                       | Earthquake, Tsunami     | March 11                   |
| 2012   | 1901         | Typhoon Bopha                                               | Philippines                                                 | Tropical cyclone        | December 4 – 5             |
| 2013   | 6340         | Typhoon Haiyan                                              | Philippines, Vietnam, China                                 | Tropical cyclone        | November 8 – 10            |
| 2014   | 2700         | 2014 Badakhshan mudslides                                   | Afghanistan                                                 | Landslide               | May 2                      |
| 2015   | 8964         | April 2015 Nepal earthquake                                 | Nepal, India                                                | Earthquake              | April 25                   |
| 2016   | 1111         | 2016 Indian heat wave                                       | India                                                       | Heat wave               | April – May                |
| 2017   | 3059         | Hurricane Maria                                             | Puerto Rico, Dominica                                       | Tropical cyclone        | September 19 – 21          |
| 2018   | 4340         | 2018 Sulawesi earthquake and tsunami                        | Indonesia                                                   | Earthquake, Tsunami     | September 28               |
| 2019   | 3951         | 2019 European heat waves                                    | Europe                                                      | Heat wave               | June – July                |
| 2020   | 6511         | 2020 South Asian floods                                     | Afghanistan, Bangladesh, India, Nepal, Pakistan, Sri Lanka  | Flood                   | May – October              |
| 2021   | 2248         | 2021 Haiti earthquake                                       | Haiti                                                       | Earthquake              | August 14                  |
| 2022   | 24501        | 2022 European heatwaves                                     | Europe                                                      | Heat wave               | June 12 – September 12     |
| 2023   | 60636        | 2023 Turkey–Syria earthquakes                               | Turkey, Syria                                               | Earthquake              | February 6                 |
| 2024   | 1080         | 2024 Enga landslide                                         | Papua New Guinea                                            | Landslide               | 24 May                     |

![Bar plot visually showing data derived from scraped tables](https://github.com/meucciilunga/biostats-datasci-assessment-2024/blob/master/Q1/results/data-sci-q1-graph.png)

### **Height (y-axis) of each bar in the plot represents the extent of the death toll for the deadliest disaster for a given year. Years are listed horizontally along x-axis. Each bar is colored by the type of disaster it represents (see key to right of figure).**




# Addressing Explicit Questions of Q2
### WORK FOR Q2 IS ALSO INCLUDED IN THE REPO. SEE APPROPRIATE DIRECTORY.
### Generally, with a smaller step-value 'e', the algorithm requires more steps to adequately converge to within a given distance of the 'true value' of the modeled loss function and thus results in slower processing times. However, results, especially at each step, are also generally more accurate w/ smaller steps. The gradient descent algorithm developed here tends to fail when, for a fixed number of iterations, the steps are 'too small' and the initial guess is too far away from the true value of the underlying loss function. Notably, larger step sizes also tend to result in two failures: (a) they can trigger overflow errors due to size of intermediate values involved in calculating gradient, or (b) they occassionally cause the gradient descent approximation to diverge, especially if initial guess is too far off.
