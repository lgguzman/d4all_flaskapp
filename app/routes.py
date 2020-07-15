from app import app
from flask import Flask, request, jsonify, make_response
import json

tasks = [
    {
        'id': 1,
        'title': 'Data4All',
        'description': 'EC2',
        'done': False
    }
]

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

options = {
    'saber': {'options': [
        {"label": "Saber 11", "value": "saber_11"},
        {"label": "Saber pro", "value": "saber_pro"},
    ],
        'value': 'saber_11'

    },
    'saber_11': {'options': [
        {"label": "Lectura Crítica", "value": "LECTURA_CRITICA"},
        {"label": "Inglés", "value": "INGLES"},
        {"label": "Matemáticas", "value": "MATEMATICAS"},
        {"label": "Sociales Ciudadanas", "value": "SOCIALES_CIUDADANAS"},

    ]

    },
    'saber_pro': {'options': [
        {"label": "Lectura Crítica", "value": "LECTURA_CRITICA:"},
        {"label": "Inglés", "value": "INGLES"},
        {"label": "Razón Cuantitatica", "value": "RAZONA_CUANTITAT"},
        {"label": "Competencia Ciudadanas", "value": "COMPETEN_CIUDADA"},
        {"label": "Comunicación Escrita", "value": "COMUNI_ESCRITA"},
    ]

    },

}


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/api/options', methods=['GET'])
def get_options():
    if request.method == "OPTIONS":  # CORS preflight
        return _build_cors_prelight_response()
    else:
        return _corsify_actual_response(jsonify(options))

@app.route('/api/cluster', methods=['GET'])
def get_clusters():

    with open('/home/ec2-user/data4all/app/data/df.json') as json_file:
        data = json.load(json_file)
        response = {
        "type": "FeatureCollection",
        "features": []
        }
        response["features"] = [{"type": "Feature",
             "properties": {"id": x["index"], "cluster": x["Clus_km"]},
             "geometry": {"type": "Point", "coordinates": [ x["Longitud"],x["Latitud"] ]}
             } for x in data]

        if request.method == "OPTIONS":  # CORS preflight
            return _build_cors_prelight_response()
        else:
            return _corsify_actual_response(jsonify(response))
