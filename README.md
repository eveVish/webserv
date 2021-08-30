# webserv

Установка и запуск: 
1. Запустить сервер MongoDB на локальном хосте 27017.
2. Загрузить архив и распокавать его в папку.
3. Открыть cmd в директории папки, прописать python application.py (может потребоваться дополнительная установка недостающих пакетов через pip install).

ИЛИ

1. Открыть application.py в IDE. 
2. В терминале среды разработки указать следующие команды: set FLASK_APP=application.py, set FLASK_DEBUG=true, flask run (запустится локальный хост).
3. В новом локальном терминале или cmd можно будет начать работу.
Внесение данных:

Внести параметры товара можно через файл parameters.py, там же монжо указать все необходимые поля. Затем, будет необходимо в файле applications.py в методе add_product внести в словарь все необходимые ключи, а значениями указать переменные из файла parameters.py (предварителньо импортировав их).

Пример: 
  `#parameters.py
  
  prod_color = 'blue'
  prod_size = 'small'
  cover = 'soft'
  
  #application.py
  
  from parameters import color, size, cover
  
  def add_product():
    """Дабавляет товар в базу данных."""
       
       db.products.insert_one({'_id': pr_id,
                              'name': product_name,
                              'description': product_description,
                              'color': prod_color,
                              'size': prod_size
                              'covering' : 'cover'})`



Curl-команды: 

Для добавления товара: 
Необходимо в терминале IDE или cmd вызвать:
curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/add
если консоль выведет сообщение "Product successfully added" - товар успешно добавлен.

Поиск товара по ID:
curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/int:id, где int:id - натуральное число (например 3, 5, 7)

curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/sort - выведет информацию обо всех имеющихся в базе данных товарах.

curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/sort/name - вернет все совпадения по наименованиям товаров, отсортированных в алфавитном порядке.

Поиск по параметрам:

В фпйле application.py находится метод sort_by_param, где реализуется .find({param : parameter_name})
Необходимо в этом словаре через запятую указать все ключи и их значения для поиска. Например: db.products.find({'color': "green", 'name' : 'Guitar'})
После этого в cmd или терминале прописать: 
curl -i -H 'Content-Type: Application/json' -X POST http://127.0.0.1:5000/sort/param 
