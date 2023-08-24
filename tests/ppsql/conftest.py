from __future__ import annotations

import pytest

from collections import namedtuple
from enum import Enum
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


class Base(DeclarativeBase):

    def __repr__(self) -> str:
        return f"{self.name} ({self.__class__.__name__}, age={self.age})"


class ParentRole(Enum):
    FATHER: str = "father"
    MOTHER: str = "mother"
    STEP_FATHER: str = "step-father"
    STEP_MOTHER: str = "step-mother"


association_table = Table(
    "association_table",
    Base.metadata,
    Column("parent_id", ForeignKey("parents.parent_id"), primary_key=True),
    Column("child_id", ForeignKey("children.child_id"), primary_key=True),
)


class Parent(Base):
    __tablename__ = "parents"

    parent_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    role: Mapped[ParentRole]

    children: Mapped[list[Child]] = relationship(secondary=association_table, back_populates="parents")


class Child(Base):
    __tablename__ = "children"

    child_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    parents: Mapped[list[Parent]] = relationship(secondary=association_table, back_populates="children")


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[list[Address]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.user_id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "addresses"

    address_id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.address_id!r}, email_address={self.email_address!r})"


@pytest.fixture(scope="module")
def engine():
    engine = create_engine("sqlite://", echo=False)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="module")
def session(engine):
    session = Session(engine)
    yield session
    session.rollback()
    session.close()


@pytest.fixture(scope="function")
def family():
    dad = Parent(name="Sully", age=46, role=ParentRole.STEP_FATHER)
    mom = Parent(name="Kiki", age=42, role=ParentRole.MOTHER)
    children = [
        Child(name="Kourtni", age=25),
        Child(name="Jacob", age=18),
        Child(name="Lauren", age=16),
    ]
    yield namedtuple("Family", ['dad', 'mom', 'children'])(
        dad=dad, mom=mom, children=children
    )
