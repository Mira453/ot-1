import random

def shell_Sort(array):
    step = int(len(array)/2.2)
    if step < 1:
        step = 1
    
    comparisons = 0  # Лічильник порівнянь
    swaps = 0  # Лічильник перестановок
    
    while step > 0:
        for i in range(step, len(array)):
            temp = array[i]
            j = i
            while j >= step:
                comparisons += 1  # Лічимо кожне порівняння
                if array[j-step] > temp:
                    array[j] = array[j - step]
                    j -= step
                    swaps += 1  # Лічимо перестановку
                else:
                    break  # Виходимо з циклу, якщо подальші перестановки не потрібні
            array[j] = temp
        step = int(step/2.2)
    
    return array, comparisons, swaps

def generate_test_arrays(size):
    random_array = random.sample(range(1, size * 2), size)  # Випадковий масив
    sorted_array = list(range(1, size + 1))  # Відсортований масив
    reversed_array = list(range(size, 0, -1))  # Зворотно відсортований масив
    partially_sorted = sorted_array[:size//2] + random.sample(range(1, size * 2), size//2)  # Частково впорядкований
    
    return {
        "Випадковий масив": random_array,
        "Відсортований масив": sorted_array,
        "Зворотно відсортований масив": reversed_array,
        "Частково впорядкований масив": partially_sorted,
    }

test_cases = generate_test_arrays(10)

for case_name, test_array in test_cases.items():
    print(f"\n{case_name} перед сортуванням:")
    print(test_array)
    
    sorted_array, total_comparisons, total_swaps = shell_Sort(test_array[:])
    
    print(f"{case_name} після сортування:")
    print(sorted_array)
    print(f"Кількість порівнянь: {total_comparisons}")
    print(f"Кількість перестановок: {total_swaps}\n")
