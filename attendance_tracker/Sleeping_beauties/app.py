from flask import Flask, render_template
import connect

app = Flask(__name__)

@app.route('/')
def index():
    # Define a Python variable
    my_variable = connect.b
    print(my_variable)
    
    # Render the template and pass the variable to the HTML
    return render_template('dashboard.html', my_variable=my_variable)

#if __name__ == '__main__':
#     app.run(debug=True)