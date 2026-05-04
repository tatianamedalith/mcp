

from abc import ABC, abstractmethod

class EmailProvider(ABC):
    @abstractmethod
    def send(
        self,
        to: list[str],
        subject: str,
        html: str,
        cc: list[str],
        bcc: list[str],
        attachments: list[str],
    ) -> str: ...
