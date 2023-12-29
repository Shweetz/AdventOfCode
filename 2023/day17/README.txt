Benchmarks

input_25.txt:
- part1_v1 = 37  sec
- part1_v2 = 2.0 sec
- part1_v3 = 0.8 sec
- part1_v4 = 0.9 sec
- part1_v5 = 0.1 sec
- part1_v5 = 0.1 sec (v5.1)

input_50.txt:
- part1_v1 = 783 sec
- part1_v2 = 21 sec
- part1_v3 = 11 sec
- part1_v4 = 7.0 sec
- part1_v5 = 0.3 sec
- part1_v5 = 0.3 sec (v5.1)

input.txt:
- part1_v3 > 3h
- part1_v4 = 573 sec
- part1_v5 = 5.8 sec
- part1_v5 = 3.1 sec (v5.1)
- part1    = 0.9 sec

Results

dfs => bfs         : 20x faster
1 tile => fullmove : 2x faster
no queue => queue  : 10x faster
queue => prioqueue : 100x faster (wtf ???)
i prio => heat prio: 2x faster
remove useless shit: 3x faster
