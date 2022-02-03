from typing import List
from sandbox.location.location import Location
from sandbox.location.path import Path


class Map(object):
    locations: List[Location]
    paths: List[Path]
