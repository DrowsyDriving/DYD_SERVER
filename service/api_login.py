from flask import Blueprint, request, session
from database.model import AreaInfo
bp = Blueprint("login", __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    result = AreaInfo.query.filter_by(area=data['area'], areacode=data['areacode']).first()
    if not result:
        return {"message": "로그인에 실패했습니다.", "success": False}, 401
    session['area'] = data['area']
    return {"message": "로그인에 성공했습니다.", "success": True}, 200


@bp.route('/logout', methods=['GET'])
def logout():
    if request.method == "GET":
        session.pop('area')
        return {"message": "로그아웃에 성공했습니다."}, 200
    return {"message": "로그아웃에 실패했습니다."}, 400
