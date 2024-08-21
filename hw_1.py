def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r') as file:
            for line in file:
                salary = line.strip().split(',')
                try:
                    salary = float(salary[-1])
                    total += salary
                    count += 1
                except ValueError:
                    pass
        average_salary = total / count if count > 0 else 0
        return total, average_salary
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None, None

# Приклад використання функції:
total, average = total_salary('salaries.txt')
print(f"Загальна сума заробітних плат: {total}")
print(f"Середня заробітна плата: {average}")
