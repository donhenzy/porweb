from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home(username=None, post_id=None):
    return render_template('index.html')


# function to dynamically feed the browser the file
@app.route('/<string:page_name>')
def pages(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('db.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open("./database.csv", newline='', mode='a') as database2:
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    else:
        #         error = 'Invalid username/password'
        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return 'something went wrong'
