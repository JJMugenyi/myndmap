from front import create_app
# from auth import auth  # Import the auth blueprint

app = create_app()

# Register the auth blueprint
#app.register_blueprint(auth)

# ... Other configurations and routes ...

if __name__ == '__main__':
    app.run(debug=True)
