import math
def students_study(time: int, coffee_needed: bool) -> bool:
    if time <= 4 and time >= 1:
        return(False)
    elif time <= 24 and time >= 18:
        return(True)
    elif time <= 17 and time >= 5 and coffee_needed is True:
        return(True)
    else:
        return(False)
    pass

def lottery(a: int, b: int, c: int) -> int:
    if a == b == c == 5:
        return(10)
    elif a == b == c:
        return(5)
    elif b != a and c != a:
        return(1)
    else:
        return(0)
    pass

def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    if (big_baskets * 5 + small_baskets >= ordered_amount) and small_baskets >= ordered_amount%5:
        if big_baskets < math.floor(ordered_amount/5):
            return(ordered_amount-big_baskets*5)
        else:
            return(ordered_amount%5)
    else:
        return(-1)
    pass

def test_students_study_night_coffee_false():
    assert students_study(3, False) is False

def test_students_study_day_coffee_true():
    assert students_study(6, True) is True

def test_students_study_day_coffee_false():
    assert students_study(7, False) is False

def test_students_study_evening_coffee_false():
    assert students_study(20, False) is True

def test_students_study_evening_coffee_true():
    assert students_study(20, True) is True

def test_students_study_evening_edge_case_coffee_true():
    assert students_study(18, True) is True
    assert students_study(24, True) is True

def test_students_study_evening_edge_case_coffee_false():
    assert students_study(24, False) is True
    assert students_study(18, False) is True

def test_students_study_night_edge_case_coffee_true():
    assert students_study(1, True) is False
    assert students_study(4, True) is False

def test_students_study_night_edge_case_coffee_false():
    assert students_study(4, False) is False
    assert students_study(1, False) is False

def test_students_study_day_edge_case_coffee_true():
    assert students_study(5, True) is True
    assert students_study(17, True) is True

def test_students_study_day_edge_case_coffee_false():
    assert students_study(5, False) is False
    assert students_study(17, False) is False

def test_lottery_all_fives():
    assert lottery(5,5,5) == 10

def test_lottery_all_same_positive():
    assert lottery(3,3,3) == 5

def test_lottery_all_same_negative():
    assert lottery(-1,-1,-1) == 5

def test_lottery_all_same_zero():
    assert lottery(0,0,0) == 5

def test_lottery_a_b_same_c_diff():
    assert lottery(2,2,1) == 0

def test_lottery_a_c_same_b_diff():
    assert lottery(2,1,2) == 0

def test_lottery_b_c_same_a_diff():
    assert lottery(1,2,2) == 1

def test_lottery_all_diff():
    assert lottery(1,2,3) == 1

def test_fruit_order_all_zero():
    assert fruit_order(0,0,0) == 0

def test_fruit_order_zero_amount_zero_small():
    assert fruit_order(0,1,0) == 0

def test_fruit_order_zero_amount_zero_big():
    assert fruit_order(1,0,0) == 0

def test_fruit_order_zero_amount_others_not_zero():
    assert fruit_order(1,1,0) == 0

def test_fruit_order_only_big_exact_match():
    assert fruit_order(0,1,5) == 0

def test_fruit_order__only_big_not_enough_but_multiple_of_5():
    assert fruit_order(0,1,10) == -1

def test_fruit_order__only_big_not_enough():
    assert fruit_order(0,1,7) == -1

def test_fruit_order_only_big_more_than_required_match():
    assert fruit_order(0,2,5) == 0

def test_fruit_order_only_big_more_than_required_no_match():
    assert fruit_order(0,2,6) == -1

def test_fruit_order_only_small_match_more_than_5_smalls():
    assert fruit_order(7,0,7) == 7

def test_fruit_order_only_small_not_enough_more_then_5_smalls():
    assert fruit_order(7,0,9) == -1

def test_fruit_order__only_small_exact_match():
    assert fruit_order(1,0,1) == 1

def test_fruit_order__only_small_not_enough():
    assert fruit_order(1,0,2) == -1

def test_fruit_order__only_small_more_than_required():
    assert fruit_order(7,0,5) == 5

def test_fruit_order_match_with_more_than_5_smalls():
    assert fruit_order(7,3,21) == 6

def test_fruit_order__all_positive_exact_match():
    assert  fruit_order(5,1,6) == 1

def test_fruit_order__use_all_smalls_some_bigs():
    assert fruit_order(3,7,13) == 3

def test_fruit_order__use_some_smalls_all_bigs():
    assert fruit_order(12,1,7) == 2

def test_fruit_order__use_some_smalls_some_bigs():
    assert fruit_order(7,7,7) == 2

def test_fruit_order__not_enough():
    assert fruit_order(1,1,7) == -1

def test_fruit_order__enough_bigs_not_enough_smalls():
    assert fruit_order(1,7,7) == -1

def test_fruit_order__not_enough_with_more_than_5_smalls():
    assert fruit_order(7,3,23) == -1

def test_fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    assert fruit_order(2,65,254) == -1

def test_fruit_order__match_large_numbers():
    assert fruit_order(1740,923,6321) == 1706

def test_fruit_order__all_positive_exact_match():
    assert  fruit_order()

print(fruit_order(1740,923,6321))