import random
import time
import numpy as np
import matplotlib.pyplot as plt

def shell_Sort(array):
    start_time = time.time()
    step = int(len(array)/2.2)
    if step < 1:
        step = 1
    
    while step > 0:
        for i in range(step, len(array)):
            temp = array[i]
            j = i
            while j >= step and array[j-step] > temp:
                array[j] = array[j - step]
                j -= step
            array[j] = temp
        step = int(step/2.2)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return execution_time

def generate_data(size, case):
    if case == "sorted":
        array = list(range(1, size + 1))  # Відсортований масив
    elif case == "reversed":
        array = list(range(size, 0, -1))  # Зворотно відсортований масив
    else:
        array = random.sample(range(1, size * 2), size)  # Випадковий масив
    
    return array

sizes = list(range(1000, 50001, 5000))  # Збільшено розміри масивів для гладкішого графіка
sorted_times, reversed_times, random_times = [], [], []
num_trials = 10  # Усереднення для зменшення шуму

for size in sizes:
    for case, time_list in zip(["sorted", "reversed", "random"],
                               [sorted_times, reversed_times, random_times]):
        total_time = 0
        for _ in range(num_trials):
            array = generate_data(size, case)
            total_time += shell_Sort(array)
        avg_time = total_time / num_trials
        time_list.append(avg_time)

plt.figure(figsize=(10, 6))
plt.plot(sizes, sorted_times, label='Відсортований масив', color='green', marker='o', linestyle='-')
plt.plot(sizes, reversed_times, label='Зворотний порядок', color='red', marker='s', linestyle='-')
plt.plot(sizes, random_times, label='Масив з випадковими числами', color='blue', marker='d', linestyle='-')
plt.xlabel('Розмір масиву')
plt.ylabel('Час виконання (секунди)')
plt.ylim(0, max(random_times) * 1.1)  # Автоматичне масштабування Y
plt.title('Залежність часу виконання від розміру масиву')
plt.legend()
plt.grid(True)
plt.show()
