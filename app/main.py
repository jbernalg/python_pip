# importar modulos
import utils
import read_csv
import charts
import pandas as pd


def run():
  # obtener los datos
  data = read_csv.read_csv('data.csv')
  '''
  #------------ Continente Sur America --------------------
  data_c = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data_c))
  percentages = list(map(lambda x: x['World Population Percentage'], data_c))
  '''
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

  #------------ Un pais con la poblacion en diferentes epocas --------------
  # seleccionar el pais a graficar
  country = input('Type Country: ')
  
  # obtener los datos requeridos del pais seleccionado
  result = utils.population_by_country(data, country)

  # si encuentra el pais, obtener el labels y values
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)

    # graficar los labels, values
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
    

if __name__ == '__main__':
  run()