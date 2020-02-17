class Config:
    debug = False
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255, 0, 0
    green = 0, 255, 0
    nicegreen = 4, 117, 19
    blue = 0, 0, 255
    niceblue = 5, 36, 150
    display_height = 768
    display_width = 1280
    card_rect_height = (display_height // 3) - 2
    card_rect_width = (display_width // 3) - 2
    center_a1 = (display_width // 6, display_height // 6)
    center_a2 = ((display_width // 6) * 3, display_height // 6)
    center_a3 = ((display_width // 6) * 5, display_height // 6)
    center_b1 = (display_width // 6, (display_height // 6) * 3)
    center_b2 = ((display_width // 6) * 3, (display_height // 6) * 3)
    center_b3 = ((display_width // 6) * 5, (display_height // 6) * 3)
    center_c1 = (display_width // 6, (display_height // 6) * 5)
    center_c2 = ((display_width // 6) * 3, (display_height // 6) * 5)
    center_c3 = ((display_width // 6) * 5, (display_height // 6) * 5)
    center_points = (
        center_a1, center_a2, center_a3,
        center_b1, center_b2, center_b3,
        center_c1, center_c2, center_c3
    )
    top_left_a1 = (1, 1)
    top_left_a2 = (card_rect_width + 3, 1)
    top_left_a3 = ((card_rect_width * 2) + 5, 1)
    top_left_b1 = (1, card_rect_height + 3)
    top_left_b2 = (card_rect_width + 3, card_rect_height + 3)
    top_left_b3 = ((card_rect_width * 2) + 5, card_rect_height + 3)
    top_left_c1 = (1, (card_rect_height * 2) + 5)
    top_left_c2 = (card_rect_width + 3, (card_rect_height * 2) + 5)
    top_left_c3 = ((card_rect_width * 2) + 5, (card_rect_height * 2) + 5)
    top_left_points = (
        top_left_a1, top_left_a2, top_left_a3,
        top_left_b1, top_left_b2, top_left_b3,
        top_left_c1, top_left_c2, top_left_c3
    )
    font_vars = {
        "small": (18, 37),
        "medium": (26, 25),
        "large": (32, 22)
    }
    font_setting = ("res/MechanicalBold-oOmA.otf", white)
