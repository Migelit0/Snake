class graphics:
    def __init__(self, snake_body, apple_coords):
        self.snake_blocks = snake_body
        self.apple = apple_coords

    def draw_field(self):
        from PIL import Image, ImageDraw
        field = Image.new('RGB', (1000, 1000), (255, 255, 255))
        field_draw = ImageDraw.Draw(field)

        for i in range(0, 1040, 40):
            field_draw.line((0, i, 1000, i), fill=(0, 0, 0), width=2)
            field_draw.line((i, 0, i, 1000), fill=(0, 0, 0), width=2)

        is_head = True
        for elem in self.snake_blocks:
            y = elem[0]
            x = elem[1]
            field_draw.rectangle(((40 * x + 3, 40 * y + 3), (40 * (x + 1) - 2, 40 * (y + 1) - 2)), (150, 150, 150))
            if is_head:
                field_draw.ellipse(((40 * x + 10, 40 * y + 10), (40 * (x + 1) - 10, 40 * (y + 1) - 10)), (255, 0, 0))
            is_head = False

        x_apple = self.apple[1]
        y_apple = self.apple[0]
        field_draw.ellipse(((40 * x_apple + 3, 40 * y_apple + 3), (40 * (x_apple + 1) - 2, 40 * (y_apple + 1) - 2)),
                           (255, 0, 0))

        field.save('field.png', 'png')
