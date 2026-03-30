class ERP_System:
    def __init__(self):
        self.warehouse_db = {"Процессор": 150, "Материнская плата": 80}

    def process_new_order(self, order_data):
        """Прием данных из интеграционного шлюза"""
        for item in order_data['items']:
            name = item['name']
            qty = item['qty']
            if name in self.warehouse_db and self.warehouse_db[name] >= qty:
                self.warehouse_db[name] -= qty
                print(f"[ERP] Товар {name} зарезервирован на складе. Остаток: {self.warehouse_db[name]}")
            else:
                print(f"[ERP] Ошибка: Недостаточно товара {name}")
