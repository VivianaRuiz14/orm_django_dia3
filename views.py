from django.shortcuts import redirect, render

def counter(req):
    # preguntamos si ya existe la variable
    veces = req.session.get('veces', None)
    #si es la primera vez que accede iniciamos de 0
    if veces is None:
        veces = 0
    # le sumamos 1 a la cantidad de visitas de ese usuario
    veces += 1
    # lo guardamos en sesion
    req.session['veces'] = veces
    return render(req,'counter.html')

def reset_counter(req):
    req.session['veces']=0
    return redirect('/counter')
