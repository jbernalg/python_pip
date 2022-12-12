import store
from fastapi import FastAPI # importar libreria fastapi
from fastapi.responses import HTMLResponse #libreria para devolver un HTML

app =FastAPI()

#funcion que devuelve los valores de una lista
@app.get('/')
def get_list():
    return [1,2,3]

#funcion que devuelve la informacion de contacto
@app.get('/contact', response_class = HTMLResponse)
def get_list():
    return '''
        <h1>Hola soy una pagina</h1>
        <p>Soy un parrafo</p>
    '''

def run():
    store.get_categories()

if __name__ == '__main__':
    run()