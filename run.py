from flaskblog import create_app

# app is the app created with the function in __init__.py
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
