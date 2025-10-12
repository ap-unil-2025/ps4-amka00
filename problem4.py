"""
JSON File Operations: Save, Load, Append, Backup, Stats, Merge, Search
"""

import json
import os

# -------------------------------
# Core JSON functions
# -------------------------------

def save_to_json(data, filename):
    """Save data to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving to {filename}: {e}")
        return False

def load_from_json(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception:
        return None

# -------------------------------
# Contact-specific functions
# -------------------------------

def save_contacts_to_file(contacts, filename="contacts.json"):
    """Save a list of contacts to a JSON file."""
    return save_to_json(contacts, filename)

def load_contacts_from_file(filename="contacts.json"):
    """Load contacts from a JSON file."""
    data = load_from_json(filename)
    if data is None:
        return []
    return data

def append_contact_to_file(contact, filename="contacts.json"):
    """Add a new contact to the file."""
    contacts = load_contacts_from_file(filename)
    contacts.append(contact)
    return save_contacts_to_file(contacts, filename)

def backup_file(source_filename, backup_filename):
    """Create a backup copy of a file."""
    data = load_from_json(source_filename)
    if data is None:
        return False
    return save_to_json(data, backup_filename)

def get_file_stats(filename):
    """Get statistics about a JSON file."""
    stats = {'exists': os.path.exists(filename)}
    if not stats['exists']:
        return stats

    stats['size_bytes'] = os.path.getsize(filename)
    data = load_from_json(filename)
    if isinstance(data, list):
        stats['type'] = 'list'
        stats['count'] = len(data)
    elif isinstance(data, dict):
        stats['type'] = 'dict'
        stats['count'] = len(data.keys())
    else:
        stats['type'] = 'other'
        stats['count'] = 0
    return stats

def merge_json_files(file1, file2, output_file):
    """Merge two JSON files containing lists."""
    list1 = load_from_json(file1)
    list2 = load_from_json(file2)
    if not isinstance(list1, list) or not isinstance(list2, list):
        return False
    combined = list1 + list2
    return save_to_json(combined, output_file)

def search_json_file(filename, key, value):
    """Search JSON file for dicts matching key-value."""
    data = load_from_json(filename)
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict) and item.get(key) == value]

# -------------------------------
# Test cases
# -------------------------------

if __name__ == "__main__":
    print("Testing JSON File Operations...")
    print("-" * 50)

    # Test 1: save_to_json and load_from_json
    print("Test 1: save_to_json and load_from_json")
    test_data = {'name': 'Alice', 'age': 25, 'city': 'Paris'}
    save_to_json(test_data, 'test_data.json')
    loaded_data = load_from_json('test_data.json')
    print(f"Saved and loaded: {loaded_data}")
    assert loaded_data == test_data
    print("✓ Passed\n")

    # Test 2: save_contacts_to_file and load_contacts_from_file
    print("Test 2: save and load contacts")
    contacts = [
        {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'},
        {'name': 'Bob', 'phone': '555-0002', 'email': 'bob@email.com'}
    ]
    save_contacts_to_file(contacts, 'test_contacts.json')
    loaded_contacts = load_contacts_from_file('test_contacts.json')
    print(f"Loaded {len(loaded_contacts)} contacts")
    assert len(loaded_contacts) == 2
    assert loaded_contacts[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 3: append_contact_to_file
    print("Test 3: append_contact_to_file")
    new_contact = {'name': 'Charlie', 'phone': '555-0003', 'email': 'charlie@email.com'}
    append_contact_to_file(new_contact, 'test_contacts.json')
    contacts = load_contacts_from_file('test_contacts.json')
    print(f"After append: {len(contacts)} contacts")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 4: backup_file
    print("Test 4: backup_file")
    backup_file('test_contacts.json', 'test_contacts_backup.json')
    backup_data = load_from_json('test_contacts_backup.json')
    print(f"Backup created with {len(backup_data)} items")
    assert len(backup_data) == 3
    print("✓ Passed\n")

    # Test 5: get_file_stats
    print("Test 5: get_file_stats")
    stats = get_file_stats('test_contacts.json')
    print(f"File stats: {stats}")
    assert stats['exists'] == True
    assert stats['type'] == 'list'
    assert stats['count'] == 3
    print("✓ Passed\n")

    # Test 6: merge_json_files
    print("Test 6: merge_json_files")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    save_to_json(list1, 'list1.json')
    save_to_json(list2, 'list2.json')
    merge_json_files('list1.json', 'list2.json', 'merged.json')
    merged = load_from_json('merged.json')
    print(f"Merged list: {merged}")
    assert merged == [1, 2, 3, 4, 5, 6]
    print("✓ Passed\n")

    # Test 7: search_json_file
    print("Test 7: search_json_file")
    results = search_json_file('test_contacts.json', 'name', 'Alice')
    print(f"Search results: {results}")
    assert len(results) == 1
    assert results[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Cleanup
    print("Cleaning up test files...")
    for file in ['test_data.json', 'test_contacts.json', 'test_contacts_backup.json',
                 'list1.json', 'list2.json', 'merged.json']:
        if os.path.exists(file):
            os.remove(file)
    print("✓ Cleaned up\n")

    print("=" * 50)
    print("All tests passed! You've mastered JSON file operations!")