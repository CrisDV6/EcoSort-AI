"""Demostración manual del sistema experto de EcoSort."""

from backend.expert_system import ExpertSystem


def main() -> None:
    system = ExpertSystem()

    print("=== EcoSort AI: sistema experto ===")
    material = input("Material predicho por la IA (plastico/vidrio): ")
    confidence = float(input("Confianza entre 0 y 1 (ejemplo 0.92): "))
    detected = input("¿Se detectó un objeto? (s/n): ").strip().lower() == "s"

    result = system.evaluate(material, confidence, detected)

    print("\n--- Resultado ---")
    print(f"Decisión: {result.decision.value}")
    print(f"Regla activada: {result.activated_rule}")
    print(f"Mensaje: {result.message}")
    print(f"¿Mover compuerta?: {'Sí' if result.should_move_gate else 'No'}")


if __name__ == "__main__":
    main()

