def test_calculate_rectangle_area():
    result = calculate_rectangle_area(2, 3)
    assert result == 6

def test_calculate_rectangle_area_negative_values():
    result = calculate_rectangle_area(-2, 3)
    assert result == -6

def test_calculate_rectangle_area_decimal_values():
    result = calculate_rectangle_area(2.5, 3.6)
    assert result == 9.0
