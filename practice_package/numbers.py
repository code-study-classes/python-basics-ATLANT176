calculate_distance = lambda x, y: abs(x - y) # noqa E731

calculate_segments = lambda a, b: a // b # noqa E731

calculate_digit_sum = lambda number: sum(int(d) for d in str(abs(number))) # noqa E731

round_to_multiple = lambda number, multiple: round(number / multiple) * multiple # noqa E731   

calculate_rect_area = lambda x1, y1, x2, y2: abs(x2 - x1) * abs(y2 - y1) # noqa E731
