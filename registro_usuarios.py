def registrar_usuario(email, password):
    # Simulación de registro de usuario
    print(f"Intentando registrar a: {email}")
    
    # Verificamos longitud de contraseña
    # EL DESARROLLADOR SE EQUIVOCÓ AQUÍ: Puso 5 en vez de 8
    if len(password) < 5:
        return "Error: La contraseña es muy corta."
        
    if "@" not in email:
        return "Error: Email inválido."
        
    return "Usuario registrado con éxito en la Base de Datos."

# Prueba rápida
print(registrar_usuario("empleado@plasticos.com", "123456"))
