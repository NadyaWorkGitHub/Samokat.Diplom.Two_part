# Надежда Елецких, 16-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
def test_create_order():
    # Создание заказа
    response_create = sender_stand_request.create_order()
    print("Create Order Status Code:", response_create.status_code)
    print("Create Order Response Body:", response_create.json())
    assert response_create.status_code == 201, "Не удалось создать заказ"
    # Получение трек-номера заказа
    track_number = response_create.json().get("track")
    assert track_number is not None, "Трек-номер отсутствует"
    # Сохранение трек-номера
    print("Трек-номер заказа:", track_number)
    # Получение заказа по трек-номеру
    response_get = sender_stand_request.get_order_by_track(track_number)
    print("Get Order Status Code:", response_get.status_code)
    print("Get Order Response Body:", response_get.json())
    assert response_get.status_code == 200, "Не удалось получить заказ по трек-номеру"
# Запуск теста
test_create_order()
