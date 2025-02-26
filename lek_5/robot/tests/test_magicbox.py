from magicbox import MagicBox

def test_roll_dice():
    box = MagicBox()
    for _ in range(100):
        value = box.roll_dice()
        assert 1 <= value <= 6