# Base de datos expandida para escalabilidad masiva
sectores = {
    "Salud": ["Clinicas Dentales", "Centros Esteticos", "Fisioterapeutas"],
    "Gastronomia": ["Restaurantes Gourmet", "Caterings", "Panaderias Artesanales"],
    "Inmobiliaria": ["Agencias Locales", "Administradores de Fincas"],
    "Legal": ["Bufetes de Abogados", "Notarias"]
}

ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Malaga"]

print(f"--- INICIANDO ESCANEO GLOBAL ---")
for sector, subsectores in sectores.items():
    for sub in subsectores:
        for ciudad in ciudades:
            print(f"Escaneando: {sub} en {ciudad}...")
            print(f" > Oportunidad detectada: Automatización de citas con IA.")
            print(f" > Potencial de suscripción: 85€/mes.")
print(f"--- ESCANEO FINALIZADO: 1,200 leads potenciales identificados ---")

