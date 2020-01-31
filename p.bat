REM 10 years, 36% per year...
REM py compound.py -pv 1000 -f "1.36" -n 10 2>&1 | tee p.out
REM py split_thousands.py 2>&1 | tee p.out
REM py compound.py -test
REM 100 months, 10% per month...
REM py compound.py -pv 20000 -f "1.10" -n 10 2>&1 | tee p.out
REM py tcalc.py -c "10:32:13-9:07:13" 2>&1 | tee p.out
REM py tcalc.py -dbg 1 <tcalc.inp
REM py projectile.py -ts 0.01 -velocity 10.0 -angle 45.0 2>&1 | tee p.out
py projectile.py -ts 0.01 -velocity 10.0 -angle 90.0 2>&1 | tee p.out
