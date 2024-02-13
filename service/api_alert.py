from flask import Blueprint, request
from database.model import db, AlertInfo
bp = Blueprint('alert', __name__, url_prefix='/alert')


@bp.route('/save', methods=["GET", "POST"])
def save_alert():
    if request.method == "POST":
        data = request.get_json()
        if not data['car_number'] or not data['latitude'] or not data['longitude']:
            return {"error": "정보가 잘못되었습니다."}, 400
        a = AlertInfo()
        a.car_number = data['car_number']
        a.latitude = data['latitude']
        a.longitude = data['longitude']
        a.warning_level = 1
        level = AlertInfo.query.filter_by(car_number=data['car_number']).order_by(AlertInfo.id.desc()).first()
        if level:
            a.warning_level = level.warning_level % 3 + 1
        db.session.add(a)
        db.session.commit()
        return {"car_number": "차량 번호", "warning_level": "경고 단계"}, 201
    return {"error": "오류가 발생했습니다."}, 400


@bp.route('/show', methods=["GET"])
def show_alert():
    if request.method == "GET":
        records = AlertInfo.query.order_by(AlertInfo.id.desc()).limit(4)
        results = list()
        for record in records:
            results.append(
                {
                    'car_number': record.car_number,
                    'warning_level': record.warning_level,
                    'latitude': record.latitude,
                    'longitude': record.longitude,
                    'occurrence_time': record.occurrence_time,
                }
            )
        return results, 200
    return {'error': "정보를 찾을 수 없습니다."}, 404


@bp.route('/dummy', methods=['GET'])
def dummy():
    for i in range(100):
        a = AlertInfo()
        a.car_number = f'{i}나{i}'
        a.warning_level = i % 3 + 1
        a.latitude = i + i / 10
        a.longitude = i + i / 10
        db.session.add(a)
    return 'dummy 데이터 생성 완료'
