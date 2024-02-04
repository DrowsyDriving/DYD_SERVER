from flask import Blueprint, request, jsonify
from database.orm import AlertInfo
from database.connection import db_session
bp = Blueprint('alert', __name__)


@bp.route('/alert', methods=['GET', 'POST'])
def alert():
    with db_session() as session:
        if request.method == "POST":  # 알람 저장
            info = request.get_json()
            a = AlertInfo.create(
                info['car_number'],
                info['warning_level'],
                info['latitude'],
                info['longitude'],
            )
            session.add(a)
            session.commit()
            session.refresh(a)
            return jsonify(info)
        elif request.method == "GET":
            records = session.query(AlertInfo).order_by(AlertInfo.id.desc()).limit(4)
            result = list()
            for record in records:
                result.append(
                    {
                        'car_number': record.car_number,
                        'warning_level': record.warning_level,
                        'latitude': record.latitude,
                        'longitude': record.longitude,
                        'occurrence_time': record.occurrence_time,
                    }
                )
            return result
        return {'error': '오류 발생'}


@bp.route('/dummy', methods=['GET'])
def dummy():
    with db_session() as session:
        for i in range(100):
            a = AlertInfo.create(
                car_number=f'{i}가{i}',
                warning_level=i % 3 + 1,
                latitude=i,
                longitude=i,
            )
            session.add(a)
        session.commit()
        return {'dummy': "생성 완료"}
