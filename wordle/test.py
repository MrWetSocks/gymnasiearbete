from slow_wordle import solve as slow_solve
from fast_wordle import solve as fast_solve
from faster_wordle import solve as faster_solve
from fastest_wordle import solve as fastest_solve

fastest_solve_time, fastest_combinations_found = fastest_solve()

print(f"""
    Faster solver:
       Time: {fastest_solve_time}
       Combinations found: {fastest_combinations_found} 
""")

faster_solve_time, faster_combinations_found = faster_solve()

print(f"""
    Faster solver:
       Time: {faster_solve_time}
       Combinations found: {faster_combinations_found} 
""")

fast_solve_time, fast_combinations_found = fast_solve()

print(f"""
    Fast solver:
       Time: {fast_solve_time}
       Combinations found: {fast_combinations_found} 
""")

slow_solve_time, slow_combinations_found = slow_solve()

print(f"""
    Slow solver:
       Time: {slow_solve_time if slow_solve_time < 1800 else "Longer than 30 minutes"}
       Combinations found: {slow_combinations_found} 
""")

