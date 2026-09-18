#!/usr/bin/env python3
"""
Script utilitario para clasificar atributos en la Matriz de Cuadrantes (IPA / CIER)
y calcular desgloses estadísticos de microdatos (% Negativas, % Neutras, % Positivas, Nota Media).
"""

import json
import argparse
import sys

def classify_quadrant(importance, performance, imp_cutoff=3.33, perf_cutoff=64.8):
    """
    Clasifica un atributo en los 4 cuadrantes estándar según importancia y desempeño.
    """
    if importance >= imp_cutoff:
        if performance >= perf_cutoff:
            return {
                "id": "mantener",
                "nombre": "Fortalezas Clave",
                "cuadrante": "Cuadrante II",
                "color": "#10b981",
                "prioridad_tipo": "Mantener / Blindar"
            }
        else:
            return {
                "id": "urgente",
                "nombre": "Foco Urgente",
                "cuadrante": "Cuadrante I",
                "color": "#ef4444",
                "prioridad_tipo": "Prioridad Máxima"
            }
    else:
        if performance >= perf_cutoff:
            return {
                "id": "eficiencia",
                "nombre": "Ventajas Secundarias",
                "cuadrante": "Cuadrante III",
                "color": "#3b82f6",
                "prioridad_tipo": "Mantener Eficiencia"
            }
        else:
            return {
                "id": "secundario",
                "nombre": "Baja Prioridad",
                "cuadrante": "Cuadrante IV",
                "color": "#94a3b8",
                "prioridad_tipo": "Monitoreo"
            }

def calculate_ratings_breakdown(ratings_list):
    """
    Calcula desglose porcentual de escala Likert 1-10:
    - Negativas: 1 a 4
    - Neutras: 5 a 7
    - Positivas: 8 a 10
    """
    valid = [r for r in ratings_list if r is not None and 1 <= r <= 10]
    total = len(valid)
    if total == 0:
        return {"neg": 0.0, "neu": 0.0, "pos": 0.0, "mean": 0.0, "n": 0}
        
    neg = sum(1 for r in valid if 1 <= r <= 4)
    neu = sum(1 for r in valid if 5 <= r <= 7)
    pos = sum(1 for r in valid if 8 <= r <= 10)
    mean_val = sum(valid) / total
    
    return {
        "neg": round((neg / total) * 100, 2),
        "neu": round((neu / total) * 100, 2),
        "pos": round((pos / total) * 100, 2),
        "mean": round(mean_val, 2),
        "n": total
    }

def main():
    print("Módulo de clasificación de cuadrantes y cálculo de microdatos cargado correctamente.")

if __name__ == "__main__":
    main()
