def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                # Видаляємо пробіли з кінців рядка і розділяємо його на частини
                cat_id, name, age = line.strip().split(',')
                # Додаємо словник з інформацією про кота до списку
                cats_info.append({
                    'id': cat_id,
                    'name': name,
                    'age': int(age)
                })
            return cats_info
    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except ValueError:
        print("Помилка у форматі даних. Перевірте, чи всі рядки мають правильний формат 'ідентифікатор,ім'я,вік'.")
        return []
    except Exception as e:
        print(f"Виникла несподівана помилка: {e}")
        return []

path_to_file = ('get_cats_info.txt')
cats_list = get_cats_info(path_to_file)
for cat in cats_list:
    print(cat)