from flask import Blueprint, jsonify
from utils import ParseVvTable
from vv_manager import extract_com_error_info, with_vv_connection


log_bp = Blueprint('log', __name__)
@log_bp.route('/log', methods=['GET'])

@with_vv_connection
def log(vv_instance):
    try:
        events = vv_instance.ReportField('Events')
        return jsonify(ParseVvTable(events))
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500
