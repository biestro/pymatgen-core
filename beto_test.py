"""
Test for the LOCPROJ string and WANNIER90_WIN strings

# TODO: Outcar magnetization for LSORBIT=T
"""

# from src.pymatgen.io.vasp import Incar
from src.pymatgen.io.vasp import Incar
from collections import defaultdict
# from .pymatgen.io.vasp import Outcar

if __name__ == "__main__":
    incar = Incar.from_file("test-files/core/locproj/INCAR_win")
    # incar_new = incar.copy()
    # incar_new['WANNIER90_WIN'] = {'kmesh_tol': 1e-5, 'write_xyz': True}
    # print()
    # print(incar_new)
    # incar_new.write_file("test-files/core/locproj/INCAR_out")
