from validator import validate_order_data
from erp_module import ERP_System

def run_integration():
    # 1. Данные, пришедшие из CRM (имитация)
    crm_payload = {
        "order_id": "7721",
        "client": "ООО ОптТорг",
        "items": [{"name": "Процессор", "qty": 5}]
    }
    
    print(f"--- Запуск интеграции заказа №{crm_payload['order_id']} ---")

    # 2. Этап валидации (ПМ.02 Требование к качеству)
    is_valid, message = validate_order_data(crm_payload)
    
    if is_valid:
        # 3. Передача данных в ERP (Интеграция)
        erp = ERP_System()
        erp.process_new_order(crm_payload)
        print("--- Интеграция успешно завершена ---")
    else:
        print(f"--- Ошибка интеграции: {message} ---")

if __name__ == "__main__":
    run_integration()
