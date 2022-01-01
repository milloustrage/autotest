from typing import List, Dict


def validator_test(project_name: str, urls: List[str]) -> Dict[str, bool]:
    # Открыть в selemium страницу валидатора
    # пройтись по urls и протестировать его через интерфейс валидатора
    # проверить есть ли ошибки
    # Если есть, то сохранить скриншот по названию url в папку проекта
    # Вернуть результатом словарь
    pass


    # return {
    #     'http://html:love@htmlonelove.top/voxhall-dev/contacts.html': True,
    #     'http://html:love@htmlonelove.top/voxhall-dev/gallery.html': False,
    # }











validator_test('voxhall', [
    'http://html:love@htmlonelove.top/voxhall-dev/contacts.html',
    'http://html:love@htmlonelove.top/voxhall-dev/gallery.html'
])
