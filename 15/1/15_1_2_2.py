# TODO 10 раз подбрасываем монету в одну строку

[print(('Решка', 'Орел')[__import__('random').randint(0, 1)]) for _ in range(10)]