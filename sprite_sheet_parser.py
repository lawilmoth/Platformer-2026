import pygame


def parse_sprite_sheet(
    sheet: pygame.Surface,
    start_x: int,
    start_y: int,
    frame_count: int,
    columns: int,
    rows: int,
    trim_top: int = 0,
    trim_bottom: int = 0,
    trim_left: int = 0,
    trim_right: int = 0
) -> list[pygame.Surface]:
    """
    Parses a sprite sheet into individual frames with optional trimming.

    Args:
        sheet: Loaded sprite sheet surface
        start_x: X pixel where the animation starts
        start_y: Y pixel where the animation starts
        frame_count: Total number of frames to extract
        columns: Number of columns in the sprite sheet
        rows: Number of rows in the sprite sheet
        trim_top: Pixels to trim from top of each frame
        trim_bottom: Pixels to trim from bottom of each frame
        trim_left: Pixels to trim from left of each frame
        trim_right: Pixels to trim from right of each frame

    Returns:
        List of pygame.Surface frames
    """

    sheet_width = sheet.get_width()
    sheet_height = sheet.get_height()

    frame_width = sheet_width // columns
    frame_height = sheet_height // rows

    # Adjusted frame size after trimming
    trimmed_width = frame_width - trim_left - trim_right
    trimmed_height = frame_height - trim_top - trim_bottom

    frames = []

    for i in range(frame_count):
        col = i % columns
        row = i // columns

        x = start_x + col * frame_width + trim_left
        y = start_y + row * frame_height + trim_top

        frame = pygame.Surface(
            (trimmed_width, trimmed_height),
            pygame.SRCALPHA
        )

        frame.blit(
            sheet,
            (0, 0),
            pygame.Rect(x, y, trimmed_width, trimmed_height)
        )

        frames.append(frame)

    return frames


def scale_frames(frames, scale):
    scaled = []
    for frame in frames:
        width = frame.get_width() * scale
        height = frame.get_height() * scale
        scaled.append(
            pygame.transform.scale(frame, (width, height))
        )
    return scaled
