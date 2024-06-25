from dia3.models import tarea, subtarea

def crear_nuevatarea(descripcion):
    t = tarea (descripcion=descripcion)
    t.save()
    imprimir_en_pantalla()
    
def crear_sub_tarea(descripcion: str, idtarea):
    t = tarea.object.get(id=idtarea)
    st = subtarea(descripcion=descripcion, tarea = t)
    st.save()
    
def elimina_tarea(idtarea: int):
    t = tarea.objects.get(id= idtarea)
    t.eliminada = True
    t.save()
    

def elimina_subtarea(idsubtarea:int):
    st = subtarea.objects.get(id=idsubtarea)
    st.eliminada = True
    st.save()
    

def imprimir_en_pantalla():
    tareas = recupera_tareas_y_sub_tareas()
    for t in tareas:
        print (f'[{t.id}] {t.descripcion}')
        for sub_tarea in t.subtareas.filter(eliminada=False):
            print(f'[{sub_tarea.id} {sub_tarea.descripcion}')
            
def recupera_tareas_y_sub_tareas():
    tareas = tareas.objects.filter(eliminada= False)
    return tareas