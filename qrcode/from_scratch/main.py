from lib import Grid

def main():
    grid = Grid(10, 3)
    data_as_qr = (
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    )
    grid.eat(data_as_qr)
    grid.draw()

if __name__ == '__main__':
    main()