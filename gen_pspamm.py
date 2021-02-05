import os
import subprocess


os.remove("pspamm.h") if os.path.exists("pspamm.h") else None
os.remove("pspamm.cpp") if os.path.exists("pspamm.cpp") else None
os.remove("pspamm2.h") if os.path.exists("pspamm2.h") else None
os.remove("pspamm2.cpp") if os.path.exists("pspamm2.cpp") else None

include_guard = """#ifndef PSPAMM_H
# define PSPAMM_H
# endif\n\n"""

include_guard2 = """#ifndef PSPAMM2_H
# define PSPAMM2_H
# endif\n\n"""

with open("pspamm.h", "a") as f:
    f.write(include_guard)
with open("pspamm.cpp", "a") as f:
    f.write("#include \"pspamm.h\"")
    f.write("\n\n")
with open("pspamm2.h", "a") as f:
    f.write(include_guard2)
with open("pspamm2.cpp", "a") as f:
    f.write("#include \"pspamm2.h\"")
    f.write("\n\n")

for MAT_DIM in range(2, 61, 2):
    with open("pspamm.cpp", "a") as f:
        mat_dim_str = str(MAT_DIM)
        result = subprocess.run(
            ['./pspamm.py', mat_dim_str,mat_dim_str,mat_dim_str ,mat_dim_str,mat_dim_str ,mat_dim_str, "1" , "0" ,"--arch", "arm", '--output_funcname' ,f'pspamm{MAT_DIM}x{MAT_DIM}'], stdout=subprocess.PIPE)
        f.write(result.stdout.decode('utf-8'))
        f.write('\n\n')

    with open("pspamm.h","a") as f:
        f.write(f'void pspamm{MAT_DIM}x{MAT_DIM} (const double* A, const double* B, double* C, double alpha, double beta, const double* prefetch);')
        f.write('\n\n')
    
    print(f'{MAT_DIM}x{MAT_DIM} generated!')


for MAT_DIM in range(62, 101, 2):
    with open("pspamm2.cpp", "a") as f:
        result = subprocess.run(
            ['./pspamm.py', mat_dim_str,mat_dim_str,mat_dim_str ,mat_dim_str,mat_dim_str ,mat_dim_str, "1" , "0" ,"--arch", "arm", '--output_funcname' ,f'pspamm{MAT_DIM}x{MAT_DIM}'], stdout=subprocess.PIPE)
        f.write(result.stdout.decode('utf-8'))
        f.write('\n\n')
        
    with open("pspamm2.h","a") as f:
        f.write(f'void pspamm{MAT_DIM}x{MAT_DIM} (const double* A, const double* B, double* C, double alpha, double beta, const double* prefetch);')
        f.write('\n\n')
    print(f'{MAT_DIM}x{MAT_DIM} generated!')
