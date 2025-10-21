# Trustpilot Review Model

## Projektbeschreibung
In diesem Projekt wurde ein lineares Regressionsmodell mit Bewertungen von **Trustpilot** trainiert, das auf verschiedenen Bewertungen unterschiedlichster Firmen basiert. Das erste Modell erreichte einen F1-Score von **63%**, was noch Spielraum für Verbesserungen lässt.

## Nächste Schritte
Im nächsten Schritt beabsichtige ich, die Trainingsdaten besser auszubalancieren, um einen höheren F1-Score von mindestens **85%** zu erreichen.

## Ausgabe von Version 1.0
- **Genauigkeit:** 0.629371

### Klassifikationsberichte
| Klasse | Präzision | Recall | F1-Score | Unterstützung |
|--------|-----------|--------|----------|---------------|
| 1      | 0.76      | 0.77   | 0.77     | 115           |
| 2      | 0.66      | 0.59   | 0.62     | 114           |
| 3      | 0.56      | 0.62   | 0.59     | 114           |
| 4      | 0.55      | 0.54   | 0.55     | 115           |
| 5      | 0.62      | 0.62   | 0.62     | 114           |
| **Gesamtgenauigkeit** |           |        | 0.63     | 572           |
| **Durchschnitt (Macro)** | 0.63      | 0.63   | 0.63     | 572           |
| **Durchschnitt (Gewichtet)** | 0.63      | 0.63   | 0.63     | 572           |
