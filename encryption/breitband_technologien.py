
conv_table = [
    # name, generation, transmission rate (bit/s)
    ('GSM', '2G', 9.6e3),
    ('GPRS', '2.5G', 115e3),
    ('EDGE', '2.75G', 236e3),
]

def get_entry(tech: str) -> tuple[str, str, float]:
    i = list(map(lambda entry: entry[0] == tech, conv_table)).index(True)
    return conv_table[i]

def get_time(bits: float, tech: str) -> float:
    return bits * get_entry(tech)[2]

def convert(bits: float, src: str, dst: str) -> float:
    src_entry = get_entry(src)
    dst_entry = get_entry(dst)

    print(f'Converting from {src}({src_entry[2]}bit/s) to {dst}({dst_entry[2]}bit/s)')

    return bits * src_entry[2] / dst_entry[2]

def test_convert() -> None:
    assert get_time(1e3, 'GSM') == 1

test_convert()
