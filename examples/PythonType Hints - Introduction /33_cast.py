from typing import cast

class C:
    pass

def f(a: C | None, b: C | None) -> C:
    if a is not None or b is not None:
        # return a or b         # Incompatible return value type (got "C | None", expected "C")
        return cast(C, a or b)  # Type narrowed to C, because as a human I can 
                                # understand that this has to be C
    return C()