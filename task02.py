import os
import multiprocessing

def search_keywords_in_file(file_path, keywords, result_queue):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            keyword_count = sum(content.lower().count(keyword.lower()) for keyword in keywords)
            result_queue.put((file_path, keyword_count))
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def main():
    # Задані ключові слова
    keywords = ['python', 'multiprocessing', 'code', 'example']

    # Шляхи до файлів, які ми хочемо обробити
    file_paths = [
        'file1.txt',
        'file2.txt',
        'file3.txt',
        # Додайте інші файли сюди
    ]

    # Створюємо чергу для зберігання результатів
    result_queue = multiprocessing.Queue()

    # Створюємо та запускаємо процеси
    processes = []
    for file_path in file_paths:
        process = multiprocessing.Process(target=search_keywords_in_file, args=(file_path, keywords, result_queue))
        process.start()
        processes.append(process)

    # Очікуємо завершення всіх процесів
    for process in processes:
        process.join()

    # Виводимо результати
    while not result_queue.empty():
        file_path, keyword_count = result_queue.get()
        print(f"File '{file_path}': {keyword_count} occurrences of keywords.")

if __name__ == "__main__":
    main()
