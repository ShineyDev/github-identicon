from typing import Any, Iterator, List, Tuple, Type, TypeVar


_I = TypeVar("_I", bound=Identicon)

class Identicon():
    @classmethod
    def from_identifier(cls: Type[_I], identifier: int) -> _I: ...
    
    def get_background(self) -> Tuple[int, int, int]: ...
    def get_foreground(self) -> Tuple[int, int, int]: ...
    def generate_bits(self) -> Iterator[bool]: ...
    def generate_list(self) -> List[bool]: ...
    def generate_matrix(self) -> List[List[bool]]: ...
    def generate_image(self) -> Any: ...
