"""Sistema experto basado en reglas para validar clasificaciones."""

from .engine import ExpertSystem
from .models import Decision, ExpertResult

__all__ = ["Decision", "ExpertResult", "ExpertSystem"]

