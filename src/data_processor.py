class DataProcessor:
    def __init__(self, port):
        # connect to com port
        self._init = True

    def get_data(self) -> dict:
        if self._init:
            # get maze shape, start and finish position
            pass
        else:
            pass
        # parse data from com port and return processed object
        return {
            'floodfill': [
                [5, 4, 5],
                [0, 3, 4],
                [1, 2, 5],
            ],
            'walls': [
                [(1, 0, 1, 1), (1, 0, 0, 0), (0, 0, 1, 0)],
                [(1, 1, 0, 1), (0, 0, 0, 1), (1, 1, 0, 0)],
                [(0, 0, 1, 1), (0, 1, 1, 0), (0, 1, 1, 1)],
            ],
            'visited': [
                [1, 1, 0],
                [1, 1, 1],
                [1, 1, 1]
            ],
            'position': (1, 0),
        }

    def send_data(self, data: list):
        # prepare and send data to com port
        pass