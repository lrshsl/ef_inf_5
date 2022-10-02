# Some constants
# Most of those should become variables or
# functions and have only fixed values for prototyping

# Error correction & other formalities
DEFAULT_ERR_CORRECTION_LVL = [0, 1]
DEFAULT_PATTERN_MASK = [1, 0, 0]
DEFAULT_FORMAT_STRING = DEFAULT_ERR_CORRECTION_LVL + DEFAULT_PATTERN_MASK

DEFAULT_GENERATOR_POLYNOMIAL = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]

# QR-23 Template
SIZE = 23
CTRL_FIELD_EDGE = [1, 0, 0, 0, 0, 0, 1]
CTRL_FIELD_BLOCK = [1, 0, 1, 1, 1, 0, 1]
WHITE_SPACE = [1] * 7
DEFAULT_TEMPLATE = (
    ( WHITE_SPACE,                  WHITE_SPACE ),
    ( CTRL_FIELD_EDGE,              CTRL_FIELD_EDGE  ),
    ( CTRL_FIELD_BLOCK,             CTRL_FIELD_BLOCK ),
    ( CTRL_FIELD_BLOCK,             CTRL_FIELD_BLOCK ),
    ( CTRL_FIELD_BLOCK,             CTRL_FIELD_BLOCK ),
    ( CTRL_FIELD_EDGE,              CTRL_FIELD_EDGE  ),
    ( WHITE_SPACE,                  WHITE_SPACE ),

    *[([], []) for _ in range(9)],

    ( WHITE_SPACE,                  [] ),
    ( CTRL_FIELD_EDGE,              [] ),
    ( CTRL_FIELD_BLOCK,             [] ),
    ( CTRL_FIELD_BLOCK,             [] ),
    ( CTRL_FIELD_BLOCK,             [] ),
    ( CTRL_FIELD_EDGE,              [] ),
    ( WHITE_SPACE,                  [] ),
)


# Fake Enum. Just names for the bits
MARGIN_BIT: int = 2
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
    cols = 23
    rows = 23

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


def get_qrcode_from(data: str) -> list:
    """ Entry point for this file """

    data = [
        *[1, 0] * 23 * 1000
    ]
    qr = QrCode(data)
    return list(qr.gen_qrcode())


