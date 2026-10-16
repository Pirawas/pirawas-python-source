"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
i = 0
temps_list = []
def get_temperture():
    while i < 7:
        temp = float(input(f"Enter temperture {i + 1} day: "))
        temps_list.append(temp)
        i += 1
       
def analysis_temps(temps_list):
 
    average = sum(temps_list) / 7
    high = max(temps_list)
    low = min(temps_list)
 
    return (average, high, low)
 
def display_analysis(average, high, low):
    print("Temperture Anlysis for the week:")
    print("Average: %.1f C" % average)
    print("Highest: %.1f C" % high)
    print("Lowest: %.1f C" % low)
 
obj = get_temperture(temps_list)
result = analysis_temps()
display_analysis(result[0], result[1], result[2])    
