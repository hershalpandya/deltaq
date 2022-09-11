# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_standard(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        for day in range(5):
            gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(15, items[0].quality)

    def test_aged(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)
        for day in range(5):
            gilded_rose.update_quality()
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_backs(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)
        for day in range(12):
            gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(41, items[0].quality)

    def test_sulfu(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80)]
        gilded_rose = GildedRose(items)
        for day in range(5):
            gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(80, items[0].quality)        

    def test_conju(self):
        """ Note:
        This is a new implementation in new code. 
        So results won't match with old code.
        In 3 iterations, quality should drop by 6
        And sell_in date will drop by 3.
        """
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        for day in range(3):
            gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)        

        
if __name__ == '__main__':
    unittest.main()
