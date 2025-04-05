from flask import Flask, jsonify, send_from_directory
import pandas as pd

app = Flask(__name__, static_folder="../frontend")

# Serve the frontend index.html
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

# Endpoint to return yearly data from data.csv
# @app.route('/api/yearly-data')
# def yearly_data():
#     try:
#         df = pd.read_csv("data.csv")
#         # "year_month" is the x-axis label
#         labels = df["year_month"].tolist()
#         # All other columns are languages
#         techs = df.columns.drop("year_month")
#         data = {tech.lower(): df[tech].tolist() for tech in techs}
#         # Also return the list of languages (for dynamic checkboxes)
#         return jsonify({"labels": labels, "data": data, "languages": list(data.keys())})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# Endpoint to return quarterly data from quarterly.csv
@app.route('/api/quarterly-data')
def quarterly_data():
    try:
        df = pd.read_csv("quarterly.csv")
        # "year_quarter" is the x-axis label
        labels = df["year_quarter"].tolist()
        techs = df.columns.drop("year_quarter")
        data = {tech.lower(): df[tech].tolist() for tech in techs}
        return jsonify({"labels": labels, "data": data, "languages": list(data.keys())})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
