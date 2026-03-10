# This is very bare-bones, will need a more robust implementation when making back end

class ItemManager:

    items = []

    def __init__(self):

        for i in range(10):
            self.addItem((i, "The all-new iPhone " + str(i) + " Pro Max", "The latest and greatest in overpriced phone technology", "assets/test_image.bmp", 99999, i, 0, "Phone"))

    def getItems(self, query):
        return self.items

    def addItem(self, item):
        self.items.append(item)

    def getItemName(self, itemID):
        for item in self.items:
            if item[0] == itemID:
                return item[1]

    def getItemDescription(self, itemID):
        for item in self.items:
            if item[0] == itemID:
                return item[2]

    def getItemThumbnail(self, itemID):
        for item in self.items:
            if item[0] == itemID:
                return item[3]

    def getItemPrice(self, itemID):
        for item in self.items:
            if item[0] == itemID:
                return item[4]

    def getItemSellerID(self, itemID):
        for item in self.items:
            if item[0] == itemID:
                return item[4]

    def getItemRiskScore(self, itemID):
        for item in self.items:
            if item[0] == itemID:
                return item[4]

    def getItemCategory(self, itemID):
        for item in self.items:
            if item[0] == itemID:
                return item[4]



itemManager = ItemManager()