# webserv

Установка и запуск: 




Curl-команды: 

Чтобы добавить новый товар, необходимо в файле application.py найти метод add_product и в словаре изменить значения для ключей "_id", "name", "description"
Затем в IDE или cmd вызвать:
curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/add
если консоль выведет сообщение "Product successfully added" - товар успешно добавлен

Поиск товара по ID: 
curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/int:id, где int:id - натуральное число (например 3, 5, 7)

curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/sort - выведет информацию обо всех имеющихся в базе данных товарах.

curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/sort/name - вернет перечень товаров отсортированных по названиям в алфавитном порядке.

curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/sort/param - вернет перечень всех товаров по ключевому слову. 
