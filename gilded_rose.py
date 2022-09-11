# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.special_cases = ["Aged Brie", "Backstage passes", "Sulfuras",
                              "Conjured"]

    def update_quality(self):
        """ Wrapper Method.
        Calls the appropriate method after scanning item.name
        """
        for item in self.items:
            special_item = any(i in item.name for i in self.special_cases)
            method_name= item.name.lower()[:4] if special_item else 'standard'
            item = eval(f"self.{method_name}(item)")
        return

    def standard(self, item):
        """ Standard Items
        * Quality degrades -1
        * Quality degrades -2 after expiry
        * 0<= Quality <=50
        """
        item.sell_in -= 1
        item.quality = item.quality-1 if item.sell_in>=0 else item.quality - 2
        item.quality = max(0, item.quality)
        item.quality = min(50, item.quality)
        return item

    def aged(self, item):
        """Aged Brie
        * Always increases in quality upto 50.
        * Sell by date has no meaning.
        * Original code has an error. Quality..
        ... increases twice after sell by date.
        """
        item.sell_in -= 1
        item.quality = item.quality+1 if item.sell_in>=0 else item.quality+2
        item.quality = min(50, item.quality)
        return item

    def back(self, item):
        """ Backstage Passes to a TAFKAL80ETC concert
        * quality @ Sell_in [-inf,0) = 0
        * quality @ Sell_in [0,5) +=3
        * quality @ Sell_in [5,10) +=2
        * quality @ Sell_in [10,inf) +=1
        """
        item.sell_in -= 1
        if item.sell_in >= 10:
            item.quality += 1
        elif item.sell_in >= 5:
            item.quality += 2
        elif item.sell_in >= 0:
            item.quality += 3
        else:
            item.quality = 0
        return item

    def sulf(self, item):
        """ Sulfuras, Hand of Ragnaros
        * Quality always constant = initial value.
        * Sell by date = initial value.
        """
        return item

    def conj(self, item):
        """Conjured
        * Quality drops twice as fast as standard cases
        """
        item.sell_in -= 1
        item.quality = item.quality-2 if item.sell_in>=0 else item.quality-4

        # Always 0<=item.quality<50
        item.quality = max(0, item.quality)
        item.quality = min(50, item.quality)
        return item


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, Days: {self.sell_in}, Quality:{self.quality}"
