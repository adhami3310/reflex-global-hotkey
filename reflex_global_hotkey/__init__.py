"""A Reflex component that listens for key events globally."""

from reflex import Fragment, Var
from reflex.event import EventHandler, EventType, key_event
from reflex.utils import imports


class GlobalHotkeyWatcher(Fragment):
    """A component that listens for key events globally."""

    # The event handler that will be called
    on_key_down: EventHandler[key_event]

    def add_imports(self) -> imports.ImportDict:
        """Add the imports for the component."""
        return {
            "react": [imports.ImportVar(tag="useEffect")],
        }

    def add_hooks(self) -> list[str | Var]:
        """Add the hooks for the component."""
        return [
            """
            useEffect(() => {
                const handle_key = %s;
                document.addEventListener("keydown", handle_key, false);
                return () => {
                    document.removeEventListener("keydown", handle_key, false);
                }
            })
            """
            % str(Var.create(self.event_triggers["on_key_down"]))
        ]

    def render(self) -> dict:
        """Render the component."""
        return {
            "name": "Fragment",
            "contents": "",
            "children": [],
            "props": {},
        }


def global_hotkey_watcher(on_key_down: EventType) -> GlobalHotkeyWatcher:
    """Create a GlobalHotkeyWatcher component."""
    return GlobalHotkeyWatcher(on_key_down=on_key_down)
