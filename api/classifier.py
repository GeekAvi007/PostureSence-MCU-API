
# Testing
def classify_posture(pose_data):
    # Simple rule-based classification
    if pose_data["slouching"]:
        posture = "slouch"
        attention = False
        confidence = 0.85
    elif pose_data["head_tilt"] > 20:
        posture = "distracted"
        attention = False
        confidence = 0.75
    else:
        posture = "attentive"
        attention = True
        confidence = 0.95

    return {
        "posture": posture,
        "attention": attention,
        "confidence": confidence
    }
