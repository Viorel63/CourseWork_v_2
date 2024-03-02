import pytest
from utils.scripts import get_transactions, sort_transactions, five_items, time_correct, get_from


@pytest.fixture
def example_data():
    return [
        {"state": "EXECUTED", "date": "2024-02-20T08:00:00", "description": "Transaction 1", "from": "Sender 1"},
        {"state": "EXECUTED", "date": "2024-02-21T09:00:00", "description": "Transaction 2", "from": "Sender 2"},
        {"state": "PENDING", "date": "2024-02-22T10:00:00", "description": "Transaction 3", "from": "Sender 3"},
        {"state": "EXECUTED", "date": "2024-02-23T11:00:00", "description": "Transaction 4", "from": "Sender 4"},
        {"state": "EXECUTED", "date": "2024-02-24T12:00:00", "description": "Transaction 5", "from": "Sender 5"},
        {"state": "EXECUTED", "date": "2024-02-25T13:00:00", "description": "Transaction 6", "from": "Sender 6"},
    ]


def test_get_transactions(example_data):
    transactions = get_transactions(example_data)
    assert len(transactions) == 5
    assert all(transaction['state'] == 'EXECUTED' for transaction in transactions)


def test_sort_transactions(example_data):
    sorted_transactions = sort_transactions(example_data)
    assert sorted_transactions == [
        {"state": "EXECUTED", "date": "2024-02-25T13:00:00", "description": "Transaction 6", "from": "Sender 6"},
        {"state": "EXECUTED", "date": "2024-02-24T12:00:00", "description": "Transaction 5", "from": "Sender 5"},
        {"state": "EXECUTED", "date": "2024-02-23T11:00:00", "description": "Transaction 4", "from": "Sender 4"},
        {"state": "EXECUTED", "date": "2024-02-21T09:00:00", "description": "Transaction 2", "from": "Sender 2"},
        {"state": "EXECUTED", "date": "2024-02-20T08:00:00", "description": "Transaction 1", "from": "Sender 1"},
        {"state": "PENDING", "date": "2024-02-22T10:00:00", "description": "Transaction 3", "from": "Sender 3"},
    ]


def test_five_items():
    sorted_transactions = [
        {"date": "2024-02-25T13:00:00", "description": "Transaction 6"},
        {"date": "2024-02-24T12:00:00", "description": "Transaction 5"},
        {"date": "2024-02-23T11:00:00", "description": "Transaction 4"},
        {"date": "2024-02-21T09:00:00", "description": "Transaction 2"},
        {"date": "2024-02-20T08:00:00", "description": "Transaction 1"},
    ]
    assert five_items(sorted_transactions) == sorted_transactions[:5]


def test_time_correct():
    assert time_correct("2024-02-20T08:00:00") == "20-02-2024"


def test_get_from():
    assert get_from({"description": "Test", "from": "John Doe"}) == "John  ** **** Doe"
    assert get_from({"description": "Открытие вклада"}) == ""
