import webview


def reload_window(window: webview.Window):
    window.evaluate_js("location.reload();")


# src contains js bridge for python code, we add reload listener here
def add_reload_listener():
    webview.js.api.src += """
    \n\nconsole.log("Registering event listener to reload (API + UI) (f5)");
    window.addEventListener('keydown', function(event) {
        const isF5Pressed = event.key === 'F5';
        if (isF5Pressed) {
            console.log("Reloading the entire app (API + UI)");
            window.pywebview.api.reload_all();
            event.preventDefault();
        }
    });
    """
