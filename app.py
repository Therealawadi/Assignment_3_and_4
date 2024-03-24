# Import necessary modules and classes from Flask
from flask import Flask, render_template, redirect, url_for
from form import StudentProgressForm  # Import the StudentProgressForm from form.py

# Create a Flask app
app = Flask(__name__)
# Set a secret key for CSRF protection
app.config['SECRET_KEY'] = 'your_secret_key'


# Route for the home page
@app.route('/')
def home():
    return render_template("index.html")


# Route for the about us page
@app.route('/about-us')
def welcome():
    return render_template("about-us.html")


# Route for the form page, handling both GET and POST requests
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = StudentProgressForm()  # Instantiate the StudentProgressForm
    if form.is_submitted():
        # Process the form data if the form is submitted
        name = form.name.data
        student_number = form.student_number.data
        email = form.email.data
        grades = form.grades.data
        satisfaction = form.satisfaction.data
        improvement = form.improvement.data

        # Write the form data to a text file
        with open("information.txt", "a") as f:
            f.write(
                f"Name: {name}\n"
                f"Student Number: {student_number}\n"
                f"Email: {email}\n"
                f"Grades: {grades}\n"
                f"Satisfaction: {satisfaction}\n"
                f"Improvement: {improvement}\n\n"
            )
        # Redirect to a thank you page after form submission
        return redirect(url_for('thank_you'))
    return render_template("form.html", form=form)  # Render the form template with the form object


# Route for the thank you page
@app.route('/thank-you')
def thank_you():
    return render_template("thank_you.html")


# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
