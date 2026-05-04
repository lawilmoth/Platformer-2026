import pygame


def parse_sprite_sheet(
    sheet: pygame.Surface,
    start_x: int,
    start_y: int,
    frame_count: int,
    columns: int,
    rows: int
) -> list[pygame.Surface]:
    """
    Parses a sprite sheet into individual frames.

    Args:
        sheet: Loaded sprite sheet surface
        start_x: X pixel where the animation starts
        start_y: Y pixel where the animation starts
        frame_count: Total number of frames to extract
        columns: Number of columns in the sprite sheet
        rows: Number of rows in the sprite sheet

    Returns:
        List of pygame.Surface frames
    """

    sheet_width = sheet.get_width()
    sheet_height = sheet.get_height()

    frame_width = sheet_width // columns
    frame_height = sheet_height // rows

    frames = []

    for i in range(frame_count):
        col = i % columns
        row = i // columns

        x = start_x + col * frame_width
        y = start_y + row * frame_height

        frame = pygame.Surface(
            (frame_width, frame_height),
            pygame.SRCALPHA
        )

        frame.blit(
            sheet,
            (0, 0),
            pygame.Rect(x, y, frame_width, frame_height)
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
