from solution import merge_customer_data

# Normal cases
def test_interleaving():
    a = [101, 104, 107, 0, 0, 0]
    merge_customer_data(a, 3, [102, 105, 108], 3)
    assert a == [101, 102, 104, 105, 107, 108]

def test_all_second_smaller():
    a = [105, 106, 107, 0, 0, 0]
    merge_customer_data(a, 3, [101, 102, 103], 3)
    assert a == [101, 102, 103, 105, 106, 107]

def test_duplicates():
    a = [101, 103, 103, 0, 0]
    merge_customer_data(a, 3, [103, 104], 2)
    assert a == [101, 103, 103, 103, 104]

# Edge cases
def test_n_zero():
    a = [103]
    merge_customer_data(a, 1, [], 0)
    assert a == [103]

def test_m_zero():
    a = [0, 0, 0]
    merge_customer_data(a, 0, [101, 102, 103], 3)
    assert a == [101, 102, 103]

def test_single_elements():
    a = [101, 0]
    merge_customer_data(a, 1, [102], 1)
    assert a == [101, 102]
