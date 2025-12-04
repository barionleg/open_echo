from argparse import ArgumentParser

from open_echo.desktop import run_desktop
from open_echo.UART_UDP_relay import configure_relay_parser, run_relay
from open_echo.web import run_web


def main():
    parser = ArgumentParser(
        description="Command-line interface for the open_echo package."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    desktop_parser = subparsers.add_parser("desktop", help="Run desktop interface")
    desktop_parser.set_defaults(handler=lambda _: run_desktop())

    web_parser = subparsers.add_parser("web", help="Run web interface")
    web_parser.set_defaults(handler=lambda _: run_web())

    relay_parser = subparsers.add_parser("relay", help="Run UART to UDP relay")
    configure_relay_parser(relay_parser)
    relay_parser.set_defaults(handler=run_relay)

    args = parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
