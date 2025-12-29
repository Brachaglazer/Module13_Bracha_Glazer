import matplotlib.pyplot as plt;

try:
    with open("weather_data_flatbush.csv", "r") as f:
        month = []
        high_temp = []
        count = 0
        for line in f:
            if count > 0:
                line = line.strip(" ").strip("\n")
                line = line.split(",")
                month.append(line[0])
                line[1] = int(line[1])
                high_temp.append(line[1])
            else:
                count += 1
except FileNotFoundError as err:
    print("file not found", err)

try:
    with open("flatbush_extremes.csv", "r") as f:
        month2 = []
        record_high = []
        record_low = []
        snow = []
        count = 0
        for line in f:
            if count > 0:
                line = line.strip(" ").strip("\n")
                line = line.split(",")
                month2.append(line[0])
                line[1] = int(line[1])
                line[2] = int(line[2])
                line[3] = float(line[3])
                record_high.append(line[1])
                record_low.append(line[2])
                snow.append(line[3])
            else:
                count += 1
except FileNotFoundError as err:
    print("file not found", err)

def barchart():
    # Create a list with the X coordinates of each bar's left edge.
    x_axis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # Create a list with the heights of each bar.
    y_axis = [high_temp[0], high_temp[1], high_temp[2], high_temp[3], high_temp[4], high_temp[5], high_temp[6],
              high_temp[7], high_temp[8], high_temp[9], high_temp[10], high_temp[11]]

    greatest = max(y_axis)
    highest = y_axis.index(greatest)
    print(f"Month with the highest value is {month[highest]}")

    least = min(y_axis)
    lowest = y_axis.index(least)
    print(f"Month with the lowest value is {month[lowest]}")

    total = sum(y_axis)
    print(f"Total of all the temps: {total}")

    bar_width = 1

    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
               [month[0], month[1], month[2], month[3], month[4], month[5], month[6], month[7], month[8],
                month[9], month[10], month[11]])

    plt.title("Average High Temps per Month")
    # Build the bar chart.
    plt.bar(x_axis, y_axis, bar_width,
            color=('b', 'g', 'r', 'c', 'm'))

    plt.grid(True)
    # Display the bar chart.
    plt.show()

def line_graph():
    # Lists with the x and y coordinates
    x_axis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y_axis = [record_high[0], record_high[1], record_high[2], record_high[3], record_high[4], record_high[5],
              record_high[6], record_high[7], record_high[8], record_high[9], record_high[10], record_high[11]]

    y_axis2 = [record_low[0], record_low[1], record_low[2], record_low[3], record_low[4], record_low[5],
              record_low[6], record_low[7], record_low[8], record_low[9], record_low[10], record_low[11]]

    greatest = max(y_axis)
    highest = y_axis.index(greatest)
    print(f"Month with the highest value in highest temps is {month2[highest]}")

    least = min(y_axis)
    lowest = y_axis.index(least)
    print(f"Month with the lowest value in highest temps is {month2[lowest]}")

    total = sum(y_axis)
    print(f"Total of all the highest temps: {total}")

    best = max(y_axis2)
    best_lower = y_axis2.index(best)
    print(f"Month with the highest value in lowest temps is {month2[best_lower]}")

    worst = min(y_axis)
    bad_lower = y_axis.index(worst)
    print(f"Month with the lowest value in lowest temps is {month2[bad_lower]}")

    total = sum(y_axis2)
    print(f"Total of all the lowest temps: {total}")

    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
               [month2[0], month2[1], month2[2], month2[3], month2[4], month2[5], month2[6], month2[7], month2[8],
                month2[9], month2[10], month2[11]])
    plt.title("Recorded High and Low Temps per Month")
    plt.plot(x_axis, y_axis, y_axis2, marker='o')
    plt.grid(True)
    plt.show()

def snow_chart():
    x_axis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y_axis = [snow[0], snow[1], snow[2], snow[3], snow[4], snow[5], snow[6],
              snow[7], snow[8], snow[9], snow[10], snow[11]]
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
               [month2[0], month2[1], month2[2], month2[3], month2[4], month2[5], month2[6], month2[7], month2[8],
                month2[9], month2[10], month2[11]])

    greatest = max(y_axis)
    highest = y_axis.index(greatest)
    print(f"Month with the highest value is {month2[highest]}")

    least = min(y_axis)
    lowest = y_axis.index(least)
    print(f"Month with the lowest value is {month2[lowest]}")

    total = sum(y_axis)
    print(f"Total of all the snow: {total}")

    bar_width = 1
    plt.bar(x_axis, y_axis, bar_width,
            color=('b', 'g', 'r', 'c', 'm'))
    plt.title("Average Snow per Month")
    plt.grid(True)
    plt.show()

def plot_graph():
    sub = [a - b for a, b in zip(record_high, record_low)]
    x_axis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y_axis = [sub[0], sub[1], sub[2], sub[3], sub[4], sub[5],
              sub[6], sub[7], sub[8], sub[9], sub[10], sub[11]]

    greatest = max(y_axis)
    highest = y_axis.index(greatest)
    print(f"Month with the highest value is {month2[highest]}")

    least = min(y_axis)
    lowest = y_axis.index(least)
    print(f"Month with the lowest value is {month2[lowest]}")

    total = sum(y_axis)
    print(f"Total of all the values: {total}")

    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
               [month2[0], month2[1], month2[2], month2[3], month2[4], month2[5], month2[6], month2[7], month2[8],
                month2[9], month2[10], month2[11]])
    plt.title("Range of Temps per Month")
    plt.plot(x_axis, y_axis, marker='o')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    barchart()
    line_graph()
    snow_chart()
    plot_graph()

"""
Graph 1- barchart:
This graph shows the average high temperatures for each month from the weather_data_flatbush.csv file.
I notice that the temperature is higher during the summer months and lower during the winter months in Flatbush.
The weather gradually increases and decreases but the highest of each month ranges between 35-85 appox.
I was surprised that the average high of the summer months is around 85, I would have expected it to be higher than that.
I was also surprised that the highests temperatures in February were lower than Decemeber because I always thought of
December and January as the coldest months.

Graph 2- line_graph:
This graph shows the recorded high temperatures and low temperatures for each month from the flatbush_extremes.csv
file. I noticed that the high temperatures change a lot more gradually than the low temperatures. I also noticed that the 
low temperatures get very low and the high temperatures get very high. I was surprised to see that the temperatures
dropped so low and rose so high because I live nearby and don't recall such extreme temperatures. It was also surprising
to see that the temperature high in January was lower than the temperature high in December.

Graph 3- snow_chart:
This graph shows the average snow per month in inches from the flatbush_extremes.csv file. I notice that it only snows
during the winter months in Flatbush. I also notice that even though January has the highest value, the months before it
had a lot less snow than the months that come after it. I was surprised that snow fell in April because it usually
starts getting warmer then. I was also surprised that December had very little snow compared to the large amount that
January had.

Graph 4- plot_graph:
This graph shows the range of temperatures per month from the flatbush_extremes file. I notice that the range is much
greater in the winter months than it is in the summer months. I supposed that it has to do with warmth the sun brings in
during the day and the lack there of during the night time. I am surprised that there is such a steep slope from april 
to July and july to september, unlike any other part of the graph. I am also surprised that the range is so large as I
thought it would be closed to a 20 degree difference than a 50 degree difference.

Thank you!
"""