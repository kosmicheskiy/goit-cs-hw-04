import os
import threading

# Функція для пошуку ключових слів у файлі
def search_keywords_in_file(file_path, keywords):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            keyword_count = sum(content.lower().count(keyword.lower()) for keyword in keywords)
            return keyword_count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0

def main():
    # Задані ключові слова
    keywords = ['python', 'threading', 'code', 'example']

    # Шляхи до файлів, які ми хочемо обробити
    file_paths = [
        'file1.txt',
        'file2.txt',
        'file3.txt',
        # Додайте інші файли сюди
    ]

    # Створюємо список потоків
    threads = []
    results = {}

    # Створюємо та запускаємо потоки
    for file_path in file_paths:
        thread = threading.Thread(target=lambda: results.update({file_path: search_keywords_in_file(file_path, keywords)}))
        thread.start()
        threads.append(thread)

    # Очікуємо завершення всіх потоків
    for thread in threads:
        thread.join()

    # Виводимо результати
    for file_path, keyword_count in results.items():
        print(f"File '{file_path}': {keyword_count} occurrences of keywords.")

if __name__ == "__main__":
    main()
