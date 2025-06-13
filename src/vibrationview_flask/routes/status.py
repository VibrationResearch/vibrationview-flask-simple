from flask import Blueprint, jsonify
from utils import DecodeStatusColor
from vv_manager import with_vibrationview

status_bp = Blueprint('status', __name__)

@status_bp.route('/status', methods=['GET'])
@with_vibrationview
def get_vv_status(vv_instance):
    status = vv_instance.Status()
    color = DecodeStatusColor(status)
        
    serialnumber = vv_instance.ReportField('BoxSerialNumber')
    version = vv_instance.ReportField('Version')
    return_color = DecodeStatusColor(status)
    boxcaldate = vv_instance.ReportField('BoxCalDate')
    boxtemp = vv_instance.ReportField('BoxTemp')

    return jsonify({
        'Status': status,
        'Color': color,
        'SerialNumber': serialnumber,
        'Version': version,
        'BoxCalDate': boxcaldate,
        'BoxTemp': boxtemp
    })