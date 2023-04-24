from website import views, db
from website import create_app

    
app =create_app()


if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        views.add_csv()
    