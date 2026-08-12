# AFF-002 — Hook launch failure collides with deny exit code 2

## Summary

A `PreToolUse` hook command that fails to launch can surface the same exit code Claude Code reserves for an intentional deny. The reported result is that a broken hook path can be interpreted as policy enforcement and block matched tools.

## Impact

A configuration mistake can produce an unrecoverable in-session tool lockout, especially when the affected hook also protects the configuration needed to restore itself.

## Evidence level

**L4 — failure reproduced.**

The upstream report contains a minimal reproduction and a control differing only in whether the hook target exists.

## What is proven

- Public upstream issue `anthropics/claude-code#80697` was filed by `KeilerHirsch`.
- The reproduction uses Claude Code 2.1.218 on Windows 11 with user settings excluded and no MCP servers.
- A missing Python hook script produces exit code 2 and the matched Bash tool is blocked.
- The control uses an existing command that exits 0 and the Bash tool executes normally.
- The report therefore isolates launch failure as the differing condition in the reproduction.

## What is not proven

- The case does not claim every possible hook launcher or interpreter produces the same collision.
- It does not establish what Anthropic's intended fail-open/fail-closed policy should be; it documents the ambiguity and operational consequence.
- Current versions may behave differently and should be retested before claiming persistence.

## References

- Upstream: https://github.com/anthropics/claude-code/issues/80697
