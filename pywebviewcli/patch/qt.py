# Patches on_load_finished in such a way so that web inspector doesn't show on load (Qt Web View)
# User can still open it from context menu
def patch_on_load_finished():
    try:
        from webview.platforms.qt import BrowserView

        import webview

        on_load_finished = BrowserView.on_load_finished

        def new_on_load_finished(self):
            old_value = webview._settings["debug"]
            webview._settings["debug"] = False
            on_load_finished(self)
            webview._settings["debug"] = old_value

        BrowserView.on_load_finished = new_on_load_finished
    except:
        return
