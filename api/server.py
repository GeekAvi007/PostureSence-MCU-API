# Flask API to serve posture data as JSON
from flask import Flask, jsonify
from pose_detection import detect_pose
from classifier import classify_posture

app = Flask(__name__)

@app.route("/posture")
def posture():
    pose_data = detect_pose()
    result = classify_posture(pose_data)
    return jsonify(result)

# ✅ THIS PART IS IMPORTANT
if __name__ == "__main__":
    app.run(debug=True)
