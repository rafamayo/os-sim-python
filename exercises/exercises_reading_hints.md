# Reading-Hints (Online) — Betriebssysteme (Übungen, Woche 1–15)

Diese Datei enthält kurze, pragmatische Empfehlungen zu Online-Quellen für jede Übungswoche.

---

## Woche 1 — Scheduler: Grundlagen / FIFO
- **OSTEP — Scheduling (Einführung)** — klare Einführung in CPU-Scheduling, Ready‑Queue, Metriken (waiting/turnaround).  
  https://pages.cs.wisc.edu/~remzi/OSTEP/

## Woche 2 — Round‑Robin & Preemption
- **OSTEP — Scheduling (Round‑Robin & Preemption)** — beschreibt Time‑Slices, Preemption und praktische Effekte.  
  https://pages.cs.wisc.edu/~remzi/OSTEP/

## Woche 3 — Prioritäts‑Scheduling, SJF / SRT
- **OSTEP — Scheduling (Prioritäten / Fairness / MLFQ)** — Diskutiert Prioritätsverfahren, Starvation und Fairness.  
  https://pages.cs.wisc.edu/~remzi/OSTEP/

## Woche 4 — Prozessmodell / Process Control Block (PCB)
- **OSTEP — Processes & Threads** — Lebenszyklus eines Prozesses, PCB‑Felder, Zustände (NEW, READY, RUNNING, BLOCKED).  
  https://pages.cs.wisc.edu/~remzi/OSTEP/

## Woche 5 — Kontextwechsel & Overhead
- **Wikipedia — Context switch** — kurzer, technischer Überblick, typische Quellen für Messgrößen/Overheads.  
  https://en.wikipedia.org/wiki/Context_switch

## Woche 6 — Interprozess‑Kommunikation (IPC)
- **Beej’s Guide to Unix IPC** — sehr praxisorientiert, erklärt Pipes, FIFOs, Message Queues, Shared Memory mit Beispielen.  
  http://beej.us/guide/bgipc/

## Woche 7 — Synchronisation: Locks, Semaphoren, Race Conditions
- **The Little Book of Semaphores (Allen B. Downey)** — didaktisch sehr gut, viele kleine Aufgaben und Beispiele (online verfügbar).  
  https://greenteapress.com/wp/semaphores/

## Woche 8 — Threading vs. Prozessmodell
- **OSTEP — Concurrency / Threads** — Konzepte zu Threads vs. Prozesse, Kontext, Modellunterschiede.  
  https://pages.cs.wisc.edu/~remzi/OSTEP/
- **POSIX threads Tutorial** — praktische Einführung in pthreads (API‑Beispiele).  
  https://computing.llnl.gov/tutorials/pthreads/

## Woche 9 — Virtual Memory: Paging (Grundlagen)
- **OSTEP — Virtual Memory** — Adressraumabbildung, Seiten/Frames, Seitentabellen, TLB.  
  https://pages.cs.wisc.edu/~remzi/OSTEP/

## Woche 10 — Page Replacement Algorithmen (FIFO, LRU, Clock)
- **OSTEP — VM Replacement** — erklärt Optimal, LRU, Clock, Belady‑Anomalie; gute Grundlage für Übungen.  
  https://pages.cs.wisc.edu/~remzi/OSTEP/

## Woche 11 — Dateisystem: Inodes & File API (open/read/write)
- **OSTEP — File Systems / Persistence** — Inode‑Modell, Verzeichnisstruktur, open/read/write semantics.  
  https://pages.cs.wisc.edu/~remzi/OSTEP/

## Woche 12 — Dateisystem: Directory‑Modelle & Allocation (FAT, Extents)
- **Übersicht: File system design** — Blogposts und Vorlesungsfolien zu FAT vs. indexed/inode/extent‑basierten Layouts (z. B. Universitätsfolien oder OSTEP‑Kapitel).  
  (Beispiele: Suche nach „file system implementation inodes extents“ in Vorlesungsressourcen.)

## Woche 13 — I/O Scheduling & Device Model
- **Linux kernel block layer documentation** — Überblick zu I/O‑Scheduler‑Konzepten und Implementationen.  
  https://www.kernel.org/doc/html/latest/block/

## Woche 14 — Sicherheit & Isolation (Namespaces / cgroups)
- **man7.org — Linux namespaces** — kompakte Referenz zu Namespaces; guter Einstieg in Container‑Grundlagen.  
  https://man7.org/linux/man-pages/man7/namespaces.7.html
- **cgroups overview (Kernel docs / tutorials)** — Einführungen zu cgroups für Ressourcenisolierung.  
  https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html

## Woche 15 — Abschlussprojekt & Vertiefung (xv6, MIT 6.828)
- **MIT xv6 / 6.828 Materials** — Lehr‑OS xv6, Labs und Begleitmaterial (ideal für Vertiefungsprojekte).  
  https://pdos.csail.mit.edu/6.828/

---

## Generelle Empfehlungen / zusätzliche Links
- **OSTEP (vollständiges Buch / Slides)** — die zentrale, freie Referenz für viele Themen.  
  https://pages.cs.wisc.edu/~remzi/OSTEP/
- **Beej’s Guide (IPC)** — für praktische Beispiele zu Pipes/Sockets/Shared Memory.  
  http://beej.us/guide/bgipc/
- **The Little Book of Semaphores** — Übungen zu Synchronisation.  
  https://greenteapress.com/wp/semaphores/

