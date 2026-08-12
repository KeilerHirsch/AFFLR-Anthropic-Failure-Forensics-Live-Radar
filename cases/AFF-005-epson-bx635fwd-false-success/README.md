# AFF-005 — Epson BX635FWD generated repair script / false-success behavior

## Summary

A PowerShell script titled `Fix-Epson-Drucker.ps1`, created on 2026-03-01 and attributed in its header to `KeilerHirsch / Claude Code`, was recovered in four historical locations with the same SHA-256:

```text
C5769D2A3482D9104790E012041493830D53CB9D1D8CB503AE2AAEC7DC5D1EC3
```

The script presents a `KOMPLETT-REPARATUR` workflow for an Epson Stylus Office BX635FWD, but contains confirmed false-success and compatibility defects. Separately, historical PowerShell history shows another cleanup block removing Epson startup values with `-ErrorAction SilentlyContinue` followed by an unconditional success message.

This case **does not** currently attribute the user's present printer/scanner outage to either script.

## Impact

Operational repair code that silently skips failed repair steps while reporting success can waste debugging time, hide configuration errors, and encourage repeated state mutation without establishing that the target fault was repaired.

## Evidence level

**L2 — artifact and relevant AI provenance established.**

The code defects themselves are directly inspectable, but execution of this exact repair script at the time of the current outage and a full causal chain to the current Epson failure have not been established.

## What is proven

- Four recovered copies of `Fix-Epson-Drucker.ps1` have the same SHA-256 listed above.
- The script header identifies the Epson BX635FWD target and attributes authorship to `KeilerHirsch / Claude Code`.
- `Repair-Printer` continues after `Show-PrinterStatus` reports that the configured printer is missing.
- The step labeled `Drucker-Fehlerzustand zuruecksetzen` only invokes `CancelAllJobs()` when its WMI lookup succeeds; it does not implement a general printer-error reset.
- The script uses `Get-WmiObject`, which is not available as a built-in cmdlet in modern PowerShell 7, while the user currently runs PowerShell 7.6.4.
- The WMI block catches failure and the workflow still prints `Reparatur abgeschlossen!`.
- The script removes print jobs and spool files but contains no `Remove-Printer`, `Remove-PrinterPort`, or printer-driver removal path.
- Historical PSReadLine history separately records an Epson cleanup block that attempts to remove `EPSDNMON` and an `EPLTarget\P0000000000000001` startup value with `-ErrorAction SilentlyContinue`, followed by an unconditional `[OK] Epson Hintergrund-Dienste entfernt` message.

## What is not proven

- Execution of this exact `Fix-Epson-Drucker.ps1` at the time of the current printer/scanner outage is not established.
- The script, as recovered, does not contain a mechanism that directly deletes the Windows printer queue object.
- The current missing Epson printer queue and unavailable scanner are therefore **not** attributed to this script by this case.
- The separate Epson startup-cleanup history block is not yet tied to the current outage or to a specific source file with a confirmed execution timestamp.
- The actual root cause of the present Epson failure remains open.

## Technical note

The interesting failure pattern is **false success**: error paths are swallowed or converted into `SKIP` output, yet the workflow emits a completion message that can be read as successful repair. This is independently useful as a generated-operational-code quality case even if the current hardware/software outage ultimately has another cause.

## References

- Recovered artifact SHA-256: `C5769D2A3482D9104790E012041493830D53CB9D1D8CB503AE2AAEC7DC5D1EC3`
- Device: Epson Stylus Office BX635FWD
- Current forensic work: printer driver and EpsonNet port remnants observed while the Windows printer queue is absent; scanner causality remains under investigation.
