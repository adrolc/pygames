from pathlib import Path

# resource directories
images_dir = Path('assets')
bullets_dir = Path(images_dir, 'bullets')
boxes_dir = Path(images_dir, 'drop_box')
gold_dir = Path(images_dir, 'gold')
explosion_dir = Path(images_dir, 'explosion')

class AssetPath:
    """Paths to game resources"""
    background = Path(images_dir, 'background.png')
    ship = Path(images_dir, 'ship.png')
    dragon_frame_1 = Path(images_dir, 'dragon_1.png')
    dragon_frame_2 = Path(images_dir, 'dragon_2.png')
    heart = Path(images_dir, 'heart.png')
    gold = Path(gold_dir, '1.png')

    bullets = [
        Path(bullets_dir, 'bullet1.png'),
        Path(bullets_dir, 'bullet2.png'),
        Path(bullets_dir, 'bullet3.png'),
        Path(bullets_dir, 'bullet4.png'),
    ]
    boxes = [
        Path(boxes_dir, 'box1.png'),
        Path(boxes_dir, 'box2.png'),
        Path(boxes_dir, 'box3.png'),
        Path(boxes_dir, 'box4.png'),
    ]

    # Explosion animation frames
    number_of_explosion_frames = sum(path.is_file() for path in Path(explosion_dir).iterdir())
    explosion_frames = [Path(explosion_dir, f"{frame}.png") for frame in range(1, number_of_explosion_frames + 1)]

    # Gold rotation animation frames
    number_of_gold_frames = sum(path.is_file() for path in Path(gold_dir).iterdir())
    gold_frames = [Path(gold_dir, f"{frame}.png") for frame in range(1,number_of_gold_frames + 1)]

