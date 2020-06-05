# #шаг 8
# def test_input_text(expected_result, actual_result):
#     # ваша реализация, напишите assert и сообщение об ошибке
#     a = expected_result
#     b = actual_result
#     assert expected_result == actual_result , f'expected {a}, got {b}'
#
#
# a = 1
# b = 2
#
# test_input_text(a, b)


# шаг 9

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    a = full_string
    b = substring
    assert substring in full_string, f"expected '{b}' to be substring of '{a}'"

a = '1'
b = '13'

test_substring(a, b)