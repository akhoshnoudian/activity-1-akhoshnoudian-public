import random
import time
import matplotlib.pyplot as plt
from q6_sort import Vehicle, selection_sort, bubble_sort, merge_sort, sort


def generate_vehicles(num):
    manufacturers = ["Toyota", "Ford", "Honda", "Chevrolet", "Nissan"]
    models = ["ModelA", "ModelB", "ModelC", "ModelD", "ModelE"]
    types = ["Sedan", "Coupe", "SUV", "Truck"]

    return [
        Vehicle(
            random.choice(manufacturers),
            random.choice(models),
            random.choice(types),
            random.randint(20000, 50000),
            random.randint(5000, 200000),
        )
        for _ in range(num)
    ]


def measure_performance():
    sizes = [10, 50, 100, 500, 1000]
    results = {"Selection Sort": [], "Bubble Sort": [], "Merge Sort": []}

    for size in sizes:
        vehicles = generate_vehicles(size)

        for name, alg in zip(results.keys(), [selection_sort, bubble_sort, merge_sort]):
            start_time = time.time()
            sort(vehicles, alg, key=lambda v: v.cost)
            elapsed_time = time.time() - start_time
            results[name].append(elapsed_time)

    for alg_name, times in results.items():
        plt.plot(sizes, times, label=alg_name)

    plt.xlabel("Number of Vehicles")
    plt.ylabel("Execution Time (s)")
    plt.title("Performance of Sorting Algorithms")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    vehicles = generate_vehicles(10)
    print("Original List:")
    for v in vehicles:
        print(v)

    print("\nSorted List (by cost using merge sort):")
    sorted_vehicles = sort(vehicles, merge_sort, key=lambda v: v.cost)
    for v in sorted_vehicles:
        print(v)

    # Measure and visualize performance
    measure_performance()
