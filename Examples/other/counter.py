class Counter:
    def __init__(self, start: int = 0, step: int = 1) -> None:
        self.value = start
        self.step = step

    def __call__(self) -> int:
        self.value += self.step
        return self.value

if __name__ == "__main__":
    counter = Counter(step=10)
    print(counter())
    print(counter())
    print(counter())
    print(counter())


