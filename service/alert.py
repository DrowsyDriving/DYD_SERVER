from flask import Blueprint, request, jsonify
from database.orm import AlertInfo
from database.connection import db_session
bp = Blueprint('alert', __name__)


@bp.route('/alert', methods=['GET', 'POST'])
def alert():
    with db_session() as session:
        if request.method == "POST":  # 알람 저장
            info = request.get_json()
            warning_level = session.query(
                AlertInfo
            ).order_by(
                AlertInfo.id.desc()
            ).where(
                AlertInfo.car_number == str(info['car_number'])
            ).first()

            level = 1
            if warning_level:
                level = warning_level.warning_level % 3 + 1

            a = AlertInfo.create(
                info['car_number'],
                level,
                info['latitude'],
                info['longitude'],
            )

            session.add(a)
            session.commit()

            return str(a.warning_level)

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
