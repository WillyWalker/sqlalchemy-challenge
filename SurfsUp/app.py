# Import the dependencies.



#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
from flask import Flask

# 2. Create an app
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)





