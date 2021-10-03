from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__) # output: __main__

# create page from html
@app.route('/') # anytime we call a root directory (http://127.0.0.1:5000/), call below
def main_page():
    # print(url_for('static', filename='bolt.ico'))
    # call templates/index.html automatically (must create templates folder and add index.html inside)
    return render_template('index.html')

# create page from html
@app.route('/<string:page_name>') # anytime we call a root directory (http://127.0.0.1:5000/<page_name>.html), call below
def about_page(page_name):
    return render_template(page_name)


# 269. Building a portfolio 4
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':   # 270. Building a portfolio 5
        try: # 275
            data = request.form.to_dict()   # 270.
            print(data)
            # write_to_file(data) # 272
            write_to_csv(data) ################   273
            # return 'form submitted !!!' # 270. 1
            return redirect('/thankyou.html') # 270. 2
        except: # 275
            print('did not save to database')
    else:
        return 'something went wrong. Try again!'

def write_to_file(data):  #  272
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):  ################   273
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

"""
@app.route('/blog') # anytime we call http://127.0.0.1:5000/blog (<root>/blog), call below
def blog():
    return 'These are my thoughts on blogs'
    
@app.route('/blog/pet/cat') # anytime we call http://127.0.0.1:5000/blog/pet/cat (<root>/blog), call below
def blog2():
    return 'RIAM!!! MEOW'

# ------ NEW -------- #
# and go to index.html > add {{name}} into body
@app.route('/<username>')
def main_page_user(username=None):
    return render_template('index.html', name=username)

@app.route('/<username>/<int:post_id>')
def main_page_user_id(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)
"""
