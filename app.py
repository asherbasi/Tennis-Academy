from app import create_app
app = create_app()
if __name__=='__main__':  #checks if app.py is really the main program
    app.run(debug=True, host="0.0.0.0", port=5000)

print("Hello world")

