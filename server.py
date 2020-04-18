from flask import Flask, request, render_template, redirect
import csv  # Comma Separated Value

app = Flask(__name__)
print(app)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<page_name>')
def my_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        return database.write(f'\n\n email: {email}\n subject: {subject} \n message: {message}')


# copied this from csv python documentation
def write_to_csv(data):  # open database.csv in excel to see the result properly
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# copied this from flask documentation(request data)
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            print(data)  # to get the submitted data as dict in cmd
            return redirect('/thankyou.html')
        except:
            return "Unable to save info to database!"
    else:
        return 'Something Went Wrong. Try Again!!!'
