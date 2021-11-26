from abc import ABC, abstractmethod

from utils.patterns import Singleton


class DatabaseGateway(ABC, Singleton):
    @abstractmethod
    def fetch_user_info(
        self, email: str, include_salary: bool, include_bonus: bool
    ) -> dict:
        pass
