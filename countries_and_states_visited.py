"""
Based on:

    https://gis.stackexchange.com/questions/88209/python-mapping-in-matplotlib-cartopy-color-one-country

    and

    https://github.com/SciTools/cartopy/issues/1303

"""
import matplotlib.pyplot as plt
import cartopy
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs

ax = plt.axes(projection=ccrs.PlateCarree())
#ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
#ax.add_feature(cartopy.feature.COASTLINE)
#ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
#ax.add_feature(cartopy.feature.LAKES, alpha=0.95)
#ax.add_feature(cartopy.feature.RIVERS)
ax.set_extent([-150, 60, -25, 60])

country_shpfilename = shpreader.natural_earth(
    resolution='110m', category='cultural', name='admin_0_countries')
country_reader = shpreader.Reader(country_shpfilename)
countries = country_reader.records()

usa_states_shpfilename = shpreader.natural_earth(
    resolution='110m', category='cultural',
    name='admin_1_states_provinces_lakes')
usa_states_reader = shpreader.Reader(usa_states_shpfilename)
usa_states = usa_states_reader.records()

countries_visited = [
    'ARG',  # Argentina
    'AUT',  # Austria
    'BEL',  # Belgium
    'CAN',  # Canada
    'CHE',  # Swizterland
    'CUB',  # Cuba
    'CZE',  # Czech Republic
    'DEU',  # Germany
    'DNK',  # Denmark: 2008
    'ESP',  # Spain
    'FIN',  # Finland: 2025
    'FRA',  # France
    'GBR',  # United Kingdom
    'GTM',  # Guatemala
    'HND',  # Honduras
    'IND',  # India: 2005, 2010
    'ITA',  # Italy
    'JPN',  # Japan
    'KEN',  # Kenya
    'KHM',  # Cambodia
    'LAO',  # Laos
    'MEX',  # Mexico
    'NLD',  # The Netherlands
    'NOR',  # Norway
    'POL',  # Poland
    'SWE',  # Sweden: 2008, 2025
    'THA',  # Thailand
    'USA',  # United States of America
    'ZMB',  # Zambia
]

usa_states_visited = [
    'Alabama',
    'Arizona',
    'California',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kentucky',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Mexico',
    'New York',
    'North Carolina',
    'Ohio',
    'Oregon',
    'Pennsylvania',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming',
]

key = 'ADM0_A3'

for country in countries:
    print(country.attributes['NAME_EN'])
    print(country.attributes[key])
    if country.attributes[key] in countries_visited:
        ax.add_geometries([country.geometry], ccrs.PlateCarree(),
                          facecolor=(0, 0, 1),
                          label=country.attributes[key])
    else:
        ax.add_geometries([country.geometry], ccrs.PlateCarree(),
                          facecolor=(0, 1, 0),
                          label=country.attributes[key])
ax.set_title(f'{len(countries_visited)} Countries and {len(usa_states_visited)} USA States Visited')

for state in usa_states:
    print(state.attributes['name_en'])
    if state.attributes['name_en'] in usa_states_visited:
        ax.add_geometries([state.geometry], ccrs.PlateCarree(),
                          facecolor=(1, 0, 0))
    else:
        ax.add_geometries([state.geometry], ccrs.PlateCarree(),
                          facecolor=(0, 1, 0))


plt.show()
