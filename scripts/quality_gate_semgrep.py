#!/usr/bin/env python3
"""Quality Gate: falla ante hallazgos ERROR en salida JSON de Semgrep.

Exit codes: 0 = no ERROR; 1 = hallazgos ERROR; 2 = reporte ausente/invalido.
Las alertas WARNING/INFO se conservan en el reporte, pero no bloquean.
"""
import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python scripts/quality_gate_semgrep.py <reporte.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"QUALITY GATE ERROR: no existe el reporte: {path}", file=sys.stderr)
        return 2
    try:
        result = json.loads(path.read_text(encoding="utf-8"))
        findings = result["results"]
        if not isinstance(findings, list):
            raise ValueError("'results' debe ser una lista")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"QUALITY GATE ERROR: JSON invalido: {exc}", file=sys.stderr)
        return 2

    fatal = [x for x in findings if str(x.get("extra", {}).get("severity", "")).upper() == "ERROR"]
    warning = [x for x in findings if str(x.get("extra", {}).get("severity", "")).upper() == "WARNING"]
    info = [x for x in findings if str(x.get("extra", {}).get("severity", "")).upper() == "INFO"]
    print(f"Semgrep: total={len(findings)}, ERROR={len(fatal)}, WARNING={len(warning)}, INFO={len(info)}")
    for x in fatal[:25]:
        loc = x.get("start", {}).get("line", "?")
        print(f"  BLOQUEANTE: {x.get('check_id', '<regla>')} - {x.get('path', '<archivo>')}:{loc}")
    if fatal:
        print("QUALITY GATE: FAILED (existen hallazgos Semgrep ERROR).", file=sys.stderr)
        return 1
    print("QUALITY GATE SAST: SUCCESS (sin hallazgos Semgrep ERROR).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
