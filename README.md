# Reflex Global Hotkey Watcher

Listens to hotkeys in the global scope and calls event handler as necessary.

```python
from reflex_global_hotkey import global_hotkey_watcher

class State(rx.State):
    last_key_pressed: str = ""

    def on_key(self, keyname: str):
        self.last_key_pressed = keyname

def index():
    return rx.fragment(
        State.last_key_pressed,
        global_hotkey_watcher(
            on_key_down=State.on_key
        )
    )
```

You can special case on the event key:

```python
global_hotkey_watcher(
    on_key_down=lambda key_name: rx.cond(
        rx.Var.create(
            ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"]
        ).contains(key_name),
        State.on_key(key_name),
        rx.console_log("Invalid key!"),
    )
)
```
