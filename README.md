# genpark-ldpc-tanner-graph-belief-propagation-skill

Agent Skill implementing **Low-Density Parity-Check (LDPC) Tanner Graph Belief Propagation**, using iterative sum-product Log-Likelihood Ratio (LLR) message passing between variable and check nodes.

## Architectural Overview
```mermaid
flowchart TD
    LLR["Initial Channel LLRs"] --> VtoC["Variable-to-Check Messages"]
    VtoC --> Check["Check Node Updates: Tanh Product Rule"]
    Check --> CtoV["Check-to-Variable Messages"]
    CtoV --> Total["Accumulate Total Marginal LLRs"]
    Total --> Hard["Hard Decision: Bit = (LLR < 0 ? 1 : 0)"]
    Hard --> SynCheck{"H * x == 0 ?"}
    SynCheck -- Yes --> Converged["Valid Codeword Recovered"]
    SynCheck -- No --> Loop["Next Iteration"]
```
