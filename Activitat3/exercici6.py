# Llista inicial
areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55,
             "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

# 1. Imprimir el segon element
print(f"El segon element és: {areas_pis[1]}")

# 2. Imprimir l’últim element
print(f"L'últim element és: {areas_pis[-1]}")

# 3. Imprimir l’àrea de la terrassa
terrassa_index = areas_pis.index("Terrassa")  # Trobar la posició de "Terrassa"
area_terrassa = areas_pis[terrassa_index + 1]  # L'àrea està en la posició següent
print(f"L'àrea de la terrassa és: {area_terrassa} m²")

# 4. Imprimir del primer element al tercer element
print(f"Del primer al tercer element: {areas_pis[:3]}")

# 5. Imprimir del tercer element a l’últim
print(f"Del tercer element a l'últim: {areas_pis[2:]}")

# 6. Imprimir el total de l'àrea de les dues habitacions
habitacio1_index = areas_pis.index("Habitació1")  # Trobar la posició de "Habitació1"
habitacio2_index = areas_pis.index("Habitació2")  # Trobar la posició de "Habitació2"
total_habitacions = areas_pis[habitacio1_index + 1] + areas_pis[habitacio2_index + 1]
print(f"El total de l'àrea de les dues habitacions és: {total_habitacions} m²")

# 7. Modificar l’àrea del lavabo i imprimir la nova llista area
lavabo_index = areas_pis.index("Lavabo")  # Trobar la posició de "Lavabo"
areas_pis[lavabo_index + 1] = 8.5  # Modificar l'àrea del lavabo
print(f"Nova llista després de modificar l'àrea del lavabo: {areas_pis}")

# 8. Afegir l'àrea de "pati interior" i 2.78 a les últimes posicions. Imprimir la nova llista area.
areas_pis.append("Pati Interior")  # Afegir "Pati Interior"
areas_pis.append(2.78)  # Afegir l'àrea del pati interior
print(f"Nova llista després d'afegir el pati interior: {areas_pis}")

# 9. Imprimir el total de l’àrea del pis
# Recorrer la llista i sumar només els elements que són números (àrees)
total_area = sum([area for area in areas_pis if isinstance(area, (int, float))])
print(f"El total de l'àrea del pis és: {total_area} m²")
