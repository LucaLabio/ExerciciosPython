from pygeocoder import Geocoder
endereco = 'avenida paulista, 100 sao paulo'
resultado = Geocoder('apikey').reverse_geocode(-23.5703022, -46.6451267)
print(resultado)