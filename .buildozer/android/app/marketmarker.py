from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu
class MarketMarker(MapMarkerPopup):
    source = "farm.png"
    market_data = []

    def on_release(self):
        """docstring for opening location popup menu in our map."""
        menu = LocationPopupMenu(self.market_data)
        menu.size_hint = [.7,.9]
        menu.open()
