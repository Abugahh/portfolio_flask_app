#This is the main application file. It typically contains the Flask app instance and the routes that define the endpoints of your web application.


from flask import Flask, render_template
import os # importing operating system module

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
# It is possible to render HTML file using the function render_templae.

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/result')
def result():
    return render_template('result.html')

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)





#Debug Mode: Setting debug=True means that Flask will automatically reload the server when you make changes to the code and provide detailed error messages if something goes wrong.
#Debug Mode: It still runs in debug mode (debug=True), which you might want to change to debug=False in a production environment to avoid exposing detailed error information.
#Convention: Port 5000 is commonly used for web development servers. 
#Non-privileged Port: Ports below 1024 are considered privileged and typically require administrative privileges to bind to. Using port 5000 avoids this issue, making it easier for developers to start their Flask applications without needing special permissions.