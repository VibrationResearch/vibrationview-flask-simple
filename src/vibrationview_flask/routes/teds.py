from flask import Blueprint, jsonify
from vv_manager import with_vv_connection, extract_com_error_info

teds_bp = Blueprint('teds', __name__)

@teds_bp.route('/inputteds', methods=['GET'])
@with_vv_connection
def get_input_teds(vv_instance):
    all_teds_data = []
    num_channels = vv_instance.GetHardwareInputChannels()
    for channel in range(num_channels):
        try:
            teds_info = vv_instance.Teds(channel)
            teds_data = {
                "Channel": channel+1,
                "Teds": teds_info
            }
            all_teds_data.append(teds_data)

        except Exception as e:
            # Extract error information using our common error handler
            error_info = extract_com_error_info(e)
            teds_error = {
                "Channel": channel+1,
                "Error": error_info,
            }
            all_teds_data.append(teds_error)

    return jsonify(all_teds_data)

