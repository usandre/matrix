### matrix example



#### Methods

 Method | Resource | Description| Params
 --- | --- | --- | ---
GET | /sub/ | List of buckets | 
POST, PUT | /sub/{name} | Saves event into {name} bucket | ?code=400&prob=70
GET | /sub/{name} | Lists events from {name} bucket|
GET | /sub/{name}/{event} | Returns record with id {event} from  from {name} bucket|
DEL | /sub/{name} | Deletes {name} bucket  |


## getting started
1. build images
2. run docker compose
3. open browser localhost:5000


## fdf
Было несколько часов свободного времени, я набросал работающий прототип, как может работать загрузка матрицы.
Все что нужно, это браузер. все ссылки открывайте в браузере

1. Загружаете матрицу в виде: <инструмент>/<число1>/<число2>/<дата>
например: просто открываете в любом браузере:
http://ec2-34-220-179-196.us-west-2.compute.amazonaws.com:5000/load/EUR/1.222/1.333/20181019
2. Матрица расчитывется по 2 числам (сейчас просто генерируются случайные числа) и матрица доступна по ссылке 
http://ec2-34-220-179-196.us-west-2.compute.amazonaws.com:5000/matrix/EUR/20181019
3. все советники обновляются сами, по расписанию или по сигналу по постоянной ссылке 
4. Все!

