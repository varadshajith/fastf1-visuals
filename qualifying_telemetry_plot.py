import fastf1 as f1
import matplotlib.pyplot as plt

session = f1.get_session(2025 , 'Saudi Arabian' , 'Q')

session.load()

ver_lap = session.laps.pick_driver('VER').pick_fastest()
ham_lap = session.laps.pick_driver('HAM').pick_fastest()


ver_tele = ver_lap.get_telemetry()
ham_tele = ham_lap.get_telemetry()

plt.figure(figsize=(10,5))
plt.grid(True, color='gray', linestyle='-', linewidth=0.5)  


fig , (ax1 , ax2 ) = plt.subplots(2 , 1 , figsize = (10,8))
plt.suptitle('Saudi Arabian GP 2025 Qualifying', fontsize=14, fontweight='bold', color='black' )

ax1.plot(ver_tele['Distance'] , ver_tele['Speed'], color = '#1E41FF' , label = 'Verstappen 1:27.294' ,  linestyle='--')
ax1.plot(ham_tele['Distance'] , ham_tele['Speed'] , color = '#FF8700', label = "Oscar Piastri 1:27.304" ,  linestyle='-')
ax1.set(ylabel = 'Speed(km/h)' )
ax1.grid(True)




ax2.plot(ver_tele['Distance'] , ver_tele['Throttle'], color = '#1E41FF' , label = 'Verstappen 1:27.294' , linestyle='--')
ax2.plot(ham_tele['Distance'] , ham_tele['Throttle'] , color = '#FF8700', label = "Oscar Piastri 1:27.304", linestyle='-') 
ax2.set(xlabel = 'Track Distance (m)', ylabel = 'Throttle(%)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()

# Increase bottom margin to make space for the footer
plt.subplots_adjust(bottom=0.10)  # Adjusted from 0.15 to 0.25

# Add footer text (position y=0.01 places it just above the bottom edge)
footer_text = "Verstappen took pole position with a time of 1:27.294, while Oscar Piastri qualified second with +0.010s."
plt.figtext(0.5, 0.01, footer_text, 
            ha='center', va='bottom',  # Changed va to 'bottom'
            fontsize=10, color='black')

plt.show()


