import pandas as pd
from matplotlib import pyplot as plt



df = pd.read_csv('historic_bets.csv')


for player in df:
    plt.plot(df[player])


print(f'The number of players\' history illustraded: {len(df.columns)}')


plt.hlines(10000, 0, 800, color='grey', linestyle='dotted')

plt.title('Black Jack Profits')
plt.ylabel('Player balance at game X')
plt.xlabel('Nr of games played')
plt.show()
