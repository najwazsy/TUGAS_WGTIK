def kena_razia(date, data):
    routes = ['Gajah Mada', 'Hayam Wuruk', 'Sisingamangaraja', 'Panglima Polim', 'Fatmawati', 'Tomang Raya']
    
    if date < 1 or date > 31:
        return 'Invalid date'
    
    violations = []
    
    for vehicle in data:
        if vehicle['type'] == 'Mobil':
            plate_number = int(vehicle['plat'].split(' ')[1][-1]) # Ambil angka belakang dari nomor plat
            is_even = plate_number % 2 == 0
            is_route_violation = any(route in routes for route in vehicle['rute'])
            
            if (is_route_violation and not is_even) or (not is_route_violation and is_even):
                violations.append({'name': vehicle['name'], 'tilang': len(vehicle['rute']) - 1})
    
    return violations

# Contoh penggunaan fungsi
data = [
    {'name': 'Denver', 'plat': 'B 2791 KDS', 'type': 'Mobil', 'rute': ['TB Simatupang', 'Panglima Polim', 'Depok', 'Senen Raya']},
    {'name': 'Toni', 'plat': 'B 1212 JBB', 'type': 'Mobil', 'rute': ['Pintu Besar Selatan', 'Panglima Polim', 'Depok', 'Senen Raya', 'Kemang']},
    {'name': 'Stark', 'plat': 'B 444 XSX', 'type': 'Motor', 'rute': ['Pondok Indah', 'Depok', 'Senen Raya', 'Kemang']},
    {'name': 'Anna', 'plat': 'B 678 DD', 'type': 'Mobil', 'rute': ['Fatmawati', 'Panglima Polim', 'Depok', 'Senen Raya', 'Kemang', 'Gajah Mada']}
]

violations = kena_razia(27, data)
print(violations)