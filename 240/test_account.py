from account import Account
import pytest

# write your pytest functions below, they need to start with test_

def test_default():
    test_account = Account("Bob")
    assert test_account.owner == "Bob"
    assert test_account.amount == 0
    assert str(test_account) == "Account of Bob with starting amount: 0"
    assert repr(test_account) == "Account('Bob', 0)"
    assert len(test_account) == 0
    assert test_account.balance == 0

def test_starting_amount():
    test_account = Account("Alice", 30)
    assert test_account.owner == "Alice"
    assert test_account.amount == 30
    assert str(test_account) == "Account of Alice with starting amount: 30"
    assert len(test_account) == 0
    assert test_account.balance == 30

def test_non_integer_transaction():
    test_account = Account("Charlie")
    with pytest.raises(ValueError, match="please use int for amount"):
        test_account.add_transaction(0.25)
    assert len(test_account) == 0
    assert test_account.balance == 0

def test_single_transaction():
    test_account = Account("Dan")
    test_account.add_transaction(30)
    assert len(test_account) == 1
    assert test_account.balance == 30

def test_transaction_with_starting_balance():
    test_account = Account("Eric", 30)
    test_account.add_transaction(5)
    assert len(test_account) == 1
    assert test_account.balance == 35

def test_multi_trans_with_starting_balance():
    test_account = Account("Fred", 25)
    test_account.add_transaction(5)
    test_account.add_transaction(7)
    assert len(test_account) == 2
    assert test_account.balance == 37
    assert test_account[0] == 5
    assert test_account[1] == 7

def test_ordering():
    first_account = Account("George", 25)
    second_account = Account("Harold", 15)
    assert first_account > second_account
    assert second_account < first_account
    first_account.add_transaction(5)
    second_account.add_transaction(5)
    assert first_account > second_account
    assert second_account < first_account
    second_account.add_transaction(10)
    assert second_account == first_account
    assert not second_account < first_account
    assert not second_account > first_account

def test_combine():
    first_account = Account("George", 25)
    second_account = Account("Harold", 15)
    
    first_account.add_transaction(5)
    second_account.add_transaction(10)
    
    combined_account = first_account + second_account
    assert combined_account.owner == "George&Harold"
    assert combined_account.balance == 55
    assert len(combined_account) == 2