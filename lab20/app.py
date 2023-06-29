from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Додайте код для перевірки введених даних для входу
        # та реагування на результати перевірки
        
        return f'Ви увійшли як {username}'
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
