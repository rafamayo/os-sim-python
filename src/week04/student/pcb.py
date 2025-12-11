\
    from dataclasses import dataclass, field
    from enum import Enum, auto
    from typing import Dict, Any, List


    class ProcessState(Enum):
        NEW = auto()
        READY = auto()
        RUNNING = auto()
        BLOCKED = auto()
        TERMINATED = auto()


    @dataclass
    class ProcessControlBlock:
        """
        Lightweight Process Control Block implementation for teaching.
        """

        pid: int
        state: ProcessState = ProcessState.NEW
        arrival: float = 0.0
        burst: float = 1.0
        remaining: float = field(default=None)
        priority: int = 0
        registers: Dict[str, Any] = field(default_factory=dict)
        fd_table: List[Any] = field(default_factory=list)

        def __post_init__(self):
            if self.remaining is None:
                self.remaining = float(self.burst)

        def set_state(self, new_state: ProcessState) -> None:
            \"\"\"Set the PCB state. Simple validation included.\"\"\"
            if self.state == ProcessState.TERMINATED:
                raise RuntimeError(\"Cannot change state of terminated process\") from None
            # Optionally: validate allowed transitions here
            self.state = new_state

        def is_terminated(self) -> bool:
            return self.state == ProcessState.TERMINATED

        def snapshot(self) -> Dict[str, Any]:
            \"\"\"Return a JSON-serializable snapshot of the PCB (for logging/tests).\"\"\"
            return {
                \"pid\": self.pid,
                \"state\": self.state.name,
                \"arrival\": self.arrival,
                \"burst\": self.burst,
                \"remaining\": self.remaining,
                \"priority\": self.priority,
                \"registers\": dict(self.registers),
                \"fd_table_len\": len(self.fd_table),
            }
