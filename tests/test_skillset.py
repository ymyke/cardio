import pytest
from dataclasses import dataclass
from cardio.skills import Skill, SkillSet, Spines, InstantDeath, Fertility


def test_init_empty_list():
    sl = SkillSet()
    assert sl.skills == []


def test_init_list_of_types():
    sl = SkillSet([Spines, InstantDeath])
    assert sl.skills == [Spines(), InstantDeath()]


def test_init_list_of_instances():
    sl = SkillSet([Spines(), InstantDeath()])
    assert sl.skills == [Spines(), InstantDeath()]


def test_has():
    sl = SkillSet([Spines, InstantDeath])
    assert sl.has(Spines()) == True
    assert sl.has(InstantDeath) == True
    assert sl.has(Fertility()) == False


def test_get():
    sl = SkillSet([Spines, InstantDeath])
    assert sl.get(Spines) == Spines()
    assert sl.get(InstantDeath) == InstantDeath()
    with pytest.raises(AttributeError):
        sl.get(Fertility)


def test_get_types():
    sl = SkillSet([Spines, InstantDeath])
    assert sl.get_types() == [Spines, InstantDeath]


def test_count():
    sl = SkillSet([Spines, InstantDeath])
    assert sl.count() == 2


def test_add():
    sl = SkillSet([Spines])
    sl.add(InstantDeath)
    assert sl.skills == [Spines(), InstantDeath()]


def test_remove():
    sl = SkillSet([Spines, InstantDeath])
    sl.remove(Spines)
    assert sl.skills == [InstantDeath()]


def test_remove_instance():
    sl = SkillSet([Spines, InstantDeath])
    sl.remove(Spines())
    assert sl.skills == [InstantDeath()]


def test_remove_all():
    sl = SkillSet([Spines, InstantDeath])
    sl.remove_all()
    assert sl.skills == []


def test_with_added_attribute():
    @dataclass
    class SomeNewSkill(Skill):
        name: str = ""
        symbol: str = ""
        description: str = ""
        potency: int = 0

        def __post_init__(self):
            self.newattr: str = "newattr"

    sl = SkillSet([SomeNewSkill])
    assert sl.get(SomeNewSkill) == SomeNewSkill()
    sl.get(SomeNewSkill).newattr = "changedattr"
    assert sl.has(SomeNewSkill)
