def replace_domain(email, old_domain, new_domain): #Primero definimos la funcion replace_domain
    if "@" + old_domain in email: #Comprobamos si en la concatenacion de @ + old domain se encuentra en la direccion de correo que introduzcamos
        index = email.index("@" + old_domain) #Si el if es true comprobamos y asignamos a index el valor concatenado
        new_email = email[:index] + "@" + new_domain#A new_email le asignamos index mas la concatenacion de @ con new_domain
        return new_email
    return email