from time import sleep
from flask import Blueprint, jsonify
from vv_manager import with_vibrationview
from utils import DecodeStatusColor, extract_com_error_info

testcontrol_bp = Blueprint('testcontrol', __name__)

@testcontrol_bp.route('/starttest', methods=['PUT'])
@with_vibrationview
def start_test(vv_instance):
    try:
        vv_instance.StartTest()

        for _ in range(50):
            if vv_instance.IsRunning() == False:
                sleep(0.1)
            else:
                break
        
        status = vv_instance.Status()
        color = DecodeStatusColor(status)

        if vv_instance.IsRunning() == False:
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

@testcontrol_bp.route('/stoptest', methods=['PUT'])
@with_vibrationview
def stop_test(vv_instance):
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

        return jsonify({
            'Status': status, 
            'Color': color
        })
        
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500