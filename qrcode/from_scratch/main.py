from src.grid import Grid
from src.qr_engine import get_qrcode_from
import math

def main():
    data = 'example'
    data_as_qr = get_qrcode_from(data)
    i = 1
    for bit in data_as_qr:
        # print(bit, end='')
        if i >= 25:
            # print()
            i = 1
        i += 1

    cols = rows = int(math.sqrt(len(data_as_qr)))
    # cols = rows = 34l+ 6
    grid = Grid(data_as_qr, cols, rows)
    grid.draw()

if __name__ == '__main__':
    main()
