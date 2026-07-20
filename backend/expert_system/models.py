"""Modelos de datos del sistema experto."""

from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    """Acciones que puede recomendar el motor de inferencia."""

    CLASSIFY_PLASTIC = "clasificar_plastico"
    CLASSIFY_GLASS = "clasificar_vidrio"
    RECAPTURE = "repetir_captura"
    REJECT = "rechazar_objeto"


@dataclass(frozen=True)
class ExpertResult:
    """Conclusión explicable producida por el sistema experto."""

    decision: Decision
    material: str | None
    confidence: float
    message: str
    activated_rule: str
    should_move_gate: bool

