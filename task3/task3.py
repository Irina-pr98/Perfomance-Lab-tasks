import json
import sys

def load_json(file_path):
    """Функция для загрузки JSON данных из файла."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    """Функция для сохранения JSON данных в файл."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def update_values(tests, values):
    """Функция для обновления полей 'value' в тестах на основании значений."""
    id_to_value = {item['id']: item['value'] for item in values['values']}
    
    def update(test):
        if 'values' in test:
            for subtest in test['values']:
                update(subtest)
        if test['id'] in id_to_value:
            test['value'] = id_to_value[test['id']]

    for test in tests['tests']:
        update(test)
    
    return tests

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <tests.json> <values.json> <report.json>")
        sys.exit(1)

    tests_path, values_path, report_path = sys.argv[1], sys.argv[2], sys.argv[3]

    tests = load_json(tests_path)
    values = load_json(values_path)

    updated_tests = update_values(tests, values)
    
    save_json(updated_tests, report_path)