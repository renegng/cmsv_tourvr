from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='templates', static_folder='static')

@home.route('/')
def _landing_page():
    return render_template('landing_page.html')

@home.route('/recepcion/')
def _recepcion():
    return render_template('recepcion.html')

@home.route('/orientacion/')
def _orientacion():
    return render_template('orientacion.html')

@home.route('/jardin/')
def _jardin():
    return render_template('jardin.html')

@home.route('/recreo/')
def _recreo():
    return render_template('recreo.html')

@home.route('/cafeteria/')
def _cafeteria():
    return render_template('cafeteria.html')

@home.route('/autonomia-economica/')
def _autonomia_economica():
    return render_template('autonomia_economica.html')

@home.route('/clases-computacion/')
def _clases_computacion():
    return render_template('clases_computacion.html')

@home.route('/cursos-agricultura/')
def _cursos_agricultura():
    return render_template('cursos_agricultura.html')

@home.route('/cursos-cocina/')
def _cursos_cocina():
    return render_template('cursos_cocina.html')

@home.route('/taller-alta-costura/')
def _taller_alta_costura():
    return render_template('taller_alta_costura.html')

@home.route('/taller-emprendedurismo/')
def _taller_emprendedurismo():
    return render_template('taller_emprendedurismo.html')

@home.route('/salud-sexual-reproductiva/')
def _salud_sexual_reproductiva():
    return render_template('salud_sexual_reproductiva.html')

@home.route('/laboratorio-clinico/')
def _laboratorio_clinico():
    return render_template('laboratorio_clinico.html')

@home.route('/ultrasonidos/')
def _ultrasonidos():
    return render_template('ultrasonidos.html')

@home.route('/violencia-genero/')
def _violencia_genero():
    return render_template('violencia_genero.html')

@home.route('/arte-terapia/')
def _arte_terapia():
    return render_template('arte_terapia.html')

@home.route('/atencion-infantil/')
def _atencion_infantil():
    return render_template('atencion_infantil.html')

@home.route('/sala-cunas/')
def _sala_cunas():
    return render_template('sala_cunas.html')

@home.route('/sala-ninos/')
def _sala_ninos():
    return render_template('sala_ninos.html')

@home.route('/sala-pequenos/')
def _sala_pequenos():
    return render_template('sala_pequenos.html')

@home.route('/acercade/')
def _acercade():
    return render_template('acercade.html')

@home.route('/politicaprivacidad/')
def _politicaprivacidad():
    return render_template('politicaprivacidad.html')

@home.route('/terminosdelservicio/')
def _terminosdelservicio():
    return render_template('terminosdelservicio.html')