from flask import Flask, render_template, request
from model.predict import predict_air_quality
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        pm25 = float(request.form["pm25"])
        pm10 = float(request.form["pm10"])
        no2 = float(request.form["no2"])
        so2 = float(request.form["so2"])
        co = float(request.form["co"])
        o3 = float(request.form["o3"])

        # Get predictions
        aqi, category, health_msg = predict_air_quality(pm25, pm10, no2, so2, co, o3)

        # For charts (JSON sent to HTML)
        chart_data = {
            "labels": ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"],
            "values": [pm25, pm10, no2, so2, co, o3],
            "aqi": aqi
        }

        return render_template(
            "result.html",
            aqi=round(aqi, 2),
            category=category,
            health_msg=health_msg,
            chart_data=json.dumps(chart_data)
        )

    except Exception as e:
        return render_template("result.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/result')
def result():
    # Your AQI calculation logic here
    return render_template('result.html', 
                         aqi=calculated_aqi,
                         category=aqi_category,
                         health_msg=health_message,
                         pm25=pm25_value,
                         pm10=pm10_value,
                         no2=no2_value,
                         so2=so2_value,
                         co=co_value,
                         o3=o3_value,
                         chart_data=chart_data)