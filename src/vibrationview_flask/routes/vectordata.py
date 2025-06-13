from flask import Blueprint, jsonify
from vibrationviewapi import vvVector
from utils import GetVectorData, extract_com_error_info
from vv_manager import with_vibrationview

vectordata_bp = Blueprint('vectordata', __name__)

@vectordata_bp.route('/datafreq', methods=['GET'])
@with_vibrationview
def data_freq(vv_instance):
    try:
        data = GetVectorData(vv_instance, 100)  # VV_FREQUENCYAXIS
        return jsonify(data)
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500

@vectordata_bp.route('/datahistory', methods=['GET'])
@with_vibrationview
def data_history(vv_instance):
    try:
        data = GetVectorData(vv_instance, vvVector.TIMEHISTORYAXIS)  
        return jsonify(data)
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500

@vectordata_bp.route('/datatime', methods=['GET'])
@with_vibrationview
def data_time(vv_instance):
    if not vv_instance:
        return jsonify({'Error': 'Could not connect to VibrationVIEW'}), 500
    try:
        data = GetVectorData(vv_instance, 0)  # VV_WAVEFORMAXIS
        return jsonify(data)
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500