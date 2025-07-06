import fastf1 as f1
import matplotlib.pyplot as plt
import pandas as pd
import fastf1.plotting

session = f1.get_session(2021, 'Italian Grand Prix', 'R')
session.load()

def get_position_changes(session):
    changes = []
    laps = session.laps.pick_quicklaps() 
    
    drivers = pd.unique(laps['Driver'])
    
    
    pos_data = laps[['LapNumber', 'Driver', 'Position']].dropna()
    pos_data = pos_data.astype({'LapNumber': 'int', 'Position': 'int'})
    

    for driver_id in drivers:
        driver_laps = pos_data[pos_data['Driver'] == driver_id]
        driver_laps = driver_laps.sort_values('LapNumber')
        
        prev_pos = None
        for _, row in driver_laps.iterrows():
            current_pos = row['Position']
            if prev_pos is not None and current_pos != prev_pos:
                changes.append({
                    'lap': row['LapNumber'],
                    'driver': session.get_driver(driver_id)["Abbreviation"], 
                    'pos_change': prev_pos - current_pos,  
                    'position': current_pos
                })
            prev_pos = current_pos
            
    return pd.DataFrame(changes)


position_changes = get_position_changes(session)
position_changes = position_changes[position_changes['pos_change'] != 0]




if not position_changes.empty:
    print("Position changes found:\n", position_changes.head())
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)  
    pd.set_option('display.width', None)         
    pd.set_option('display.max_colwidth', None) 
    print("Position changes found:\n", position_changes)

    
    plt.figure(figsize=(12, 6))
    

    driver_colors = {driver_abbr: fastf1.plotting.get_driver_color(driver_abbr, session) for driver_abbr in position_changes['driver'].unique()}


    for driver in position_changes['driver'].unique():
        driver_data = position_changes[position_changes['driver'] == driver]
        plt.scatter(
            x=driver_data['lap'],
            y=driver_data['position'],
            c=[driver_colors[driver]], 
            alpha=0.7,
            s=100,
            edgecolors='w',
            label=driver
        )
    
    plt.title(f"{session.event['EventName']} {session.event.year} - Position Changes")
    plt.xlabel("Lap Number")
    plt.ylabel("Position")

    plt.gca().invert_yaxis()  
    plt.grid(alpha=0.3)
    plt.legend(title="Driver")
    plt.tight_layout()
    plt.show()
    
else:
    print("No position changes recorded in this session!")

