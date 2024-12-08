import pytest
from src.task_manager import TaskManager

@pytest.fixture
def manager():
    return TaskManager()

def test_add_task(manager):
    manager.add_task("Fazer compras")
    assert len(manager.list_tasks()) == 1
    assert manager.list_tasks()[0].title == "Fazer compras"
    assert manager.list_tasks()[0].completed is False

def test_add_duplicate_task(manager):
    manager.add_task("Ler um livro")
    with pytest.raises(ValueError):
        manager.add_task("Ler um livro")

def test_complete_task(manager):
    manager.add_task("Estudar Python")
    manager.complete_task("Estudar Python")
    assert manager.list_tasks()[0].completed is True

def test_complete_non_existent_task(manager):
    with pytest.raises(ValueError):
        manager.complete_task("Tarefa Inexistente")

def test_remove_task(manager):
    manager.add_task("Praticar exercícios")
    manager.remove_task("Praticar exercícios")
    assert len(manager.list_tasks()) == 0

def test_remove_non_existent_task(manager):
    with pytest.raises(ValueError):
        manager.remove_task("Tarefa Não Cadastrada")
