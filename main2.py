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
            while j >= step and array[j-step] > temp:
                comparisons += 1  # Лічимо порівняння
                array[j] = array[j - step]
                j -= step
                swaps += 1  # Лічимо перестановку
            array[j] = temp
            if j != i:
                swaps += 1  # Лічимо ще одну перестановку, якщо елемент змінив позицію
        step = int(step/2.2)
    
    return array, comparisons, swaps

array_100 = random.sample(range(1, 1001), 100)

print("Масив перед сортуванням:")
print(array_100)

# Виконуємо сортування
sorted_array, total_comparisons, total_swaps = shell_Sort(array_100)

print("\nМасив після сортування:")
print(sorted_array)

# Вивід статистики
print(f"Кількість порівнянь: {total_comparisons}")
print(f"Кількість перестановок: {total_swaps}")
