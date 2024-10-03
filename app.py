from flask import Flask, render_template ,url_for,redirect, request
from models import Student, session

app=Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    Students = session.query(Student).all()
    return render_template('index.html', x=Students)

@app.route('/detals/<int:id>')
def details(id):
    s = session.query(Student).get(id)
    return render_template('details.html',s=s)

@app.route('/delete/<int:id>')
def delete(id):
    s= session.query(Student).get(id)
    session.delete(s)
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    st = session.query(Student).get(id)
    if request.method == "POST":
        n = request.form['name']
        e = request.form['email']
        st.name=n
        st.email = e
        session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', st=st)



@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

if __name__=="__main__":
    app.run(debug=True,port=5001)  