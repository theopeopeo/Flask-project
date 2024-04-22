from flask import Flask, render_template, jsonify, request
from supabase import create_client, Client



app = Flask(__name__)
url: str = "https://shqvhviglspulcejfrmv.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNocXZodmlnbHNwdWxjZWpmcm12Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM2ODQ2NTEsImV4cCI6MjAyOTI2MDY1MX0.pv-aL_tLxpPVwvpIU6iJoW-_fPCiDLuiiS3U0LgjfhY"
supabase: Client = create_client(url, key)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "Rs. 10,00,000",
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "Rs. 15,00,000",
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Remote",
        "salary": "Rs. 12,00,000",
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "San Francisco, USA",
        "salary": "$120,000",
    },
]
    
@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

@app.route('/users', methods=['POST'])
def add_user():
    username = request.json['username']  # Make sure client sends JSON with a 'username' key
    data = supabase.table("users").insert({"username": username}).execute()
    return jsonify(data.data), 201

@app.route('/users', methods=['GET'])
def get_users():
    data = supabase.table("users").select("*").execute()
    return jsonify(data.data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
