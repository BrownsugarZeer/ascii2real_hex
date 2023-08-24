def convert_hex_to_bin(source_path: str, output_path: str) -> None:
    with open(output_path, "wb") as ostream:
        with open(source_path, "r", encoding="utf-8") as istream:
            for line in istream.readlines():
                ostream.write(bytes.fromhex("3A" + line[1:]))

if __name__ == "__main__":
    convert_hex_to_bin(
        source="pwr-200-wvd-5412-of-pm-New_Firmware.hex",
        output="output.bin",
    )
