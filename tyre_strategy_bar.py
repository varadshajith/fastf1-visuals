import fastf1 as f1
import matplotlib.pyplot as plt
import pandas as pd

session =  f1.get_session(2023 , 'Hungary' , 'R')
session.load()

def get_tyre_life(session):
    tyre_data = []

    for driver in session.drivers:
        laps = session.laps.pick_drivers(driver)
        stints = laps[['LapNumber' , 'Compound' , 'Stint']].dropna()


        if not stints.empty:
            for stint in stints['Stint'].unique():

                stint_laps = stints[stints['Stint'] == stint]
                compound = stint_laps['Compound'].iloc[0]
                start = stint_laps['LapNumber'].min()
                end = stint_laps['LapNumber'].max()

                tyre_data.append({
                    'Driver' : driver,
                    'Compound' : compound,
                    'Start' : start,
                    'End' : end,
                    'Laps' : end-start + 1
                }) 

    return pd.DataFrame(tyre_data)

tyre_df = get_tyre_life(session)

print(tyre_df.head())


plt.figure(figsize= (15,8))

drivers= tyre_df['Driver'].unique()

y_pos = range(len(drivers))

compound_colors = {
    'SOFT': '#FF3333',
    'MEDIUM': '#FFD700',
    'HARD': '#B0E0E6',
    'INTERMEDIATE': '#00FF00', 
    'WET': '#0000FF',           
    'TEST_UNKNOWN': '#808080'   
}

def get_compound_color(compound):
    return compound_colors.get(
        str(compound).split()[0].upper(),
        '#808080'
    )

for idx , driver in enumerate (drivers):
    driver_tyre = tyre_df[tyre_df['Driver'] == driver]

    for _ , row in driver_tyre.iterrows():
        plt.barh(
            y = idx , 
            width = row['Laps'],
            left = row['Start'] - 1,
            color = get_compound_color(row['Compound']),
            edgecolor = 'black',
            height = 0.6          
            ) 
        

        
plt.yticks(y_pos , [session.get_driver(d).Abbreviation for d in drivers])
plt.title("2023 Hungarian GP Tyre Strategies")
plt.xlabel("Lap Number")
plt.ylabel("Driver")
plt.grid(axis = 'x' , alpha = 0.3)

legend_elements = [
    plt.Rectangle((0,0),1,1, color = compound_colors[c]) for c in compound_colors
]
plt.legend(legend_elements , compound_colors.keys() , title='Compounds')

plt.tight_layout()

plt.show()
