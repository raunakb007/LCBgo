from flask import Flask, render_template,request
from drinkSearch import drink_search

app = Flask('__name__')


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        drink_name = request.form.get('drinkname')
        search_results = drink_search(drink_name)
        if search_results:
            return render_template('hibiki.html', results=search_results['result'])
        else:
            return "Could Not Find The Drink!"

    return render_template('hibiki.html', results=[])

if __name__ == "__main__":
    app.run(debug=True)
