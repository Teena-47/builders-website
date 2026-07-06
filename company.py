from flask import Flask, render_template, request, abort
import json

# Create the Flask app object
app = Flask(__name__)

# Load project data once when the server starts
with open('projects.json', 'r') as file:
    projects = json.load(file)


# ---------- HOME PAGE ----------
@app.route('/')
def home():
    # Pass the full list of projects to company.html
    # so it can render the "Previous Projects" carousel
    return render_template('company.html', projects=projects)


# ---------- ABOUT PAGE ----------
@app.route('/about')
def about():
    return render_template('about.html')


# ---------- CONTACT PAGE ----------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message_sent = False

    if request.method == 'POST':
        # Read form fields sent from contact.html
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # For now we just print to the terminal.
        # Later you can save this to a database or send an email.
        print(f"New contact message from {name} ({email}): {message}")

        message_sent = True

    return render_template('contact.html', message_sent=message_sent)


# ---------- PROJECT DETAIL PAGE ----------
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    # Find the project whose "id" matches project_id
    project = next((p for p in projects if p['id'] == project_id), None)

    if project is None:
        # No project with that id -> show a 404 error page
        abort(404)

    return render_template('project_detail.html', project=project)


# ---------- 404 ERROR PAGE ----------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# ---------- RUN THE APP ----------
if __name__ == '__main__':
    app.run(debug=False)
