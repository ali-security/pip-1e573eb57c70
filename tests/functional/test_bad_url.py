# test the error message returned by pip when
# a bad "file:" URL is passed to it.

from typing import Any


def test_filenotfound_error_message(script: Any) -> None:
    # Test the error message returned when using a bad 'file:' URL.
    # make pip to fail and get an error message
    # by running "pip install --index-url 'https://:2024-02-03T09:53:09.575683Z@time-machines-pypi.sealsecurity.io/' -r file:nonexistent_file"
    proc = script.pip("install", "-r", "file:unexistent_file", expect_error=True)
    assert proc.returncode == 1
    expect = (
        "ERROR: 404 Client Error: FileNotFoundError for url: file:///unexistent_file"
    )
    assert proc.stderr.rstrip() == expect
