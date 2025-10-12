"""
Problem 2: Dictionary Operations and Nested Structures
Practice working with Python dictionaries - creating, accessing, modifying, and nesting them.
"""


def create_student_record(name, age, major, gpa):
    """Create a student record as a dictionary."""
    return {
        "name": name,
        "age": age,
        "major": major,
        "gpa": gpa
    }


def get_value_safely(dictionary, key, default=None):
    """Get a value from a dictionary safely, returning default if key doesn't exist."""
    return dictionary.get(key, default)


def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries. If keys conflict, dict2's values take precedence."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def count_word_frequency(text):
    """Count the frequency of each word in a text string (ignore punctuation, case insensitive)."""
    import string
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, "")
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def invert_dictionary(dictionary):
    """Invert a dictionary (swap keys and values)."""
    return {v: k for k, v in dictionary.items()}


def filter_dictionary(dictionary, keys_to_keep):
    """Create a new dictionary with only the specified keys."""
    return {k: dictionary[k] for k in keys_to_keep if k in dictionary}


def group_by_first_letter(words):
    """Group words by their first letter."""
    grouped = {}
    for word in words:
        if not word:
            continue
        first = word[0]
        grouped.setdefault(first, []).append(word)
    return grouped


def calculate_grades_average(students):
    """Calculate the average grade for each student."""
    averages = {}
    for name, grades in students.items():
        if grades:
            avg = round(sum(grades) / len(grades), 2)
            averages[name] = avg
    return averages


def nested_dict_access(data, keys):
    """Access a nested dictionary using a list of keys. Return None if missing."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current


# --- Tests ---
if __name__ == "__main__":
    print("Testing Dictionary Operations...")
    print("-" * 50)

    # Test create_student_record
    result = create_student_record("Alice", 20, "CS", 3.8)
    assert result == {'name': 'Alice', 'age': 20, 'major': 'CS', 'gpa': 3.8}
    print("✓ create_student_record passed")

    # Test get_value_safely
    d = {'a': 1, 'b': 2}
    assert get_value_safely(d, 'a') == 1
    assert get_value_safely(d, 'c', 'Not found') == 'Not found'
    print("✓ get_value_safely passed")

    # Test merge_dictionaries
    result = merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    assert result == {'a': 1, 'b': 3, 'c': 4}
    print("✓ merge_dictionaries passed")

    # Test count_word_frequency
    result = count_word_frequency("hello world hello")
    assert result == {'hello': 2, 'world': 1}
    print("✓ count_word_frequency passed")

    # Test invert_dictionary
    result = invert_dictionary({'a': 1, 'b': 2, 'c': 3})
    assert result == {1: 'a', 2: 'b', 3: 'c'}
    print("✓ invert_dictionary passed")

    # Test filter_dictionary
    result = filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
    assert result == {'a': 1, 'c': 3}
    print("✓ filter_dictionary passed")

    # Test group_by_first_letter
    result = group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
    assert result == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    print("✓ group_by_first_letter passed")

    # Test calculate_grades_average
    result = calculate_grades_average({
        'Alice': [90, 85, 88],
        'Bob': [75, 80, 78]
    })
    assert result == {'Alice': 87.67, 'Bob': 77.67}
    print("✓ calculate_grades_average passed")

    # Test nested_dict_access
    data = {'a': {'b': {'c': 123}}}
    assert nested_dict_access(data, ['a', 'b', 'c']) == 123
    assert nested_dict_access(data, ['a', 'x']) is None
    print("✓ nested_dict_access passed")

    print("=" * 50)
    print("All tests passed! Excellent work!")
    
