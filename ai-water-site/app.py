from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

REQUESTS_PER_SECOND = 28935

WATER_PER_REQUEST = 0.0003  
CO2_PER_REQUEST = 7.3 / 1000  
ENERGY_PER_REQUEST = 18.35 / 1000  


WATER_PER_SECOND = REQUESTS_PER_SECOND * WATER_PER_REQUEST
CO2_PER_SECOND = REQUESTS_PER_SECOND * CO2_PER_REQUEST
ENERGY_PER_SECOND = REQUESTS_PER_SECOND * ENERGY_PER_REQUEST * 3.6  # convert to GJ


BUCKET = 10
BOTTLE = 1.5
BATHTUB = 150
TRUCK = 30000
POOL = 2500000

BAIKAL = 2.3615e16
ATLANTIC = 3.1e20
PACIFIC = 7.1e20

start_time = time.time()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/stats")
def stats():

    elapsed = time.time() - start_time

    total_water = 10 + elapsed * WATER_PER_SECOND
    total_co2 = elapsed * CO2_PER_SECOND
    total_energy = elapsed * ENERGY_PER_SECOND

    return jsonify({

        "water": total_water,
        "co2": total_co2,
        "energy": total_energy,

        "buckets": total_water / BUCKET,
        "bottles": total_water / BOTTLE,
        "bathtubs": total_water / BATHTUB,
        "trucks": total_water / TRUCK,
        "pools": total_water / POOL,

        "baikal_percent": total_water / BAIKAL * 100,
        "atlantic_percent": total_water / ATLANTIC * 100,
        "pacific_percent": total_water / PACIFIC * 100

    })


if __name__ == "__main__":
    app.run(debug=True)