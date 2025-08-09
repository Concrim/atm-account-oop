import builtins
import pytest
from io import StringIO
from main import Account, SavingAccount  # adjust import as per your folder structure


def mock_inputs(monkeypatch, inputs):
    """Mocks input() calls by returning items from the given list."""
    input_iter = iter(inputs)
    monkeypatch.setattr(builtins, 'input', lambda _: next(input_iter))


# for Account
def test_account_deposit(monkeypatch, capsys):
    mock_inputs(monkeypatch, ["1234"])
    acc = Account("Ali", 100)
    acc.deposit(50)
    captured = capsys.readouterr().out
    assert "Your new balance is $150" in captured

def test_account_withdraw_success(monkeypatch, capsys):
    mock_inputs(monkeypatch, ["1234"])
    acc = Account("Ali", 200)

    # mock password for withdraw check
    mock_inputs(monkeypatch, ["1234"])
    acc.withdraw(50)
    captured = capsys.readouterr().out
    assert "Your new balance is $150" in captured

def test_account_withdraw_insufficient(monkeypatch, capsys):
    mock_inputs(monkeypatch, ["1234"])
    acc = Account("Ali", 50)

    # mock password for withdraw check
    mock_inputs(monkeypatch, ["1234"])
    acc.withdraw(100)
    captured = capsys.readouterr().out
    assert "Your balance is low" in captured

# For Savings Account
def test_add_to_savings_success(monkeypatch, capsys):
    mock_inputs(monkeypatch, ["1234"])
    sa = SavingAccount("Ali", 200)

    # password check + amount to save
    mock_inputs(monkeypatch, ["1234", "50"])
    sa.add_to_savings()

    # check_savings
    mock_inputs(monkeypatch, ["1234"])
    sa.check_savings()
    captured = capsys.readouterr().out
    assert "Your current savings are: $50" in captured

def test_add_to_savings_insufficient(monkeypatch, capsys):
    mock_inputs(monkeypatch, ["1234"])
    sa = SavingAccount("Ali", 100)

    # password check + amount to save (too much)
    mock_inputs(monkeypatch, ["1234", "200"])
    sa.add_to_savings()
    captured = capsys.readouterr().out
    assert "Your balance is insufficient" in captured

def test_interest_and_withdraw_savings(monkeypatch, capsys):
    mock_inputs(monkeypatch, ["1234"])
    sa = SavingAccount("Ali", 200)

    # add some savings first
    mock_inputs(monkeypatch, ["1234", "100"])
    sa.add_to_savings()

    # bank official sets time passed
    mock_inputs(monkeypatch, ["2"])
    sa.inc_time()

    # withdraw savings
    sa.withdraw_savings()
    captured = capsys.readouterr().out
    assert "Withdrawing funds in savings account" in captured
    assert "Withdrawn amount:" in captured
