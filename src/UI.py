import tkinter as tk
from src.data_processor import DataProcessor

wall_offsets = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

class UI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.state('zoomed')
        self.root.title('Maze viewer')

        info_frame = tk.Frame(self.root)
        connect_frame = tk.Frame(info_frame)
        tk.Label(connect_frame, text='Com port:').pack(side=tk.LEFT, anchor=tk.N)
        self.com_port = tk.StringVar(value='3')
        tk.Entry(connect_frame, textvariable=self.com_port).pack(side=tk.LEFT, anchor=tk.N)
        tk.Button(connect_frame, text='Connect', command=self.connect).pack(side=tk.LEFT, anchor=tk.N)

        self.connect_status_label = tk.Label(info_frame, text='')

        connect_frame.pack(side=tk.TOP, anchor=tk.W)
        self.connect_status_label.pack(side=tk.TOP, anchor=tk.W)
        info_frame.pack(side=tk.LEFT, anchor=tk.N)

        self.data_processor: DataProcessor | None = None

        self.maze_shape: tuple | None = None
        self.maze_config: dict | None = None
        self.maze_size = (601, 601)

        self.maze_space = tk.Canvas(self.root, bg='blue', height=self.maze_size[0], width=self.maze_size[1])
        self.maze_space.pack(side=tk.RIGHT, anchor=tk.CENTER)

    def start(self):
        self.root.mainloop()

    def connect(self):
        self.data_processor = DataProcessor(port='COM' + self.com_port.get())
        self.connect_status_label.config(text='Connected', fg='green')
        # read first data and init table and variables
        self.maze_shape = (3, 3)
        self.maze_config = {
            'cell_size': self.maze_size[0] // max(self.maze_shape),

        }
        self.update_maze()

    def update_maze(self):
        size = self.maze_config['cell_size']
        data = self.data_processor.get_data()
        for y in range(self.maze_shape[0]):
            for x in range(self.maze_shape[1]):
                offset = 2
                corner_left = (x * size + offset, y * size + offset)
                corner_right = ((x + 1) * size + offset, (y + 1) * size + offset)
                if data['visited'][y][x]:
                    self.maze_space.create_rectangle(
                        corner_left,
                        corner_right,
                        fill='green',
                        width=0,
                    )
                    first_point = (corner_left[0] * size, corner_left[1] * size)
                    for direction, wall in enumerate(data['walls'][y][x]):
                        second_point = (
                            first_point[0] + wall_offsets[direction][0] * size,
                            first_point[1] + wall_offsets[direction][1] * size,
                        )
                        if wall:
                            self.maze_space.create_line(first_point, second_point, width=5)
                        first_point = second_point

                center = ((corner_left[0] + corner_right[0]) // 2, (corner_left[1] + corner_right[1]) // 2)
                self.maze_space.create_text(center, text=data['floodfill'][y][x])
                # self.maze_space.create_line()

