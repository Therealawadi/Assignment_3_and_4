from flask import Flask, request, render_template, redirect, url_for
from form import StudentProgressForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # You should set a secret key for CSRF protection


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about-us')
def welcome():
    return render_template("about-us.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = StudentProgressForm()
    if form.is_submitted():
        # Process the form data
        name = form.name.data
        student_number = form.student_number.data
        email = form.email.data
        grades = form.grades.data
        satisfaction = form.satisfaction.data
        improvement = form.improvement.data

        # Print the form data to the terminal
        f = open("information.txt", "a")
        f.write(f"Name: {name}, Student Number: {student_number}, Email: {email}, Grades: {grades}, Satisfaction: {satisfaction}, Improvement: {improvement}")
        f.close()

        # Redirect to a thank you page or home page
        return redirect(url_for('thank_you'))
    return render_template("form.html", form=form)


@app.route('/thank-you')
def thank_you():
    return render_template("thank_you.html")


if __name__ == '__main__':
    app.run(debug=True)
