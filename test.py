from itertools import groupby
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn


conn = get_db_connection()
towns = conn.execute('SELECT Items.RAND_ID, Items.ItemType, Items.ItemSubtype, Items.ItemName, Items.CostStandard, Items.CostExpensive, Items.Limited, Items.Size, ShopType.ShopType FROM Items JOIN ShopType ON Items.ShopTypeID = ShopType.ID WHERE Size = "All" ORDER BY RANDOM()').fetchall()
ShopType = {}
def print_groupby(iterable, keyfunc=None):
    for key, group in groupby(towns, key=lambda t: t['ShopType']):
        shoplist = " and ".join([towns['ItemName'] for towns in group])
        print_groupby(sorted("key: '{}'-->group: {}".format(key, list(group))))

   # ShopType[key] = list(group)
