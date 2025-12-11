\
    from typing import Any
    from src.student.pcb import ProcessControlBlock, ProcessState


    def create_pcb_from_process(process: Any) -> ProcessControlBlock:
        \"\"\"Create a PCB from an existing lightweight Process-like object.

        The Process-like object must have attributes: pid, arrival, burst, remaining, priority
        \"\"\"
        pcb = ProcessControlBlock(
            pid=process.pid,
            arrival=getattr(process, "arrival", 0.0),
            burst=getattr(process, "burst", getattr(process, "remaining", 0.0)),
            remaining=getattr(process, "remaining", None),
            priority=getattr(process, "priority", 0),
        )
        return pcb


    def attach_pcb_to_process(process: Any) -> ProcessControlBlock:
        \"\"\"Attach a PCB to a process instance (in-place) and return the PCB.\"\"\"
        pcb = create_pcb_from_process(process)
        setattr(process, "pcb", pcb)
        return pcb


    # Small helpers used by simulators

    def on_dispatch_start(pcb: ProcessControlBlock):
        pcb.set_state(ProcessState.RUNNING)

    def on_dispatch_stop(pcb: ProcessControlBlock):
        # if remaining == 0 => terminated
        if pcb.remaining <= 0:
            pcb.set_state(ProcessState.TERMINATED)
        else:
            pcb.set_state(ProcessState.READY)

    def on_block(pcb: ProcessControlBlock):
        pcb.set_state(ProcessState.BLOCKED)

    def on_unblock(pcb: ProcessControlBlock):
        pcb.set_state(ProcessState.READY)
