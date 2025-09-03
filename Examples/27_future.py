from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from people import Person

def create_message(person: Person | None = None) -> str: ...