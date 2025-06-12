from flask import Blueprint, jsonify
from utils import DecodeStatusColor, GetVectorData
from vv_manager import extract_com_error_info, with_vv_connection

datafreq_bp = Blueprint('datafreq', __name__)
@datafreq_bp.route('/datafreq', methods=['GET'])

@with_vv_connection
def dataFreq(vv_instance):
    try:
        data = GetVectorData(vv_instance, 100)  # VV_FREQUENCYAXIS
        return jsonify(data)
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500

