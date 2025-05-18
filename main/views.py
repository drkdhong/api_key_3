from flask import Blueprint, jsonify, render_template, request
main = Blueprint("main", __name__, template_folder='templates', url_prefix="/v1")

@main.route('/web')
def index():
    return render_template('main/index.html')

@main.route('/predict', methods=['POST'])
def predict():
    # 요청에서 데이터 추출
    data = request.get_json()
    # 입력값 체크
    if not data or 'features' not in data:
        return jsonify({"error": "Input data missing"}), 400
    try:
        # 예시 입력값: { "features": [5.1, 3.5, 1.4, 0.2] }
        features = data['features']
        return jsonify({'prediction': features})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#curl -X POST http://localhost:5000/v1/predict -H "Content-Type:application/json" -d "{\"features\": [5.1,3.5,1.4,0.2]}"
