from flask import Blueprint, jsonify
from utils import ParseVvTable, extract_com_error_info
from vv_manager import with_vibrationview

log_bp = Blueprint('log', __name__)

@log_bp.route('/log', methods=['GET'])
@with_vibrationview
def log(vv_instance):
    try:
        events = vv_instance.ReportField('Events')
        return jsonify(ParseVvTable(events))
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500