from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class AppConfig:
    pass

def load_config(data: dict) -> AppConfig:
    pass

class Stack(Generic[T]):
    pass


if __name__ == "__main__":
    # AppConfig
    config = load_config({"host": "localhost", "port": 8080, "debug": True, "tags": ["web"]})
    print(config)

    # Stack
    s: Stack[int] = Stack()
    s.push(1)
    s.push(2)
    print(s.peek())
    print(s.pop())
    print(s.is_empty())
