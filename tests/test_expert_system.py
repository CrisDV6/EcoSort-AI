"""Pruebas del motor de reglas sin dependencias externas."""

import unittest

from backend.expert_system import Decision, ExpertSystem


class ExpertSystemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.system = ExpertSystem()

    def test_high_confidence_plastic_is_classified(self) -> None:
        result = self.system.evaluate("plástico", 0.95)
        self.assertEqual(result.decision, Decision.CLASSIFY_PLASTIC)
        self.assertTrue(result.should_move_gate)

    def test_high_confidence_glass_is_classified(self) -> None:
        result = self.system.evaluate("glass", 0.90)
        self.assertEqual(result.decision, Decision.CLASSIFY_GLASS)
        self.assertTrue(result.should_move_gate)

    def test_medium_confidence_requests_new_capture(self) -> None:
        result = self.system.evaluate("vidrio", 0.72)
        self.assertEqual(result.decision, Decision.RECAPTURE)
        self.assertFalse(result.should_move_gate)

    def test_low_confidence_rejects_decision(self) -> None:
        result = self.system.evaluate("plastico", 0.40)
        self.assertEqual(result.decision, Decision.REJECT)

    def test_missing_object_never_moves_gate(self) -> None:
        result = self.system.evaluate("plastico", 0.99, object_detected=False)
        self.assertEqual(result.activated_rule, "R1_NO_OBJECT")
        self.assertFalse(result.should_move_gate)

    def test_unsupported_material_is_rejected(self) -> None:
        result = self.system.evaluate("metal", 0.99)
        self.assertEqual(result.activated_rule, "R2_UNSUPPORTED_MATERIAL")

    def test_invalid_confidence_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            self.system.evaluate("vidrio", 1.25)


if __name__ == "__main__":
    unittest.main()

