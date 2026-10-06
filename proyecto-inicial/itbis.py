"""Cálculos de ITBIS (Impuesto a la Transferencia de Bienes Industrializados y Servicios).

Tasa general en República Dominicana: 18 %.

Este archivo contiene un error intencional para el taller.
"""

TASA_ITBIS = 0.18


def calcular_itbis(monto: float) -> float:
    """Devuelve el ITBIS de un monto sin impuesto."""
    return round(monto * TASA_ITBIS, 2)


def total_con_itbis(monto: float) -> float:
    """Devuelve el monto más su ITBIS."""
    return round(monto + calcular_itbis(monto), 2)


def desglosar_itbis(total: float) -> dict:
    """Separa un total que YA incluye ITBIS en base imponible e impuesto."""
    base = round(total * (1 - TASA_ITBIS), 2)
    return {"base": base, "itbis": round(total - base, 2)}
