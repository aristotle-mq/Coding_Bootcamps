import redis

with redis.Redis() as redis_client:
    value = redis_client.brpop('queue')
    '''
    brpop - в случае передачи пустой очереди, будет ждать 
        int(value) - обращение к значению
        
    rpop - в случае передачи пустой очереди, произойдет ошибка
        int(value[1]) - обращение к значению, потому что передается кортеж,
                        где первый элемент - это ключ
    '''

print(int(value[1]))