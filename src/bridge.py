import json
import time

class IntegrationBridge:
    """Модуль интеграции CRM и ERP систем"""
    
    def __init__(self):
        print("[System] Модуль интеграции ПМ.02 запущен...")

    def fetch_from_crm(self):
        """Эмуляция получения данных о новом заказе из CRM"""
        sample_order = {
            "order_id": 1025,
            "client": "ООО ТехноПром",
            "items": [{"id": 55, "name": "Процессор", "qty": 10}],
            "status": "New"
        }
        print(f"[CRM] Получен новый заказ №{sample_order['order_id']}")
        return sample_order

    def transform_for_erp(self, data):
        """Преобразование данных под формат складской системы ERP"""
        print("[Transform] Конвертация данных в формат ERP (JSON)...")
        data["status"] = "Processing_in_ERP"
        data["timestamp"] = time.ctime()
        return data

    def send_to_erp(self, data):
        """Эмуляция отправки данных в ERP через REST API"""
        print(f"[ERP] Данные заказа {data['order_id']} успешно интегрированы.")
        return True

# Запуск процесса интеграции
if __name__ == "__main__":
    bridge = IntegrationBridge()
    order = bridge.fetch_from_crm()
    processed_order = bridge.transform_for_erp(order)
    
    if bridge.send_to_erp(processed_order):
        print("\n[Итог] Интеграция программных модулей завершена успешно.")
