import os

def rename_images(file_extension):
    """
    Переименовывает все изображения в текущей папке в формате 1, 2, 3 и так далее.
    
    :param file_extension: Расширение файлов, которые нужно нумеровать (например, 'jpg').
    """
    try:
        # Получаем список файлов с указанным расширением
        files = [f for f in os.listdir('.') if f.lower().endswith(f".{file_extension.lower()}")]

        # Сортируем файлы, чтобы они переименовывались последовательно
        files.sort()

        # Нумеруем файлы и переименовываем
        for i, file_name in enumerate(files, start=1):
            old_path = os.path.join('.', file_name)
            new_name = f"{i}.{file_extension}"
            new_path = os.path.join('.', new_name)

            os.rename(old_path, new_path)
            print(f"Переименовано: {file_name} -> {new_name}")

        print("Все изображения успешно переименованы!")

    except Exception as e:
        print(f"Ошибка: {e}")

# Пример использования
if __name__ == "__main__":
    extension = input("Введите расширение изображений (например, jpg, png): ")
    rename_images(extension)
