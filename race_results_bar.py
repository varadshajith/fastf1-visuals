import fastf1 as f1
import matplotlib.pyplot as plt
import pandas as pd




session = f1.get_session(2025 , 'China' , 'R')
session.load()

result = session.results
print(result[['DriverNumber' , 'FullName' , 'TeamName' , 'Position']])

plt.figure(figsize=(12,6))

team_color = {
    'RedBull' : '#0600EF',
    'Ferrari' : '#DC0000',
    'Mercedes': '#00D2BE',
    'McLaren' : '#FF8700',
    'Williams': '#00A0DE',
    'AstonMartin': '#002420',
    'Hass' : '#E6002B',
    'Alpine' : '#F363B9',
    'RacingBull' : '#6692FF',
    'KickSauber' : '#2ED719'
}

bar_colors = [team_color.get(team , 'gray')for team in result['TeamName']]

bars = plt.bar(result['FullName'] , result['Position'] , color = bar_colors)
bars[0].set_edgecolor('gold')
bars[0].set_linewidth(3)

plt.annotate('Winner!' ,
            xy = (0 , result['Position'][0]),
            xytext=(5,-20),
            textcoords='offset points',
            color = 'gold' ,
            weight = 'bold')

plt.title("2025 CHINESE GP Finishing Position" , fontsize = 14 , pad= 20)

plt.xlabel('Driver' , labelpad=10)
plt.ylabel('Position' , labelpad=10)
plt.xticks(rotation = 45 , ha = 'right')

plt.grid(axis='y' , linestyle = '--' , alpha = 0.7)

plt.bar(result['FullName'] , result['Position'])

plt.tight_layout()
plt.show()