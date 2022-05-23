from pathlib import Path

# resource directories
assets_dir = Path('assets')
images_dir = Path(assets_dir, 'images')
fonts_dir = Path(assets_dir, 'fonts')
sounds_dir = Path(assets_dir, 'sounds')

class AssetsPath:
    # Images
    background_day = Path(images_dir, 'background-day.png')
    background_night = Path(images_dir, 'background-night.png')
    background_scoreboard = Path(images_dir, 'message.png')

    red_bird = [
        Path(images_dir, 'redbird-upflap.png'),
        Path(images_dir, 'redbird-midflap.png'),
        Path(images_dir, 'redbird-downflap.png')
    ]

    floor = Path(images_dir, 'base.png')
    pipe_green = Path(images_dir, 'pipe-green.png')

    # Fonts
    font = Path(fonts_dir, 'flappybird_font.TTF')

    # Sounds
    sound_die = Path(sounds_dir, 'sfx_die.wav')
    sound_hit = Path(sounds_dir, 'sfx_hit.wav')
    sound_point = Path(sounds_dir, 'sfx_point.wav')
    sound_swooshing = Path(sounds_dir, 'sfx_swooshing.wav')
    sound_wing = Path(sounds_dir, 'sfx_wing.wav')


