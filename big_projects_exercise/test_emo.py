
from emo2 import get_emoji
from unittest import TestCase, main

class EmojiTests(TestCase):

    def test_happy(self):
        wynik = get_emoji("wesoly")
        self.assertEqual(wynik, ":-)")


if __name__ == '__main__':
    main()

