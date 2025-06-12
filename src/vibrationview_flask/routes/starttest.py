from time import sleep
from flask import Blueprint, jsonify
from vv_manager import extract_com_error_info, with_vv_connection
from utils import DecodeStatusColor

starttest_bp = Blueprint('starttest', __name__)
@starttest_bp.route('/starttest', methods=['PUT'])

@with_vv_connection
def start(vv_instance):
    try:
        vv_instance.StartTest()

        for _ in range(50):
            if vv_instance.IsRunning()==False:
                sleep(0.1)
            else:
                break
        
        status = vv_instance.Status()
        color = DecodeStatusColor(status)

        if vv_instance.IsRunning()==False:
            return jsonify({
                'Status': status['stop_code'],
                'Code': status['stop_code_index'],
                'Color': color,
                'Error': 'Test did not start after multiple attempts.'
            }), 500
        
        return jsonify({
            'Status': status,
            'Color': color,
        })

    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500

