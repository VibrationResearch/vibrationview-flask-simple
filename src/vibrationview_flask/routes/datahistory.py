from flask import Blueprint, jsonify
from vibrationviewapi import vvVector
from utils import  GetVectorData
from vv_manager import extract_com_error_info, with_vv_connection

datahistory_bp = Blueprint('datahistory', __name__)
@datahistory_bp.route('/datahistory', methods=['GET'])

@with_vv_connection
def datahistory(vv_instance):
    try:
        data = GetVectorData(vv_instance, vvVector.TIMEHISTORYAXIS)  
        return jsonify(data)
    except Exception as e:
        return jsonify(extract_com_error_info(e)), 500
