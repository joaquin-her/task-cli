from src.DataBase.JsonDataBase import JsonDataBase
from datetime import datetime
import os
import json
import pytest

"""@pytest.fixture
def create_test_dir():
"""

def test_01_se_crea_un_json_si_no_lo_hay_en_la_ubicacion_designada(tmp_path):
	"""Se define una ruta para almacenar la informacion, si la ruta esta vacia se crea un archivo alli"""

	temp_dir = tmp_path / "tests_folder"
	temp_dir.mkdir()
	ubicacion_designada = temp_dir / 'test_data.json'

	assert os.path.exists(ubicacion_designada) == False
	db = JsonDataBase(str(ubicacion_designada))
	assert os.path.exists(ubicacion_designada) == True

	with open(ubicacion_designada, "r") as f:
		contenido = json.load(f)
	assert contenido == {"tasks": [], "items":0}

def test_02_un_json_vacio_no_da_items(tmp_path):
	"""Se crea un archivo con el formato a utilizar en la ubicacion designada y su lectura devuelve una lista vacia"""
	temp_dir = tmp_path / "tests_folder"
	temp_dir.mkdir()
	ubicacion_designada = temp_dir / 'test_data.json'
	with open(ubicacion_designada, "w")as file:
		json_vacio = {"tasks":[],"items":0}
		json.dump(json_vacio, file)
	
	db = JsonDataBase(str(ubicacion_designada))
	assert len(db.getItems()) == 0
	
def test_03_se_puede_agregar_un_item(tmp_path):
	db = crearDBVacia(tmp_path)

	db.add("Leer 1 capitulo de Algebra Lineal")
	items_obtenidos = db.getItems()

	assert len(items_obtenidos) == 1


def test_04_el_item_agregado_se_devuelve_correctamente(tmp_path):
	"""Se evalua que los elementos tengan los campos correspondientes al ser aniadidos"""
	db = crearDBVacia(tmp_path)
	descripcion_esperada = "Estudiar para parcial de Analisis"
	id_esperado = 0
	status_esperado = "to-do"
	created_time_esperado = datetime.now()
	updated_time_esperado = created_time_esperado

	db.add("Estudiar para parcial de Analisis")
	item_aniadido = db.getItems()[0]

	assert item_aniadido["description"] == descripcion_esperada
	assert item_aniadido["id"] == id_esperado
	assert item_aniadido["status"] == status_esperado
	assert item_aniadido["created"] == created_time_esperado.isoformat()
	assert item_aniadido["updated"] == updated_time_esperado.isoformat()

def test_05_la_cantidad_de_items_incrementa_al_aniadir_elementos(tmp_path):
	"""Se evalua que el contador de id continue creciendo"""
	db = crearDBVacia(tmp_path)
	cantidad_esperada = 3

	db.add("Estudiar para parcial de Analisis")
	db.add("Leer 1 capitulo de Algebra Lineal")
	db.add("Hacer un proyecto con python")

	cantidad_obtenida = db.getLastId()
	assert cantidad_esperada == cantidad_obtenida

def test_06_se_puede_modificar_el_estado_de_una_tarea(tmp_path):
	"""Se evalua que se pueda modificar el campo 'status' de las tareas """
	db = crearDBVacia(tmp_path)
	db.add("Leer 1 capitulo de Algebra Lineal")
	db.updateStatus(0, "done")
	item_modificado = db.getItems()[0]

	assert item_modificado["status"] == "done"

def test_07_al_modificar_se_actualiza_el_campo_updated(tmp_path):
	"""Se evalua que se actualice el timestamp de cuando fue modificado por ultima vez la tarea"""
	db = crearDBVacia(tmp_path)
	db.add("Hacer un proyecto con python")
	db.add("Estudiar para parcial de Analisis")
	
	db.updateStatus(1, "done")
	updated_time_esperado = datetime.now()
	item_modificado = db.getItems()[1]

	assert item_modificado["descrripcion"] == "Estudiar para parcial de Analisis"
	assert item_modificado["status"] == "done"
	assert item_modificado["created"] != item_modificado["updated"]
	assert item_modificado["updated"] == updated_time_esperado.isoformat()

def test_08_se_puede_eliminar_un_item(tmp_path):
	"""Se evalua que los elementos puedan ser eliminados correctamente"""
	db = crearDBVacia(tmp_path)

	db.add("Leer 1 capitulo de Algebra Lineal")
	db.removeItem(0)
	items_obtenidos = db.getItems()

	assert len(items_obtenidos) == 0

def test_09_eliminar_de_archivo_destino(tmp_path):
	"""Se evalua que el elemento pueda ser eliminado del archivo destino """
	
	temp_dir = tmp_path / "tests_folder"
	temp_dir.mkdir()
	ubicacion_designada = temp_dir / 'test_data.json'
	with open(ubicacion_designada, "w")as file:
		json_con_elementos = {"tasks":[{
			"id": 0,
			"description": "Practicar programacion",
			"status": "to-do",
			"created": "2025-03-26",
			"updated": "2025-03-26"
		},{
			"id": 1,
			"description": "Estudiar algebra lineal",
			"status": "to-do",
			"created": "2025-03-26",
			"updated": "2025-03-26"
		}],"items":2}
		json.dump(json_con_elementos, file)
	db = JsonDataBase(str(ubicacion_designada))
	db.removeItem(0)

	with open(ubicacion_designada, "r" ) as file:
		json_obtenido = json.load(file)
		
	json_esperado = {"tasks":[{
		"id": 1,
		"description": "Estudiar algebra lineal",
		"status": "to-do",
		"created": "2025-03-26",
		"updated": "2025-03-26"
	}],"items":1}

	assert json_obtenido == json_esperado

def test_10_elminar_un_elemento_no_resta_a_la_cantidad_de_ids(tmp_path):
	"""Se evalua que eliminar elementos no disminuya la cantidad de ids del contador del db"""
	assert False

def test_11_pedir_un_elemento_que_no_existe_arroja_una_excepcion(tmp_path):
	"""Se evalua que si se intenta obtener un elemento que no esta dentro de la informacion cargada o aniadida, una excepcion es lanzada"""
	assert False

def test_12_se_puede_filtrar_las_tareas_por_status_done(tmp_path):
	"""Se evalua que se obtengan correctamente las tareas ya completadas de la db"""
	assert False

def test_13_se_puede_filtrar_las_tareas_por_status_to_do(tmp_path):
	"""Se evalua que se obtengan correctamente las tareas en 'to-do de la db"""
	assert False

def test_14_se_puede_filtrar_las_tareas_por_status_in_progress(tmp_path):
	"""Se evalua que se obtengan correctamente las tareas en 'in-progress de la db"""
	assert False
	
def crearDBVacia(tmp_path):
	temp_dir = tmp_path / "tests_folder"
	temp_dir.mkdir()
	ubicacion_designada = tmp_path / "test_data.json"

	db = JsonDataBase(str(ubicacion_designada))
	return db
