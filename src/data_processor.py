class DataProcessor:
    def __init__(self, port):
        # connect to com port
        pass

    def get_data(self) -> dict:
        # parse data from com port and return processed object
        return {
            'floodfill': [
                [5, 4, 5],
                [0, 3, 4],
                [1, 2, 5],
            ],
            'walls': [
                [(1, 0, 1, 1), (1, 0, 0, 0), (1, 1, 1, 0)],
                [(1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 0, 0)],
                [(0, 0, 1, 1), (0, 1, 1, 0), (0, 1, 1, 1)],
            ],
            'visited': [
                [1, 1, 0],
                [1, 1, 1],
                [1, 1, 1]
            ],
            'position': (1, 1),
        }

    def send_data(self, data: list):
        # prepare and send data to com port
        pass