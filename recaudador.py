# Motor de gestión de pagos automatizados
leads_ganados = ["Clinica Dental Central", "Restaurante Gourmet", "Abogados Madrid"]

print("--- INICIANDO PROCESAMIENTO DE COBROS ---")
for lead in leads_ganados:
    enlace = f"https://pago.ia-automatizada.com/checkout?cliente={lead.replace(' ', '_')}"
    print(f"Estado: Propuesta enviada a {lead}")
    print(f"Enlace de suscripción de 85€ generado: {enlace}")
    print("-" * 20)

print("Sistema de recaudación listo para operar.")
