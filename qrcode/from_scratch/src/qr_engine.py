# Some constants
# Most of those should become variables or
# functions and have only fixed values for prototyping

# Error correction & other formalities
DEFAULT_ERR_CORRECTION_LVL = [0, 1]
DEFAULT_PATTERN_MASK = [1, 0, 0]
DEFAULT_FORMAT_STRING = DEFAULT_ERR_CORRECTION_LVL + DEFAULT_PATTERN_MASK

DEFAULT_GENERATOR_POLYNOMIAL = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]

# QR-4 Template
SIZE = 21
CTRL_FIELD_EDGE = [0, 1, 1, 1, 1, 1, 0]
CTRL_FIELD_BLOCK = [0, 1, 0, 0, 0, 1, 0]
BLACK_SPACE = [0] * 7
WHITE_SPACE = [1] * 7

DEFAULT_TEMPLATE = (
    ( BLACK_SPACE + [1],            [1] + BLACK_SPACE ),
    ( CTRL_FIELD_EDGE + [1],        [1] + CTRL_FIELD_EDGE  ),
    ( CTRL_FIELD_BLOCK + [1],       [1] + CTRL_FIELD_BLOCK ),
    ( CTRL_FIELD_BLOCK + [1],       [1] + CTRL_FIELD_BLOCK ),
    ( CTRL_FIELD_BLOCK + [1],       [1] + CTRL_FIELD_BLOCK ),
    ( CTRL_FIELD_EDGE + [1],        [1] + CTRL_FIELD_EDGE  ),
    ( BLACK_SPACE + [1],            [1] + BLACK_SPACE ),
    ( WHITE_SPACE,                  WHITE_SPACE ),

    *[([], []) for _ in range(SIZE - 2 * 8)],

    ( WHITE_SPACE,                  [] ),
    ( BLACK_SPACE + [1],            [] ),
    ( CTRL_FIELD_EDGE + [1],        [] ),
    ( CTRL_FIELD_BLOCK + [1],       [] ),
    ( CTRL_FIELD_BLOCK + [1],       [] ),
    ( CTRL_FIELD_BLOCK + [1],       [] ),
    ( CTRL_FIELD_EDGE + [1],        [] ),
    ( BLACK_SPACE + [1],            [] ),
)


# Fake Enum. Just names for the bits
MARGIN_BIT: int = 1
WHITE_BIT: int = 1
BLACK_BIT: int = 0


# Toggle debug printing for this file
debug = False


def flatten_and_iter(arr: list) -> list:
    """ Returns a Iterator over the elements of the direct sublists of 'arr'
        Flattens only to depth 2
    """
    return (x for sublist in arr for x in sublist)


class QrCode:

    def __init__(self, data_bits: list) -> None:
        """ Konstructor """
        self.data_bits = data_bits
        self.format_str = DEFAULT_FORMAT_STRING
        self.gen_polynomial = DEFAULT_GENERATOR_POLYNOMIAL
        self.template = DEFAULT_TEMPLATE
        self.qr_size = SIZE

    def gen_qrcode(self):
        """ Yields the final QR code bit for bit """

        # Set up iterator over raw data
        bit_iter = iter(self.data_bits)

        # Decide whether to count line numbers or not
        if debug: ln=0

        # First three lines are white
        for _ in range((self.qr_size + 6) * 3): yield MARGIN_BIT

        # Draw QR code line for line in read direction (top -> bottom, left -> right)
        for line in self.template:

            # Print debug information if necessairy
            if debug:
                print(f"line {ln}: \n\t1: {line[0]}\n\t2: {self.qr_size - (len(line[0]) + len(line[1]))}\n\t3: {line[1]}")
                ln += 1

            # Three unit wide white margin
            for _ in range(3): yield MARGIN_BIT

            """ Acutal Content """
            # Template bits
            for bit in line[0]: yield bit

            # Data bits
            for _ in range(self.qr_size - len(line[0]) - len(line[1])):
                yield next(bit_iter)

            # Template bits
            for bit in line[1]: yield bit

            """ Margin """
            # White margin after content
            for _ in range(3): yield MARGIN_BIT


        # Last three lines are white again
        for _ in range((self.qr_size + 6) * 3): yield MARGIN_BIT


MODE_INDICATOR = [0, 1, 0, 0]
REQUIRED_CHAR_COUNT_LENGTH = 8

QR_VERSION: int = 4
ERR_CORRECTION_LVL_L = 0

def as_byte(char: str) -> list:
    # Convert to array of binary representation of characters
    in_binary = [int(bit) for bit in bin(char)[2:]]
    
    # Make len = 8
    while len(in_binary) < 8:
        in_binary.insert(0, 0)

    return in_binary

# class QRMetaData:
#     """ Holds metadata for QR codes """
#     def __init__(self,
#                  version: int,
#                  err_correction_lvl: int,
#                  encoding_mode: int):
#         self.version = version
#         self.err_correction_lvl = err_correction_lvl
#         self.encoding_mode = encoding_mode

#     # Only blueprint
#     def get_capacity(self):
#         assert all((self.version == 4,
#                     self.err_correction_lvl == ERR_CORRECTION_LVL_L,
#                     self.encoding_mode == ENCODING__MODE_BYTE))
#         return 80


def get_qrcode_from(data: str):
    """ Entry point for this file """
    # used_qr_code_type = QRMetaData(QR_VERSION, ERR_CORRECTION_LVL_L)

    # Char count
    char_count = [int(x) for x in bin(len(data))[2:]]
    while len(char_count) < REQUIRED_CHAR_COUNT_LENGTH:
        char_count.insert(0, 0)

    raw_data = [as_byte(c) for c in bytes(data, 'utf-8')]
    raw_data = flatten_and_iter(raw_data)

    # max_capacity = look_up_max_capacity(used_qr_code)
    # assert used < max_capacity
    # if used < max_capacity - 4:
        # nb_padding_zeros = 4
    # elif used < max_capacity:
        # nb_padding_zeros = max_capacity - used
    padding_zeros = [0] * 4

    tmp_data = [
        *MODE_INDICATOR,
        *char_count,
        *raw_data,
        *padding_zeros,
        *[1,1,1,0,1,1,0,0 , 0,0,0,1,0,0,0,1] * 200
    ]
    additional_padding_zeros = [0] * (4 - (len(tmp_data) % 4))
    data = tmp_data + additional_padding_zeros
    qr = QrCode(data)
    return list(qr.gen_qrcode())


