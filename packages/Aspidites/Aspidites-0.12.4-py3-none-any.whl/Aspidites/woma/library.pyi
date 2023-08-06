from Aspidites.woma import *
from Aspidites._vendor import F as F
from Aspidites._vendor.contracts import new_contract as new_contract
from Aspidites.monads import Surely as Surely, Undefined as Undefined
from collections.abc import Generator
from pyrsistent import PClass as PClass, PRecord as PRecord, m as m, pmap as pmap, pset as pset, pvector as pvector, s as s, v as v
from typing import Any

procedure: None
coroutine: Generator
number: Any

def Add(x: number = ..., y: number = ...) -> number: ...
def Sub(x: number = ..., y: number = ...) -> number: ...
def Div(x: number = ..., y: number = ...) -> number: ...
def Exp(x: number = ..., y: number = ...) -> number: ...
def Mod(x: number = ..., y: number = ...) -> number: ...
