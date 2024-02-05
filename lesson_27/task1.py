import multiprocessing

def process_data(data_chunk):
    # Функція обробки даних для кожного процесу
    result = []
    for item in data_chunk:
        # Ваша обробка даних тут
        processed_item = item * 2  # Приклад: подвоєння значення
        result.append(processed_item)
    return result

def main():
    # Ваш великий набір даних
    big_data = list(range(1000000))

    # Розділіть дані на кілька частин для обробки різними процесами
    chunk_size = len(big_data) // multiprocessing.cpu_count()
    data_chunks = [big_data[i:i + chunk_size] for i in range(0, len(big_data), chunk_size)]

    # Створіть пул процесів та розпочніть обробку
    with multiprocessing.Pool() as pool:
        results = pool.map(process_data, data_chunks)

    # Об'єднайте результати
    final_result = []
    for result in results:
        final_result.extend(result)

    # Ваші дії з фінальним результатом тут
    print(f"Приклад обробки для перших 5 елементів: {final_result[:5]}")
    print(f"Загальна кількість оброблених елементів: {len(final_result)}")

if __name__ == "__main__":
    main()
