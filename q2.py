import matplotlib.pyplot as plt
def graphSnowfall(t):
    try:
        ranges = ['0-10', '11-20', '21-30', '31-40', '41-50']
        counts = [0, 0, 0, 0, 0]
        
        with open(t, 'r') as file:
            for line in file:
                snowfall = int(line.strip())  

                if snowfall >= 0 and snowfall <= 10:
                    counts[0] += 1
                elif snowfall >= 11 and snowfall <= 20:
                    counts[1] += 1
                elif snowfall >= 21 and snowfall <= 30:
                    counts[2] += 1
                elif snowfall >= 31 and snowfall <= 40:
                    counts[3] += 1
                elif snowfall >= 41 and snowfall <= 50:
                    counts[4] += 1
        plt.figure(figsize=(10, 5))
        plt.bar(ranges, counts)
        plt.xlabel('Snowfall Range (cm)')
        plt.ylabel('Number of Occurrences')
        plt.title('Snowfall Accumulation Ranges')
        plt.show()
    
    except FileNotFoundError:
        print(f"The file '{t}' was not found.")

graphSnowfall("snowfall.txt")
