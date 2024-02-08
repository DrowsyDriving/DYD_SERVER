from flask import Blueprint, request, jsonify
from database.orm import AreaInfo
from database.connection import db_session
from sqlalchemy import select
bp = Blueprint('login', __name__)
# 로그인 보안 강화


@bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    with db_session() as session:
        if request.method == 'POST':
            info = request.get_json()
            area = AreaInfo.create(info['area'], info['areacode'])
            session.add(area)
            session.commit()
            return jsonify(info)
        return {'error': '오류가 발생했습니다.'}


@bp.route('/log-in', methods=["POST"])
def log_in():
    with db_session() as session:
        if request.method == 'POST':
            login = request.get_json()
            result = session.scalar(select(AreaInfo).where(AreaInfo.area == str(login['area'])))
            if not result:
                return {'error': '아이디나 비밀번호가 잘못되었습니다.'}
            elif result.areacode != str(login['areacode']):
                return {'error': '아이디나 비밀번호가 잘못되었습니다.'}
            return {'area': result.area, 'areacode': result.areacode}

        return {'error': '오류 발생'}
