# Analysis of Sorting Algorithms

## Sorting Algorithms Implemented

### 1. Selection Sort
- **Description**: This algorithm repeatedly selects the minimum element from the unsorted portion of the list and places it in the sorted portion.
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Best Use Case**: Useful for small datasets or when memory is a constraint.

### 2. Bubble Sort
- **Description**: This algorithm repeatedly compares adjacent elements and swaps them if they are in the wrong order. It continues until no swaps are required.
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Best Use Case**: Mostly educational; not efficient for large datasets.

### 3. Merge Sort
- **Description**: A divide-and-conquer algorithm that splits the list into halves, recursively sorts each half, and merges them back together in sorted order.
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Best Use Case**: Efficient for large datasets due to its guaranteed O(n log n) performance.

## Experiment Results

### Observations
1. **Selection Sort** and **Bubble Sort** exhibited quadratic growth in runtime as the number of vehicles increased. This makes them inefficient for large datasets.
2. **Merge Sort** demonstrated linearithmic growth, making it much faster for larger datasets.

### Graph
The graph generated during the experiment shows a clear distinction between the performance of the algorithms. Merge Sort significantly outperformed the other two algorithms as the dataset size increased.

## Conclusion
Merge Sort is the most efficient algorithm among the three for sorting the Vehicle objects, especially for larger datasets. Selection Sort and Bubble Sort are more suitable for smaller datasets or educational purposes.
