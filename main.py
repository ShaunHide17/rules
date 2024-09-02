from flask import Flask, render_template, request, jsonify
from faker import Faker

from utils import query_db

app = Flask(__name__)
## chrome://net-internals/#socket

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/select')
def select():
    rows = [
      {
        'id':x,
        'company':f'Company {x+1}',
        'contact':f'Contact {x+1}',
        'country':f'Country {x+1}'
      }
      for x in range(0,30)
    ]
    return render_template('select.html', rows=rows)

@app.route('/tabs')
def tabs():
    if request.args.get('tab'):
        tab = request.args.get('tab')
        return render_template('partials/tab_request.html',tab=tab)
    else:
        return render_template('tabs.html',tab="1")

@app.route('/datatables')
def datatables():
    return render_template('datatables.html')

############################################################
## HTMX Learning

## List :: HTMX Accessory Routes
@app.route('/list-load-items', methods = ['GET'])
def list_load_items():
    items = [f"Item {x+1}" for x in range(0,20)]
    return render_template('partials/list_load_items.html', items=items)

## Table :: HTMX Accesory Routes
@app.route('/table-load-items', methods = ['GET'])
def table_load_items():
    rows = [
      {
        'company':f'Company {x+1}',
        'contact':'Unknown',
        'country':'United Kingdom'
      }
      for x in range(0,5)]
    return render_template('partials/table_load_items.html', rows=rows)

# @app.route('/load-more-items', methods=['GET'])
# def load_more_items():
#     # Simulate loading more items
#     items = ["Item 4", "Item 5", "Item 6"]
#     return render_template('partials/items_list.html', items=items)

# @app.route('/search', methods=['POST'])
# def search():
#     query = request.form.get('search')
#     print(query)
#     items = [x for x in ["Item 1", "Item 2", "Item 3"] if query in x]
#     return render_template('partials/items_list.html', items=items)

# @app.route('/submit-form', methods=['POST'])
# def submit_form():
#     username = request.form['username']
#     return f"Hello, {username}!"

# @app.route('/update-item/<int:item_id>', methods=['PUT'])
# def update_item(item_id):
#     # Handle updating the item
#     return f"<div id='item-{item_id}'>Updated Item {item_id}</div>"

# @app.route('/delete-item/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     return "", 204


############################################################
## Data Sources

@app.route('/sources')
def sources():
    rows = query_db('SELECT * FROM sources')
    if type(rows) == dict:
        rows = [rows]
    return render_template('df/sources.html',rows=rows)

@app.route('/sources/edit/<int:id>', methods=['GET','POST'])
def sources_edit(id):
    if request.method == 'POST':
        print(request.form.get('name'))
        return "Edited"
    else:
        row = query_db(f'SELECT * FROM sources WHERE id={id}')[0]
        print(row)
        return render_template('df/partials/sources_edit_form.html',row=row)


@app.route('/sources/delete/<int:id>', methods=['GET'])
def sources_delete(id):
    print(id)
    return "Deleted"

@app.route('/sources/add', methods=['GET','POST'])
def sources_add():
    if request.method == 'POST':
        print(request.form.get('name'))
        return "Added"
    else:
        return render_template('df/partials/sources_add_form.html')

############################################################
## Rule Engine

############################################################
## Helpers

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
