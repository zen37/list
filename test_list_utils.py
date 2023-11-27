import pytest
from list_utils import remove_duplicates

def test_remove_duplicates():
    # Test case 1: Numbers
    input_array1 = [1, 2, 3, 2, 4, 5, 1]
    expected_output1 = [1, 2, 3, 4, 5]
    result1 = remove_duplicates(input_array1)
    assert result1 == expected_output1, f"For input {input_array1}, expected {expected_output1}, but got {result1}"
    print(f"Test case 1 - Numbers: {input_array1}, Result: {result1}")

    # Test case 2: Empty array
    input_array2 = []
    expected_output2 = []
    result2 = remove_duplicates(input_array2)
    assert result2 == expected_output2, f"For input {input_array2}, expected {expected_output2}, but got {result2}"
    print(f"Test case 2 - Empty: {input_array2}, Result: {result2}")

    # Test case 3: Mixed
    input_array3 = [(1, 2), (3, 4), (1, 2), (5, 6), 7, (9, 12, "a"), 7, 8, (9, "a", 12), 8, "X", "x", 23, "X" ]
    expected_output3 = [(1, 2), (3, 4), (5, 6), 7, (9, 12, "a"), 8, (9, "a", 12), "X", "x", 23]
    result3 = remove_duplicates(input_array3)
    assert result3 == expected_output3, f"For input {input_array3}, expected {expected_output3}, but got {result3}"
    print(f"Test case 3 - Mixed: {input_array3}, Result: {result3}")

    # Test case 4: Strings
    input_array4 = ['apple', 'orange', 'banana', 'apple', 'grape', 'orange', 'kiwi', 'banana']
    expected_output4 = ['apple', 'orange', 'banana', 'grape', 'kiwi']
    result4 = remove_duplicates(input_array4)
    assert result4 == expected_output4, f"For input {input_array4}, expected {expected_output4}, but got {result4}"
    print(f"Test case 4 - Strings: {input_array4}, Result: {result4}")

    # Test case 5: Unicode
    input_array5 = input_unicode_duplicates = ['😊', '🍣', '你好', 'عربي', 'こんにちは', '🍣', 'مرحبا', '🌏', '🎉', '日本語', '中文', '😄', '🍜', 'عربي', 'hello', 'عربي', 'world', '日本語', '😄', 'python']
    expected_output5 = ['😊', '🍣', '你好', 'عربي', 'こんにちは', 'مرحبا', '🌏', '🎉', '日本語', '中文', '😄', '🍜', 'hello', 'world', 'python']
    result5 = remove_duplicates(input_array5)
    assert result5 == expected_output5, f"For input {input_array5}, expected {expected_output5}, but got {result5}"
    print(f"Test case 5 - Unicode: {input_array5}, Result: {result5}")

    # Add more test cases as needed

@pytest.mark.parametrize("input_array, expected_output", [
    ([1, 2, 3, 2, 4, 5, 1], [1, 2, 3, 4, 5]),
    ([], []),
    ([(1, 2), (3, 4), (1, 2), (5, 6), 7, (9, 12, "a"), 7, 8, (9, "a", 12), 8, "X", "x", 23, "X"], [(1, 2), (3, 4), (5, 6), 7, (9, 12, "a"), 8, (9, "a", 12), "X", "x", 23]),
    (['apple', 'orange', 'banana', 'apple', 'grape', 'orange', 'kiwi', 'banana'], ['apple', 'orange', 'banana', 'grape', 'kiwi']),
    (['😊', '🍣', '你好', 'عربي', 'こんにちは', '🍣', 'مرحبا', '🌏', '🎉', '日本語', '中文', '😄', '🍜', 'عربي', 'hello', 'عربي', 'world', '日本語', '😄', 'python'], ['😊', '🍣', '你好', 'عربي', 'こんにちは', 'مرحبا', '🌏', '🎉', '日本語', '中文', '😄', '🍜', 'hello', 'world', 'python']),
])
def test_remove_duplicates2(input_array, expected_output):
    result = remove_duplicates(input_array)
    assert result == expected_output, f"For input {input_array}, expected {expected_output}, but got {result}"
    print(f"Test case - Input: {input_array}, Result: {result}")