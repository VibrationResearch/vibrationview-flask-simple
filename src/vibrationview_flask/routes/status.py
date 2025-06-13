from flask import Blueprint, jsonify
from utils import DecodeStatusColor
from vv_manager import with_vv_connection

status_bp = Blueprint('status', __name__)

@status_bp.route('/status', methods=['GET'])
@with_vv_connection
def get_vv_status(vv_instance):
    status = vv_instance.Status()
    serialnumber = vv_instance.ReportField('BoxSerialNumber')
    version = vv_instance.ReportField('Version')
    return_color = DecodeStatusColor(status)
    boxcaldate = vv_instance.ReportField('BoxCalDate')
    boxtemp = vv_instance.ReportField('BoxTemp')

    return jsonify({
        'StopCode': status['stop_code'],
        'StopCodeIndex': status['stop_code_index'],
        'Color': return_color,
        'SerialNumber': serialnumber,
        'Version': version,
        'BoxCalDate': boxcaldate,
        'BoxTemp': boxtemp
    })
