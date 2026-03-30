import re

def validate_order_data(data):
    """Проверка данных на соответствие стандартам предприятия"""
    # Проверка формата ID заказа (например, только цифры)
    if not str(data.get("order_id")).isdigit():
        return False, "Некорректный формат ID заказа"
    
    # Проверка наличия позиций товара
    if not data.get("items") or len(data["items"]) == 0:
        return False, "Список товаров пуст"
        
    print("[Validator] Данные успешно прошли проверку качества.")
    return True, "OK"
