from time import sleep
from flask import Blueprint, jsonify
from vv_manager import extract_com_error_info, with_vv_connection
from utils import DecodeStatusColor

stoptest_bp = Blueprint('stoptest', __name__)
@stoptest_bp.route('/stoptest', methods=['PUT'])

@with_vv_connection
def stoptest(vv_instance):
    try:
        vv_instance.StopTest()

        for _ in range(50):
            if vv_instance.IsRunning():
                sleep(0.1)
            else:
                break

        status = vv_instance.Status()
        color = DecodeStatusColor(status)

        if vv_instance.IsRunning():
            return jsonify({
                'Status': status,
                'Color': color,
                'Error': 'Test did not stop after multiple attempts.'
            }), 500

        return jsonify({'Status': status, 
                        'Color': color})
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500
