# ============================================
#                23/04/2025              
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# UFU - Universidade Federal de Uberlândia
# FEELT31722 - Robótica
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Matheus Pelegrini Bucater
# 11921ECP022
# ---------------------------------------------
# Trabalho 05 - Cinemática Direta (continuação)
# =============================================

from math import cos, sin, pi as PI

import numpy as np
import sys

def print_help():
    """Print a help message"""
    print("uso: python main.py theta1 theta2 d1 a2")
    print(" - theta1      angulo da junta 1")
    print(" - theta2      angulo da junta 2")
    print(" - d1          offset da junta 1")
    print(" - a2          comprimento do elo 2")

def dg_to_rad(dg: float) -> float:
    """Return the converted angle from degree to radians"""
    return (dg * PI) / 180

def convert_args(args: list[str]) -> None:
    """Modify the given args list converting the angles from degrees to radians"""
    arg_name = ["theta1", "theta2", "d1", "a2"]
    for i in range(len(args)):
        arg = args[i]
        try:
            args[i] = float(arg)
        except ValueError:
            print(f"Valor inválido {arg_name[i]}={arg}")
            print_help()
            sys.exit(1)

    args[0] = dg_to_rad(args[0])
    args[1] = dg_to_rad(args[1])

def create_DH_matrix(d: float, theta: float, a: float, alpha: float) -> np.ndarray:
    """Return the Denavit-Hartenberg matrix given the Denavit–Hartenberg parameters"""
    return np.array([
        [ cos(theta), -sin(theta) * cos(alpha),  sin(theta) * sin(alpha), a * cos(theta) ],
        [ sin(theta),  cos(theta) * cos(alpha), -cos(theta) * sin(alpha), a * sin(theta) ],
        [          0,               sin(alpha),               cos(alpha),              d ],
        [          0,                        0,                        0,              1 ]
    ])

if __name__ == "__main__":

    args = sys.argv[1:]

    if "help" in args:
        print_help()
        sys.exit(1)

    if len(args) < 4:
        print(f"4 argumentos esperados, apenas {len(args)} encontrado")
        print_help()
        sys.exit(1)

    convert_args(args)
    [theta1, theta2, d1, a2] = args

    A1 = create_DH_matrix(d1, theta1, 0, dg_to_rad(90))
    A2 = create_DH_matrix(0, theta2, a2, 0)

    A = A1.dot(A2)

    [x, y, z, w] = A[:, 3]

    print(f"(x, y, z) = ({x}, {y}, {z})")
