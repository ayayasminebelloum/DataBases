import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Connect to the Sakila database
engine = create_engine('mysql://root:belloum.@Yasmines-MacBook-Air-2.local/sakila')

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Sakila Rental Data Over Time"),

    # Dropdown to select a query
    dcc.Dropdown(
        id='query-dropdown',
        options=[
            {'label': 'Number of Rentals by Category', 'value': 1},
            {'label': 'Rental Count Over Time', 'value': 2},
            {'label': 'Average Rental Duration by Film Rating', 'value': 3},
            {'label': 'Rental Count Over Months in 2006', 'value': 4},
            {'label': 'Rental Count by Staff Member', 'value': 5},
        ],
        value=1  # Default selected option
    ),

    # Graph to display data based on the selected query
    dcc.Graph(id='query-graph')
])

# Define callback to update the graph based on the selected query
@app.callback(
    Output('query-graph', 'figure'),
    [Input('query-dropdown', 'value')]
)
def update_graph(selected_query):
    if selected_query == 1:
        # Number of Rentals by Category
        query1 = """
        SELECT c.name AS category, COUNT(r.rental_id) AS rental_count
        FROM category c
        JOIN film_category fc ON c.category_id = fc.category_id
        JOIN film f ON fc.film_id = f.film_id
        JOIN inventory i ON f.film_id = i.film_id
        JOIN rental r ON i.inventory_id = r.inventory_id
        GROUP BY category;
        """

        rental_data = pd.read_sql(query1, engine)

        fig = px.bar(rental_data, x='category', y='rental_count', labels={'category': 'Category', 'rental_count': 'Rental Count'})
        fig.update_layout(title='Number of Rentals by Category')

    elif selected_query == 2:
        # Rental Count Over Time
        query2 = """
        SELECT DATE(rental_date) AS rental_day, COUNT(rental_id) AS rental_count
        FROM rental
        GROUP BY rental_day;
        """

        rental_data = pd.read_sql(query2, engine)

        fig = px.line(rental_data, x='rental_day', y='rental_count', labels={'rental_day': 'Rental Day', 'rental_count': 'Rental Count'})
        fig.update_layout(title='Rental Count Over Time')

    # Add more elif blocks for the rest of the queries (3, 4, 5)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
