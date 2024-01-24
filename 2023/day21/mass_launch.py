import subprocess

# clean file
open("mass_output.txt", "w")

for nb_steps in range(500):
# for nb_steps in range(259, 264):
# for nb_steps in range(65, 365, 131):
	subprocess.run(["python", "part2_only_center.py", str(nb_steps)])
	subprocess.run(["python", "part2.py", str(nb_steps)])
