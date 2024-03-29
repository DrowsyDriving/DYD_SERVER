from flask import Blueprint, request
from database.model import AreaInfo
bp = Blueprint("login", __name__, url_prefix='/users')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        data = request.get_json()
        result = AreaInfo.query.filter_by(area=data['area'], areacode=data['areacode']).first()
        if not result:
            return {"message": "로그인에 실패했습니다.", "success": False}, 401
        return {"message": "로그인에 성공했습니다.", "success": True}, 200
    return {"message": "오류가 발생했습니다."}, 400


@bp.route('/logout', methods=['GET'])
def logout():
    if request.method == "GET":
        return {"message": "로그아웃에 성공했습니다."}, 200
    return {"message": "로그아웃에 실패했습니다."}, 400
