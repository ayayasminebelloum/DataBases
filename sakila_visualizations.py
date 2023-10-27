from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'username' and 'password' with your MySQL username and password
engine = create_engine('mysql+pymysql://root:belloum.@Yasmines-MacBook-Air-2.local/sakila')

# Replace with your connection string
# engine = create_engine('mysql+pymysql://username:password@server_name/db_name')



# Query 1: Number of Rentals by Category
query1 = """
SELECT c.name AS category, COUNT(r.rental_id) AS rental_count
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY category;
"""

# Execute the SQL query and load the results into a pandas DataFrame
rental_data1 = pd.read_sql(query1, engine)

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar chart for Query 1
plt.bar(rental_data1['category'], rental_data1['rental_count'])

# Customize the chart for Query 1
plt.title('Number of Rentals by Category')
plt.xlabel('Category')
plt.ylabel('Rental Count')
plt.xticks(rotation=45)  # Rotate category labels for readability

# Display the chart for Query 1
plt.tight_layout()
plt.show()

# Query 2: Rental Count Over Time
query2 = """
SELECT DATE(rental_date) AS rental_day, COUNT(rental_id) AS rental_count
FROM rental
GROUP BY rental_day;
"""

# Execute the SQL query and load the results into a pandas DataFrame
rental_data2 = pd.read_sql(query2, engine)

# Set the figure size
plt.figure(figsize=(12, 6))

# Create a time-series line chart for Query 2
plt.plot(rental_data2['rental_day'], rental_data2['rental_count'], marker='o', linestyle='-')

# Customize the chart for Query 2
plt.title('Rental Count Over Time')
plt.xlabel('Rental Day')
plt.ylabel('Rental Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability

# Display the chart for Query 2
plt.tight_layout()
plt.show()

# Query 3: Average Rental Duration by Film Rating
query3 = """
SELECT film.rating, AVG(rental.rental_duration) as avg_duration
FROM film
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY film.rating
"""

# Execute the SQL query and load the results into a pandas DataFrame
rental_data3 = pd.read_sql(query3, engine)

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar chart for Query 3
plt.bar(rental_data3['rating'], rental_data3['avg_duration'])

# Customize the chart for Query 3
plt.title('Average Rental Duration by Film Rating')
plt.xlabel('Film Rating')
plt.ylabel('Average Duration')
plt.xticks(rotation=45)  # Rotate rating labels for readability

# Display the chart for Query 3
plt.tight_layout()
plt.show()

# Query 4: Rental Count Over Months in 2006
query4 = """
SELECT DATE_FORMAT(rental.rental_date, '%Y-%m') as rental_month, COUNT(rental.rental_id) as rental_count
FROM rental
WHERE YEAR(rental.rental_date) = 2006
GROUP BY rental_month
"""

# Execute the SQL query and load the results into a pandas DataFrame
rental_data4 = pd.read_sql(query4, engine)

# Set the figure size
plt.figure(figsize=(12, 6))

# Create a time-series line chart for Query 4
plt.plot(rental_data4['rental_month'], rental_data4['rental_count'], marker='o', linestyle='-')

# Customize the chart for Query 4
plt.title('Rental Count Over Months in 2006')
plt.xlabel('Rental Month')
plt.ylabel('Rental Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability

# Display the chart for Query 4
plt.tight_layout()
plt.show()

# Query 5: Rental Count by Staff Member
query5 = """
SELECT CONCAT(staff.first_name, ' ', staff.last_name) as staff_name, COUNT(rental.rental_id) as rental_count
FROM staff
LEFT JOIN rental ON staff.staff_id = rental.staff_id
GROUP BY staff.staff_id
"""

# Execute the SQL query and load the results into a pandas DataFrame
rental_data5 = pd.read_sql(query5, engine)

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar chart for Query 5
plt.bar(rental_data5['staff_name'], rental_data5['rental_count'])

# Customize the chart for Query 5
plt.title('Rental Count by Staff Member')
plt.xlabel('Staff Member')
plt.ylabel('Rental Count')
plt.xticks(rotation=45)  # Rotate staff member labels for readability

# Display the chart for Query 5
plt.tight_layout()
plt.show()
