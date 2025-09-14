import abc
import typing

class Config(typing.Protocol):
    name: str


class Platform(abc.ABC):
    config = Config

    def __init_subclass__(
            cls, /, config: type[Config], **kwargs: typing.Any
        ) -> None:
        super().__init_subclass__(**kwargs)
        cls.config = config

    @abc.abstractmethod
    def get_name(self) -> str:
        ...


class SonyConfig:
    name = "Sony"


class Sony(Platform, config=SonyConfig):
    def get_name(self) -> str:
        return self.config.name


if __name__ == "__main__":
    sony = Sony()
    name = sony.get_name()
    print(name)
