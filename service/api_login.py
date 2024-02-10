from flask import Blueprint
from database.model import AreaInfo
from flask_request_validator import *

bp = Blueprint("login", __name__)


@bp.route('/login', methods=['GET', 'POST'], endpoint='login')
@validate_params(
    Param('area', JSON, str),
    Param('areacode', JSON, str),
)
def login(valid: ValidRequest):
    data = valid.get_json()
    result = AreaInfo.query.filter_by(area=data['area'], areacode=data['areacode']).first()
    if not result:
        return '아이디나 비밀번호가 잘못되었습니다.', 403
    return {'area': result.area, 'areacode': result.areacode}, 200
