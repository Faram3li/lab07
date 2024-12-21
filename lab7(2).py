def find_most_repeating_chars_line(lines):
    max_count = 0
    result_line = ""
    
    for line in lines:
        char_count = max(line.count(char) for char in set(line))
        if char_count > max_count:
            max_count = char_count
            result_line = line
            
    return result_line

n = int(input("Введіть кількість рядків: "))
lines = [input(f"Введіть рядок {i+1}: ") for i in range(n)]
result = find_most_repeating_chars_line(lines)
print("Рядок з найбільшою кількістю однакових символів:", result)
