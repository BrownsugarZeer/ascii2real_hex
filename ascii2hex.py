def convert_hex_to_bin(source_path: str, output_path: str) -> None:
    """
    Converts a file containing ASCII-encoded hexadecimal values to binary format.

    The function reads the source file line by line, converts each line to binary,
    and writes the resulting binary data to the output file.

    Parameters
    ----------
    source_path : str
        The path to the source file.
    output_path : str
        The path to the output file.

    Example
    -------
    >>> with open("test.hex", "w") as f:
    >>>     f.write(":10010000214601360121470136007EFE09D2190140\n")
    >>>     f.write(":100110002146017E17C20001FF5F160021480119\n")
    >>>     f.write(":00000001FF\n")
    >>> # Call the function with the appropriate file paths
    >>> convert_hex_to_bin("test.hex", "test.bin")
    >>> # Verify that the output file was created and has the expected contents
    >>> with open("test.bin", "rb") as f:
    >>>     assert f.read() == bytes.fromhex("3A10010000214601360121470136007EFE09D21901403A100110002146017E17C20001FF5F1600214801193A00000001FF")

    """
    with open(output_path, "wb") as ostream:
        with open(source_path, "r", encoding="utf-8") as istream:
            for line in istream.readlines():
                ostream.write(bytes.fromhex("3A" + line[1:]))

if __name__ == "__main__":
    convert_hex_to_bin(
        source="pwr-200-wvd-5412-of-pm-New_Firmware.hex",
        output="output.bin",
    )
