from src.DataBase.JsonDataBase import JsonDataBase
import os
import json
import pytest

def test_01_se_crea_un_json_si_no_lo_hay_en_la_ubicacion_designada(tmp_path):
	temp_dir = tmp_path / "tests_folder"
	temp_dir.mkdir()
	ubicacion_designada = temp_dir / 'test_data.json'
	db = JsonDataBase(str(ubicacion_designada))

	assert os.path.exists(ubicacion_designada) == True
	with open(ubicacion_designada, "r") as f:
		contenido = json.load(f)
	assert contenido == {"tasks": [], "items":0}

# def test_02_un_json_vacio_no_da_items():
	
# def test_03_un_json_con_un_item_devuelve_un_item_correctamente():
    
# def test_04_agregar_un_item_lo_escribe_en_el_destino_indicado():

# def test_05_
	