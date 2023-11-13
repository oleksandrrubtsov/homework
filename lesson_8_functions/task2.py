def make_country(country_name,country_capital):
    country_dict = {
        'name': country_name,
        'capital': country_capital}
    return country_dict

country_dict = make_country("USA", "Washington DC")
print(country_dict)