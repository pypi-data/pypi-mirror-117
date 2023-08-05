"""
Main CLI entrypoint.
"""
import sys


def print_info() -> None:
    """
    Print package info to stdout.
    """
    print(
        "Type annotations for boto3.MediaPackage 1.18.25\n"
        "Version:         1.18.25\n"
        "Builder version: 5.1.0\n"
        "Docs:            https://pypi.org/project/mypy-boto3-mediapackage/\n"
        "Boto3 docs:      https://boto3.amazonaws.com/v1/documentation/api/1.18.25/reference/services/mediapackage.html#MediaPackage\n"
        "Other services:  https://pypi.org/project/boto3-stubs/\n"
        "Changelog:       https://github.com/vemel/mypy_boto3_builder/releases"
    )


def print_version() -> None:
    """
    Print package version to stdout.
    """
    print("1.18.25")


def main() -> None:
    """
    Main CLI entrypoint.
    """
    if "--version" in sys.argv:
        return print_version()
    print_info()


if __name__ == "__main__":
    main()
