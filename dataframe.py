"""
import pandas as pd

# Membuat dataframe dengan identitas kelompok
data = {
    'no': [1, 2, 3,4],
    'role': ['ketua', 'anggota', 'anggota','anggota'],
    'nama': ['abyan', 'ridho', 'Adit','Jaka'],
    'nim': ['123456', '234567', '345678','9101112'],
    'alamat': ['Jl. A No.1', 'Jl. B No.2', 'Jl. C No.3','Jl.pasawahan'],
    'no.hp': ['08123456789', '08123456790', '08123456791','081310116489']
}

df = pd.DataFrame(data)


# Melakukan slicing untuk menghapus kolom alamat dan no.hp
df_sliced = df.drop(columns=['alamat', 'no.hp'])

print(df_sliced)
"""
from collections import deque

def bfs_solve(start_state, goal_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path  # Solusi ditemukan, kembalikan urutan langkah

        if current_state not in visited:
            visited.add(current_state)
            for action in possible_actions(current_state):
                new_state = perform_action(current_state, action)
                queue.append((new_state, path + [action]))

    return None  # Tidak ada solusi
