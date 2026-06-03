import tkinter as tk
import heapq

# ==========================
# DATA PETA KOTA
# ==========================
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'D': 5, 'E': 12},
    'C': {'D': 2, 'F': 7},
    'D': {'E': 3, 'F': 2},
    'E': {'G': 2},
    'F': {'G': 5},
    'G': {}
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 5,
    'E': 2,
    'F': 4,
    'G': 0
}

# Posisi node pada canvas
positions = {
    'A': (100, 200),
    'B': (250, 100),
    'C': (250, 300),
    'D': (400, 200),
    'E': (550, 100),
    'F': (550, 300),
    'G': (700, 200)
}

# ==========================
# ALGORITMA A*
# ==========================
def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, g_cost[goal]

        for neighbor, cost in graph[current].items():

            tentative = g_cost[current] + cost

            if tentative < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = tentative

                f = tentative + heuristic[neighbor]
                heapq.heappush(open_list, (f, neighbor))

    return None, None

# ==========================
# GAMBAR PETA
# ==========================
def draw_map(highlight_path=None):

    canvas.delete("all")

    # gambar jalan
    for city in graph:
        x1, y1 = positions[city]

        for neighbor, distance in graph[city].items():

            x2, y2 = positions[neighbor]

            color = "gray"
            width = 2

            if highlight_path:
                for i in range(len(highlight_path)-1):
                    if city == highlight_path[i] and neighbor == highlight_path[i+1]:
                        color = "red"
                        width = 5

            canvas.create_line(
                x1, y1, x2, y2,
                fill=color,
                width=width
            )

            mx = (x1+x2)/2
            my = (y1+y2)/2

            canvas.create_text(
                mx, my-10,
                text=str(distance),
                fill="blue"
            )

    # gambar kota
    for city, (x, y) in positions.items():

        canvas.create_oval(
            x-25, y-25,
            x+25, y+25,
            fill="lightblue"
        )

        canvas.create_text(
            x, y,
            text=city,
            font=("Arial", 12, "bold")
        )

# ==========================
# CARI RUTE
# ==========================
def find_route():

    path, cost = astar("A", "G")

    draw_map(path)

    result_label.config(
        text=f"Rute Terbaik : {' → '.join(path)}\nTotal Biaya : {cost}"
    )

# ==========================
# UI
# ==========================
root = tk.Tk()
root.title("Navigasi Peta Kota dengan A*")
root.geometry("850x600")

title = tk.Label(
    root,
    text="Visualisasi Navigasi Peta Kota (A*)",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)

canvas = tk.Canvas(
    root,
    width=800,
    height=400,
    bg="white"
)

canvas.pack()

draw_map()

btn = tk.Button(
    root,
    text="Cari Jalur Terbaik",
    command=find_route,
    font=("Arial", 12)
)

btn.pack(pady=10)

result_label = tk.Label(
    root,
    text="Klik tombol untuk mencari rute",
    font=("Arial", 12)
)

result_label.pack()

root.mainloop()