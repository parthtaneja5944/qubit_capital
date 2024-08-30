from flask import Flask, jsonify
from fetch_data import fetch_company_data
from enrich_data import enrich_data
from filter_data import filter_data
from store_data import store_enriched_data

app = Flask(__name__)

@app.route('/enrich', methods=['POST'])
def enrich():
    try:
        company_data = fetch_company_data()
        linkedin_urls = [row[1] for row in company_data]
        enriched_response = enrich_data(linkedin_urls)

        if not enriched_response:
            raise ValueError("Failed to enrich company data.")
        
        filtered_data = filter_data(enriched_response)
        store_enriched_data(filtered_data)
  
        return jsonify({"message": "Company data enriched and stored successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
