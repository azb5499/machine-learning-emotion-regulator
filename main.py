from flask import Flask, jsonify, request
from models import init_db
from units.record_service import RecordService
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Initialize the database
init_db(app)

@app.route("/")
def home():
    return "This is home"

@app.route("/records", methods=["GET"])
def get_records():
    records = RecordService.get_records()
    return jsonify([{
        "record_id": record.record_id,
        "emotion_name": record.emotion_name,
        "likelihood_score": record.likelihood_score,
        "colour_displayed": record.colour_displayed,
        "record_date": record.record_date,
        "colour_match": record.colour_match
    } for record in records])

@app.route("/records/<int:record_id>", methods=["GET"])
def get_record_by_id(record_id):
    record = RecordService.find_record_by_id(record_id)
    if record:
        return jsonify({
            "record_id": record.record_id,
            "emotion_name": record.emotion_name,
            "likelihood_score": record.likelihood_score,
            "colour_displayed": record.colour_displayed,
            "record_date": record.record_date,
            "colour_match": record.colour_match
        })
    return jsonify({"error": "Record not found"}), 404

@app.route("/records", methods=["POST"])
def create_record():
    data = request.json
    new_record = RecordService.add_record(
        emotion_name=data.get("emotion_name"),
        likelihood_score=data.get("likelihood_score"),
        colour_displayed=data.get("colour_displayed"),
        record_date=date.fromisoformat(data.get("record_date")),
        colour_match=data.get("colour_match")
    )
    return jsonify({
        "record_id": new_record.record_id,
        "emotion_name": new_record.emotion_name,
        "likelihood_score": new_record.likelihood_score,
        "colour_displayed": new_record.colour_displayed,
        "record_date": new_record.record_date,
        "colour_match": new_record.colour_match
    }), 201

@app.route("/records/<int:record_id>", methods=["PUT"])
def update_record(record_id):
    data = request.json
    updated_record = RecordService.update_record(
        record_id,
        emotion_name=data.get("emotion_name"),
        likelihood_score=data.get("likelihood_score"),
        colour_displayed=data.get("colour_displayed"),
        record_date=date.fromisoformat(data.get("record_date")),
        colour_match=data.get("colour_match")
    )
    if updated_record:
        return jsonify({
            "record_id": updated_record.record_id,
            "emotion_name": updated_record.emotion_name,
            "likelihood_score": updated_record.likelihood_score,
            "colour_displayed": updated_record.colour_displayed,
            "record_date": updated_record.record_date,
            "colour_match": updated_record.colour_match
        })
    return jsonify({"error": "Record not found"}), 404

@app.route("/records/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    if RecordService.delete_record(record_id):
        return jsonify({"message": "Record deleted successfully"})
    return jsonify({"error": "Record not found"}), 404

if __name__ == "__main__":
    app.run()
