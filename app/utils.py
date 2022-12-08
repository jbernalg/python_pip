#funcion para obtener la poblacion de un pais
def get_population(country_dict):
  #creamos un diccionario con la informacion necesaria
  population_dict = {
    '2022':int(country_dict['2022 Population']),
    '2020':int(country_dict['2020 Population']),
    '2015':int(country_dict['2015 Population']),
    '2010':int(country_dict['2010 Population']),
    '2000':int(country_dict['2000 Population']),
    '1990':int(country_dict['1990 Population']),
    '1980':int(country_dict['1980 Population']),
    '1970':int(country_dict['1970 Population'])
  }

  # devolver en formato lista, los labels y values para graficar
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values 
  

# obtener la poblacion basados en un pais
def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result


  
  