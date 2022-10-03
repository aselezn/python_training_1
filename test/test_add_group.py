# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.add_group import testdata
#from data.add_group import constant as testdata - подменить переменную на другую можно, если переименовать ее


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])  #название параметра/источник тестовых данных/ преобразовали в список тестовые данные
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count() #используем count (выступает в роли хэша), выполянется быстрее чем основная функция
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

