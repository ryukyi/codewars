"""Problem Statement: Describe how you would design a simple BankAccount class in Python that encapsulates the account details and
operations such as depositing money and withdrawing money.  Ensure that the balance is not directly accessible but through methods.
Discuss the benefits of this approach in the context of a banking application."""

from typing import List
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime, timezone

from loguru import logger


class BaseBankAccountException(Exception):
    pass


class DepositNotPositive(BaseBankAccountException):
    """Deposit must be positive"""


class WithdrawalNotPositive(BaseBankAccountException):
    """Withdrawal must be positive"""


class InsufficientFunds(BaseBankAccountException):
    """Must have more funds than requested withdraw amount"""


class AccountHistoryData(BaseModel):
    recordGuid: str
    time: datetime
    transaction_type: str
    amount: float
    balance_after: float


class AccountHistory:
    def __init__(self) -> None:
        self._history = []

    @property
    def history(self):
        return self._history

    def add_record(
        self, amount: float, transaction_type: str, balance_after: float
    ) -> None:
        record_guid = str(uuid4())
        time_now = datetime.now(timezone.utc)
        record = AccountHistoryData(
            recordGuid=record_guid,
            time=time_now,
            transaction_type=transaction_type,
            amount=amount,
            balance_after=balance_after,
        )
        self._history.append(record)
        logger.info(f"GUID: {record_guid}")

    def get_records(self) -> List:
        return self._history


class BankAccount:
    def __init__(self) -> None:
        self._balance: float = 0
        self._account_history = AccountHistory()

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def account_history(self) -> AccountHistory:
        return self._account_history

    def deposit(self, money: float) -> None:
        if money <= 0:
            raise DepositNotPositive(
                f"{money} was attempted to be deposited but deposit must be a positive value"
            )
        self._balance += money
        self._account_history.add_record(
            amount=money, transaction_type="deposit", balance_after=self._balance
        )

    def withdraw(self, money: float) -> None:
        if money <= 0:
            raise WithdrawalNotPositive(
                f"{money} was attempted to be withdrawn but withdrawal must be a positive value"
            )
        elif money > self._balance:
            raise (
                InsufficientFunds(
                    f"{money} was attempted to be withdrawn but you don't have enough funds"
                )
            )
        self._balance -= money
        self._account_history.add_record(
            amount=money, transaction_type="withdrawal", balance_after=self._balance
        )


if __name__ == "__main__":
    b = BankAccount()
    b.deposit(1000)
    b.withdraw(200)
    logger.debug(b.balance)
    logger.debug(b.account_history.get_records())
    b.withdraw(2000)
