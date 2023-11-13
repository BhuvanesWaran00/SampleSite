from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    "host": "test.cwyp9bpkbyeg.ap-south-1.rds.amazonaws.com:3306",
    "user": "admin",
    "password": "admin123",
    "database": "data",
    "port": 3306
}

# Function to insert user data into the database
def insert_user(email, name, password):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    insert_query = "INSERT INTO user_details (Email, Name, Password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (email, name, password))
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        confirm_password = request.form['con_pass']

        if password != confirm_password:
            flash("Passwords do not match. Please try again.", "error")
        else:
            insert_user(email, name, password)
            flash("Signup successful!", "success")

    return render_template('signup.html')

if __name__ == '__main__':
    app.secret_key = 'b123'  # Change this to a strong secret key
    app.run(debug=True)
