from pygeocoder import Geocoder
endereco = 'avenida paulista, 100 sao paulo'
resultado = Geocoder('AIzaSyBm36NEwh9yfzNRS6Qp0IDPLfhZq6rjmGo').reverse_geocode(-23.5703022, -46.6451267)
print(resultado)