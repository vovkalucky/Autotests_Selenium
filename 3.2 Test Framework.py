def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
#test_input_text(11,15)

def test_substring(full_string, substring):
    assert str(substring) in str(full_string), f"expected '{substring}' to be substring of '{full_string}'"
#test_substring('fulltext', 'some_value')
test_substring(1,1)
