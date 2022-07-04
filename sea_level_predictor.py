import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.subplots(figsize=(18, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='CSIRO Adjusted Sea Level')
    
    # Create first line of best fit
    years_extended = range(df['Year'].min(), 2051, 1)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line = [res.slope*xi + res.intercept for xi in years_extended]
    plt.plot(years_extended, line, 'r', label='fitted line')
    plt.legend()
    # Create second line of best fit
    years_extended = range(2000,2051,1)
    res = linregress(df.loc[df['Year'] >= 2000, 'Year'], df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])
    line = [res.slope*xi + res.intercept for xi in years_extended]
    plt.plot(years_extended, line, 'r', label='fitted line (2000-present)')
    plt.legend()
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()