from flask import Blueprint, jsonify
from utils import GetVectorData
from vv_manager import extract_com_error_info, with_vv_connection

datatime_bp = Blueprint('datatime', __name__)
@datatime_bp.route('/datatime', methods=['GET'])

@with_vv_connection
def dataTime(vv_instance):
    if not vv_instance:
        return jsonify({'Error': 'Could not connect to VibrationVIEW'}), 500
    try:
        data = GetVectorData(vv_instance, 0)  # VV_WAVEFORMAXIS
        return jsonify(data)
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500

