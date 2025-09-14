import ipaddress
import sys

from pathlib import Path

__author__ = "Adam Walkiewicz"
__version__ = "0.0.1"


HELP = f"""\
Usage: {Path(__file__).name} [port] [--host] [--help] [--version]

Positional arguments:
    port\t\tRun server on this port, default 8080.

Options:
    --help\t\tPrint this help message.
    --host\t\tRun server on this address, default to 127.0.0.1.
    --version\t\tPrint program version and exit.

Author:
    {__author__}

License:
    MIT 2025 {__author__}
"""

VALID_FLAGS = {"--help", "-h", "--version", "-v", "--host"}


class Server:
    """Fake Server class, it does nothing.

    Attributes:
        HOST (str): Host to which server is bind.
        PORT (int): Port on which server runs.
    """

    HOST = "127.0.0.1"
    PORT = 8080

    def __init__(self, host: str | None = None, port: int | None = None) -> None:
        """Initialize Server with host and port.

        Args:
            host: Host to which server is bind, defaults to None.
            port: Port on which server runs, defaults to None.
        """

        self.host = host or Server.HOST
        self.port = port or Server.PORT

    def run(self) -> None:
        """Run the server"""

        print(f"Running on: {self.host}:{self.port}")
        input("Press any key to exit")


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print(HELP)
        sys.exit(0)

    if "--version" in sys.argv or "-v" in sys.argv:
        print(__version__)
        sys.exit(0)

    flags = {flag for flag in sys.argv if flag.startswith("-")}
    invalid_flags = flags - VALID_FLAGS
    if invalid_flags:
        print(f"Following flags are not valid: {invalid_flags}", file=sys.stderr)
        sys.exit(2)

    arguments = sys.argv[::]
    host: str | None = None
    if "--host" in sys.argv:
        host_index = sys.argv.index("--host")
        try:
            host = sys.argv[host_index + 1]
            ipaddress.IPv4Address(host)
            arguments.remove(host)
            arguments.remove("--host")
        except IndexError:
            print("Missing host argument", file=sys.stderr)
            sys.exit(2)
        except ipaddress.AddressValueError:
            print("Provided host '{host}' is not a valid IPv4 address", file=sys.stderr)
            sys.exit(2)

    try:
        port = int(arguments[1])
    except IndexError:
        print("Missing port", file=sys.stderr)
        sys.exit(2)
    except ValueError:
        print("Port must be an integer", file=sys.stderr)
        sys.exit(2)

    server = Server(host, port)
    server.run()
