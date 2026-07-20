"""Motor de inferencia mediante reglas SI-ENTONCES.

La IA visual entregará un material y un nivel de confianza. Este módulo
transforma esos datos en una decisión segura y explicable para EcoSort.
"""

from .models import Decision, ExpertResult


class ExpertSystem:
    """Evalúa hechos utilizando reglas ordenadas por prioridad."""

    SUPPORTED_MATERIALS = {"plastico", "vidrio"}

    def __init__(
        self,
        automatic_threshold: float = 0.85,
        recapture_threshold: float = 0.60,
    ) -> None:
        if not 0 <= recapture_threshold < automatic_threshold <= 1:
            raise ValueError(
                "Los umbrales deben cumplir: 0 <= repetición < automático <= 1."
            )

        self.automatic_threshold = automatic_threshold
        self.recapture_threshold = recapture_threshold

    def evaluate(
        self,
        material: str | None,
        confidence: float,
        object_detected: bool = True,
    ) -> ExpertResult:
        """Aplica encadenamiento hacia adelante sobre los hechos recibidos."""

        self._validate_confidence(confidence)
        normalized_material = self._normalize_material(material)

        # R1: nunca accionar el mecanismo si no hay un objeto presente.
        if not object_detected:
            return ExpertResult(
                decision=Decision.REJECT,
                material=None,
                confidence=confidence,
                message="No se detectó un objeto; la compuerta permanece inmóvil.",
                activated_rule="R1_NO_OBJECT",
                should_move_gate=False,
            )

        # R2: una clase desconocida no pertenece al alcance plástico/vidrio.
        if normalized_material not in self.SUPPORTED_MATERIALS:
            return ExpertResult(
                decision=Decision.REJECT,
                material=normalized_material,
                confidence=confidence,
                message="El material no pertenece a las clases admitidas.",
                activated_rule="R2_UNSUPPORTED_MATERIAL",
                should_move_gate=False,
            )

        # R3: con confianza baja no se toma una decisión física.
        if confidence < self.recapture_threshold:
            return ExpertResult(
                decision=Decision.REJECT,
                material=normalized_material,
                confidence=confidence,
                message="La confianza es demasiado baja; revise el objeto manualmente.",
                activated_rule="R3_LOW_CONFIDENCE",
                should_move_gate=False,
            )

        # R4: en la zona intermedia se solicita una nueva fotografía.
        if confidence < self.automatic_threshold:
            return ExpertResult(
                decision=Decision.RECAPTURE,
                material=normalized_material,
                confidence=confidence,
                message="Clasificación dudosa; capture otra imagen con mejor iluminación.",
                activated_rule="R4_MEDIUM_CONFIDENCE",
                should_move_gate=False,
            )

        # R5 y R6: clasificación automática de alta confianza.
        if normalized_material == "plastico":
            return ExpertResult(
                decision=Decision.CLASSIFY_PLASTIC,
                material=normalized_material,
                confidence=confidence,
                message="Plástico confirmado; dirigir al contenedor de plástico.",
                activated_rule="R5_HIGH_CONFIDENCE_PLASTIC",
                should_move_gate=True,
            )

        return ExpertResult(
            decision=Decision.CLASSIFY_GLASS,
            material=normalized_material,
            confidence=confidence,
            message="Vidrio confirmado; dirigir al contenedor de vidrio.",
            activated_rule="R6_HIGH_CONFIDENCE_GLASS",
            should_move_gate=True,
        )

    @staticmethod
    def _validate_confidence(confidence: float) -> None:
        if not 0 <= confidence <= 1:
            raise ValueError("La confianza debe estar entre 0 y 1.")

    @staticmethod
    def _normalize_material(material: str | None) -> str | None:
        if material is None:
            return None

        normalized = material.strip().lower()
        translations = {
            "plastic": "plastico",
            "plástico": "plastico",
            "glass": "vidrio",
        }
        return translations.get(normalized, normalized)

