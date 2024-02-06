def get_cats_info(cats_hw4):
    cats_info = []
    try:
        with open(cats_hw4, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat_info = {"id": id, "name": name, "age": age}
                cats_info.append(cat_info)
    except FileNotFoundError:
        print(f"Файл не знайдено: {cats_hw4}")
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")
    return cats_info

cats_info = get_cats_info("C:/Projects/cats_hw4.txt")
print(cats_info)
