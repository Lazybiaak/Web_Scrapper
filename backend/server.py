from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # allow browser frontend to call

# Example IPO list (replace with real company IDs after checking CDSC)
IPO_LIST = {
    "Himalayan Bank": 12345,
    "Nabil Bank": 67890
}

@app.route('/api/ipos')
def get_ipos():
    return jsonify(IPO_LIST)

@app.route('/api/check-ipo', methods=['POST'])
def check_ipo():
    data = request.json
    boids = data.get('boids')
    company_id = data.get('company_id')

    if not boids or not company_id:
        return jsonify({"error": "Missing BOIDs or company_id"}), 400

    results = []
    for boid in boids:
        try:
            # 🔹 Replace URL with real IPO endpoint
            url = f"https://iporesult.cdsc.com.np/api/check"
            payload = {"boid": boid, "companyShareId": company_id}
            r = requests.post(url, json=payload)
            rdata = r.json()
            results.append({
                "boid": boid,
                "status": rdata.get("allotmentStatus", "Not Allotted"),
                "units": rdata.get("allottedQuantity", 0)
            })
        except Exception as e:
            results.append({
                "boid": boid,
                "status": "Error",
                "units": 0
            })
    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5000)