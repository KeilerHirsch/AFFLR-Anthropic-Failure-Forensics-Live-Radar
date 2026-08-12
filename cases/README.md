# Cases

Each case is a compact forensic record, not a duplicate of the upstream issue.

## Required sections

Every case should contain exactly these core sections:

1. **Summary**
2. **Impact**
3. **Evidence level**
4. **What is proven**
5. **What is not proven**
6. **References**

Optional short sections such as **Technical note** or **Timeline** are fine when they materially improve clarity.

## Naming

Use sequential identifiers:

```text
AFF-001-description
AFF-002-description
AFF-003-description
...
```

Do not renumber old cases when chronology changes. The identifier is archival, not semantic.

## New findings

For a new finding, copy the nearest existing case or open a repository issue using the finding template. Once the evidence is worth preserving, create the next `AFF-###` directory and add one row to the root README index.
