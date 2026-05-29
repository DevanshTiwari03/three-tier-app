from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import pyodbc
import os

# Load Environment Variables
load_dotenv()

# Flask App
app = Flask(__name__)

# Enable CORS
CORS(app)

# Database Configuration
DB_SERVER = os.getenv("DB_SERVER")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DRIVER = os.getenv("DB_DRIVER")

# Host and Port
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 5000))

# MSSQL Connection Function
def get_connection():

    connection_string = f"""
    DRIVER={{{DB_DRIVER}}};
    SERVER={DB_SERVER};
    DATABASE={DB_DATABASE};
    UID={DB_USERNAME};
    PWD={DB_PASSWORD};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
    """

    return pyodbc.connect(connection_string)

# Health Check Route
@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "success": True,
        "message": "Backend API Running"
    })

# Save Customer Route
@app.route("/api/customers", methods=["POST"])
def save_customer():

    try:

        data = request.json

        first_name = data.get("firstName")
        last_name = data.get("lastName")
        mobile_number = data.get("mobileNumber")
        address = data.get("address")

        # Validate Input
        if not first_name:
            return jsonify({
                "success": False,
                "message": "First Name is required"
            }), 400

        if not last_name:
            return jsonify({
                "success": False,
                "message": "Last Name is required"
            }), 400

        if not mobile_number:
            return jsonify({
                "success": False,
                "message": "Mobile Number is required"
            }), 400

        if not address:
            return jsonify({
                "success": False,
                "message": "Address is required"
            }), 400

        # DB Connection
        conn = get_connection()

        cursor = conn.cursor()

        # Insert Query
        query = """
        INSERT INTO Customers
        (
            FirstName,
            LastName,
            MobileNumber,
            Address
        )
        VALUES (?, ?, ?, ?)
        """

        cursor.execute(
            query,
            first_name,
            last_name,
            mobile_number,
            address
        )

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Customer saved successfully"
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

# Run App
if __name__ == "__main__":

    app.run(
        host=HOST,
        port=PORT,
        debug=True
    )