from flask import Blueprint, jsonify
from utils import get_channel_data
from vv_manager import with_vibrationview

pretest_bp = Blueprint('pretest', __name__)

@pretest_bp.route('/channelpretest', methods=['GET'])
@with_vibrationview
def get_channel_pretest(vv_instance):
    field_keys = [
        'ChName', 'pretest_SNR', 'pretest_channel', 'pretest_ChannelLimit', 'pretest_ChannelAbort'
    ]

    channels = get_channel_data(vv_instance, field_keys)
    return jsonify(channels)