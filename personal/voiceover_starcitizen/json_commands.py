import json

default_config: dict = {
    "commands": [
        {
            "name": "Tren de aterrizaje",
            "info": "Despliega o repliega el tren de aterrizaje",
            "input": "n",
            "modifier": 0,
            "mode": 0
        },
        {
            "name": "Modo crucero",
            "info": "Activa o desactiva la velocidad de crucero",
            "input": "c",
            "modifier": 0,
            "mode": 0
        },
        {
            "name": "Motor de salto",
            "info": "Inicia el modo 'Quantum Travel'",
            "input": "b",
            "modifier": 0,
            "mode": 0
        },
        {
            "name": "Salto cuántico",
            "info": "Con el motor de salto cargado, viaja al objetivo frontal",
            "input": "b",
            "modifier": 0,
            "mode": 1
        },
        {
            "name": "Energía",
            "info": "Enciende o apaga la energía de la nave por completo",
            "input": "u",
            "modifier": 0,
            "mode": 0
        },
        {
            "name": "Motores",
            "info": "Enciende o apaga los motores principales",
            "input": "i",
            "modifier": 0,
            "mode": 0
        }
    ]
}


def load_json():
    try:
        with open('commands.json') as file:
            return json.load(file)["commands"]
    except:
        save_json(default_config)
        load_json()


def save_json(data: dict):
    json_data = json.dumps(data, indent=4)
    with open('commands.json', 'w') as file:
        file.write(json_data)
