"""
A hub used to trade different artifacts
Artworks could be listed and traded between museums and individuals
Transactions also occur during trades
You can add new arts and clients and transact between them
"""


class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return f'{self.artist}. "{self.title}". {self.year}, {self.medium}, {self.owner.name}, {self.owner.location}.'


class MarketPlace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
        self.listings.remove(expired_listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Client:
    def __init__(self, name, wallet, location='Private Collection'):
        self.name = name
        self.location = location
        self.wallet = wallet

    def sell_artwork(self, artwork, price, market_place):
        if artwork.owner is self:
            new_listing = Listing(artwork, price, self)
            market_place.add_listing(new_listing)

    def buy_artwork(self, artwork, market_place):
        if artwork.owner is not self:
            art_listing = None
            for listing in market_place.listings:
                if listing.art == artwork:
                    art_listing = listing
                    break
        if art_listing is not None:
            self.wallet -= art_listing.price
            art_listing.art.owner.wallet += art_listing.price
            art_listing.art.owner = self
            market_place.remove_listing(art_listing)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return f'{self.art.title} ${self.price}'


# A quick test using 2 clients transaction in a market plance
art_hub = MarketPlace()
client_1 = Client('Edytta Halpirt', 238000000)
client_2 = Client('The MOMA', 325000000, 'New York')
art_1 = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)',
            'oil on canvas', 1910, client_1)
print(art_1)


client_1.sell_artwork(art_1, 6000000, art_hub)
client_2.buy_artwork(art_1, art_hub)
print(art_1)

print(client_1.wallet)
print(client_2.wallet)
