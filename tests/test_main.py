from unittest.mock import patch
from io import StringIO
import pytest
from scripts import main


@pytest.fixture
def mock_data():
    return '{"transactions": [{"date": "2024-02-20", "description": "Transaction 1", "amount": 100}, {"date": "2024-02-21", "description": "Transaction 2", "amount": 200}]}'


@patch('builtins.open')
def test_main_output(mock_open, mock_data, capsys):
    mock_open.return_value = StringIO(mock_data)
    expected_output = "20-Feb-2024 Transaction 1\nNone {}\n{'date': '2024-02-20', 'description': 'Transaction 1', 'amount': 100}\n\n21-Feb-2024 Transaction 2\nNone {}\n{'date': '2024-02-21', 'description': 'Transaction 2', 'amount': 200}\n\n"

    main()

    captured = capsys.readouterr()
    assert captured.out == expected_output


if __name__ == '__main__':
    pytest.main([__file__])
